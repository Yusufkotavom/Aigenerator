"""API views for handling AJAX requests and AI generation"""

from flask import Blueprint, request, jsonify, session, send_file
from app.utils.ai_client import ai_client
from app.models.ai_models import get_model_by_id
from app.models.prompts import get_template_by_id, search_templates
from app.utils.bulk_generator import bulk_generator
import datetime
import uuid
import io

api_bp = Blueprint('api', __name__)

@api_bp.route('/generate', methods=['POST'])
def generate():
    """Generate AI response"""
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data or 'prompt' not in data or 'model_id' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing required fields: prompt and model_id'
            }), 400
        
        prompt = data['prompt'].strip()
        model_id = data['model_id']
        
        if not prompt:
            return jsonify({
                'success': False,
                'error': 'Prompt cannot be empty'
            }), 400
        
        # Get model
        model = get_model_by_id(model_id)
        if not model:
            return jsonify({
                'success': False,
                'error': f'Model {model_id} not found'
            }), 404
        
        # Get parameters with defaults
        temperature = float(data.get('temperature', 0.7))
        max_tokens = int(data.get('max_tokens', 500))
        top_p = float(data.get('top_p', 0.9))
        api_key = data.get('api_key')
        
        # Validate parameters
        temperature = max(0.0, min(1.0, temperature))
        max_tokens = max(50, min(2000, max_tokens))
        top_p = max(0.0, min(1.0, top_p))
        
        # Generate response
        result = ai_client.generate_response(
            model_id=model_id,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            api_key=api_key
        )
        
        # Add generation metadata
        if result['success']:
            result['metadata'] = {
                'timestamp': datetime.datetime.now().isoformat(),
                'model_id': model_id,
                'parameters': {
                    'temperature': temperature,
                    'max_tokens': max_tokens,
                    'top_p': top_p
                },
                'prompt_length': len(prompt),
                'response_length': len(result['response']) if result['response'] else 0
            }
            
            # Store in session history
            if 'generation_history' not in session:
                session['generation_history'] = []
            
            history_item = {
                'id': str(uuid.uuid4()),
                'timestamp': result['metadata']['timestamp'],
                'model': result['model'],
                'provider': result['provider'],
                'prompt': prompt[:200] + '...' if len(prompt) > 200 else prompt,
                'response': result['response'][:500] + '...' if len(result['response']) > 500 else result['response'],
                'parameters': result['metadata']['parameters']
            }
            
            session['generation_history'].insert(0, history_item)
            
            # Keep only last 50 items
            session['generation_history'] = session['generation_history'][:50]
            session.modified = True
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

# Bulk Generation Endpoints
@api_bp.route('/bulk/validate-csv', methods=['POST'])
def validate_csv():
    """Validate CSV data against template requirements"""
    try:
        data = request.get_json()
        
        if not data or 'csv_content' not in data or 'template_id' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing required fields: csv_content and template_id'
            }), 400
        
        csv_content = data['csv_content']
        template_id = data['template_id']
        
        result = bulk_generator.process_csv_data(csv_content, template_id)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/bulk/generate', methods=['POST'])
def bulk_generate():
    """Generate bulk content from CSV data"""
    try:
        data = request.get_json()
        
        required_fields = ['csv_data', 'template_id', 'model_id']
        if not data or not all(field in data for field in required_fields):
            return jsonify({
                'success': False,
                'error': f'Missing required fields: {", ".join(required_fields)}'
            }), 400
        
        csv_data = data['csv_data']
        template_id = data['template_id']
        model_id = data['model_id']
        output_format = data.get('output_format', 'html')
        use_ai_enhancement = data.get('use_ai_enhancement', False)
        api_key = data.get('api_key')
        
        if not csv_data:
            return jsonify({
                'success': False,
                'error': 'CSV data is empty'
            }), 400
        
        result = bulk_generator.generate_bulk_content(
            csv_data=csv_data,
            template_id=template_id,
            model_id=model_id,
            output_format=output_format,
            use_ai_enhancement=use_ai_enhancement,
            api_key=api_key
        )
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/bulk/download', methods=['POST'])
def bulk_download():
    """Download bulk generation results as ZIP"""
    try:
        data = request.get_json()
        
        if not data or 'results' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing results data'
            }), 400
        
        results = data['results']
        summary = data.get('summary', {})
        template_name = data.get('template_name', 'unknown')
        
        # Create ZIP package
        zip_data = bulk_generator.create_download_package(
            results=results,
            summary=summary,
            template_name=template_name
        )
        
        # Create response
        zip_file = io.BytesIO(zip_data)
        zip_file.seek(0)
        
        return send_file(
            zip_file,
            mimetype='application/zip',
            as_attachment=True,
            download_name=f'bulk_content_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.zip'
        )
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/templates/search', methods=['GET'])
def search_templates_api():
    """Search templates by query"""
    try:
        query = request.args.get('q', '').strip()
        
        if not query:
            return jsonify({
                'success': False,
                'error': 'Query parameter is required'
            }), 400
        
        results = search_templates(query)
        
        return jsonify({
            'success': True,
            'results': [template.to_dict() for template in results],
            'count': len(results)
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/template/<template_id>', methods=['GET'])
def get_template_api(template_id):
    """Get template by ID"""
    try:
        template = get_template_by_id(template_id)
        
        if not template:
            return jsonify({
                'success': False,
                'error': 'Template not found'
            }), 404
        
        return jsonify({
            'success': True,
            'template': template.to_dict()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/history', methods=['GET'])
def get_history():
    """Get generation history"""
    try:
        history = session.get('generation_history', [])
        
        # Pagination
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        
        start = (page - 1) * per_page
        end = start + per_page
        
        paginated_history = history[start:end]
        
        return jsonify({
            'success': True,
            'history': paginated_history,
            'total': len(history),
            'page': page,
            'per_page': per_page,
            'total_pages': (len(history) + per_page - 1) // per_page
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/history/<history_id>', methods=['DELETE'])
def delete_history_item(history_id):
    """Delete history item"""
    try:
        history = session.get('generation_history', [])
        
        # Find and remove item
        updated_history = [item for item in history if item['id'] != history_id]
        
        if len(updated_history) == len(history):
            return jsonify({
                'success': False,
                'error': 'History item not found'
            }), 404
        
        session['generation_history'] = updated_history
        session.modified = True
        
        return jsonify({
            'success': True,
            'message': 'History item deleted'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/history/clear', methods=['POST'])
def clear_history():
    """Clear all history"""
    try:
        session['generation_history'] = []
        session.modified = True
        
        return jsonify({
            'success': True,
            'message': 'History cleared'
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/models', methods=['GET'])
def get_models_api():
    """Get all available models"""
    try:
        from app.models.ai_models import get_all_models
        
        models = get_all_models()
        
        return jsonify({
            'success': True,
            'models': [model.to_dict() for model in models]
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@api_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat(),
        'version': '1.0.0'
    })