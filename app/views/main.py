"""Main views for the AI Generator web interface"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from app.models.ai_models import get_all_models, get_model_by_id
from app.models.prompts import get_all_templates, get_template_categories, get_template_by_id
from app.models.content_templates import (
    get_all_content_templates, 
    get_content_template_categories,
    get_content_template_by_id
)

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """Home page"""
    models = get_all_models()
    templates = get_all_templates()
    categories = get_template_categories()
    
    return render_template('index.html', 
                         models=models, 
                         templates=templates, 
                         categories=categories)

@main_bp.route('/generator')
def generator():
    """AI Generator page"""
    models = get_all_models()
    templates = get_all_templates()
    categories = get_template_categories()
    
    # Get selected model from query params
    selected_model_id = request.args.get('model', 'groq-llama')
    selected_model = get_model_by_id(selected_model_id)
    
    return render_template('generator.html',
                         models=models,
                         templates=templates,
                         categories=categories,
                         selected_model=selected_model)

@main_bp.route('/bulk-generator')
def bulk_generator():
    """Bulk Content Generator page"""
    models = get_all_models()
    content_templates = [template.to_dict() for template in get_all_content_templates()]
    content_categories = get_content_template_categories()
    
    return render_template('bulk_generator.html',
                         models=models,
                         content_templates=content_templates,
                         content_categories=content_categories)

@main_bp.route('/templates')
def templates():
    """Template library page"""
    all_templates = get_all_templates()
    categories = get_template_categories()
    
    # Filter by category if specified
    category_filter = request.args.get('category')
    if category_filter:
        filtered_templates = [t for t in all_templates if t.category == category_filter]
    else:
        filtered_templates = all_templates
    
    return render_template('templates.html',
                         templates=filtered_templates,
                         categories=categories,
                         selected_category=category_filter)

@main_bp.route('/content-templates')
def content_templates():
    """Content template library page"""
    all_templates = get_all_content_templates()
    categories = get_content_template_categories()
    
    # Filter by category if specified
    category_filter = request.args.get('category')
    if category_filter:
        filtered_templates = [t for t in all_templates if t.category == category_filter]
    else:
        filtered_templates = all_templates
    
    return render_template('content_templates.html',
                         templates=filtered_templates,
                         categories=categories,
                         selected_category=category_filter)

@main_bp.route('/template/<template_id>')
def template_detail(template_id):
    """Template detail page"""
    template = get_template_by_id(template_id)
    if not template:
        flash('Template tidak ditemukan', 'error')
        return redirect(url_for('main.templates'))
    
    return render_template('template_detail.html', template=template)

@main_bp.route('/content-template/<template_id>')
def content_template_detail(template_id):
    """Content template detail page"""
    template = get_content_template_by_id(template_id)
    if not template:
        flash('Content template tidak ditemukan', 'error')
        return redirect(url_for('main.content_templates'))
    
    return render_template('content_template_detail.html', template=template)

@main_bp.route('/models')
def models():
    """AI Models overview page"""
    all_models = get_all_models()
    
    # Group models by provider
    providers = {}
    for model in all_models:
        if model.provider not in providers:
            providers[model.provider] = []
        providers[model.provider].append(model)
    
    return render_template('models.html', 
                         models=all_models,
                         providers=providers)

@main_bp.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@main_bp.route('/help')
def help_page():
    """Help and documentation page"""
    return render_template('help.html')

@main_bp.route('/settings')
def settings():
    """Settings page"""
    return render_template('settings.html')