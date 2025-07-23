"""Bulk Content Generator with CSV support"""

import csv
import io
import json
import os
import zipfile
from typing import List, Dict, Any, Optional
import pandas as pd
from datetime import datetime
import asyncio
import concurrent.futures
from app.utils.ai_client import ai_client
from app.models.content_templates import get_content_template_by_id

class BulkContentGenerator:
    """Bulk content generator for WordPress and other platforms"""
    
    def __init__(self):
        self.ai_client = ai_client
        self.supported_formats = ['html', 'wordpress', 'markdown', 'json']
    
    def process_csv_data(self, csv_content: str, template_id: str) -> Dict[str, Any]:
        """Process CSV data and validate against template requirements"""
        
        template = get_content_template_by_id(template_id)
        if not template:
            return {
                'success': False,
                'error': f'Template {template_id} not found'
            }
        
        try:
            # Parse CSV
            csv_file = io.StringIO(csv_content)
            reader = csv.DictReader(csv_file)
            rows = list(reader)
            
            if not rows:
                return {
                    'success': False,
                    'error': 'CSV file is empty'
                }
            
            # Validate required fields
            csv_headers = set(rows[0].keys())
            required_fields = set(template.fields)
            missing_fields = required_fields - csv_headers
            
            if missing_fields:
                return {
                    'success': False,
                    'error': f'Missing required fields: {", ".join(missing_fields)}',
                    'missing_fields': list(missing_fields),
                    'required_fields': template.fields,
                    'found_fields': list(csv_headers)
                }
            
            return {
                'success': True,
                'data': rows,
                'template': template,
                'row_count': len(rows),
                'preview': rows[:3]  # First 3 rows for preview
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'Error processing CSV: {str(e)}'
            }
    
    def generate_bulk_content(self, csv_data: List[Dict], template_id: str, 
                            model_id: str, output_format: str = 'html',
                            use_ai_enhancement: bool = False,
                            api_key: Optional[str] = None) -> Dict[str, Any]:
        """Generate bulk content from CSV data"""
        
        template = get_content_template_by_id(template_id)
        if not template:
            return {
                'success': False,
                'error': f'Template {template_id} not found'
            }
        
        if output_format not in self.supported_formats:
            return {
                'success': False,
                'error': f'Unsupported output format. Supported: {", ".join(self.supported_formats)}'
            }
        
        results = []
        errors = []
        
        # Process each row
        for i, row in enumerate(csv_data):
            try:
                # Generate content for this row
                content_result = self._generate_single_content(
                    row, template, model_id, output_format, 
                    use_ai_enhancement, api_key, i + 1
                )
                
                if content_result['success']:
                    results.append(content_result)
                else:
                    errors.append({
                        'row': i + 1,
                        'data': row,
                        'error': content_result['error']
                    })
                    
            except Exception as e:
                errors.append({
                    'row': i + 1,
                    'data': row,
                    'error': str(e)
                })
        
        # Create summary
        summary = {
            'total_rows': len(csv_data),
            'successful': len(results),
            'failed': len(errors),
            'success_rate': (len(results) / len(csv_data)) * 100 if csv_data else 0
        }
        
        return {
            'success': True,
            'results': results,
            'errors': errors,
            'summary': summary,
            'template_used': template.name,
            'output_format': output_format,
            'generated_at': datetime.now().isoformat()
        }
    
    def _generate_single_content(self, row_data: Dict, template, model_id: str,
                               output_format: str, use_ai_enhancement: bool,
                               api_key: Optional[str], row_number: int) -> Dict[str, Any]:
        """Generate content for a single row"""
        
        try:
            # Replace placeholders in template
            html_content = self._replace_template_placeholders(
                template.html_template, row_data
            )
            
            # Enhance with AI if requested
            if use_ai_enhancement:
                enhanced_content = self._enhance_with_ai(
                    html_content, row_data, model_id, api_key
                )
                if enhanced_content:
                    html_content = enhanced_content
            
            # Format output
            formatted_content = self._format_content(
                html_content, template.css_styles, template.js_scripts, 
                output_format, row_data
            )
            
            # Generate filename
            filename = self._generate_filename(row_data, template, row_number, output_format)
            
            return {
                'success': True,
                'content': formatted_content,
                'filename': filename,
                'row_number': row_number,
                'data_used': row_data,
                'content_length': len(formatted_content)
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'row_number': row_number,
                'data_used': row_data
            }
    
    def _replace_template_placeholders(self, template_content: str, data: Dict) -> str:
        """Replace template placeholders with actual data"""
        
        content = template_content
        
        for key, value in data.items():
            placeholder = f"{{{key}}}"
            # Handle None values
            if value is None:
                value = ""
            # Convert to string
            value = str(value)
            content = content.replace(placeholder, value)
        
        return content
    
    def _enhance_with_ai(self, content: str, data: Dict, model_id: str, 
                        api_key: Optional[str]) -> Optional[str]:
        """Enhance content using AI"""
        
        try:
            # Create enhancement prompt
            prompt = f"""
            Please enhance and optimize the following HTML content for better engagement and SEO.
            Keep the structure intact but improve:
            1. Text quality and readability
            2. SEO-friendly descriptions
            3. Call-to-action effectiveness
            4. Overall content flow
            
            Original content:
            {content[:2000]}  # Limit content for prompt
            
            Enhanced version:
            """
            
            result = self.ai_client.generate_response(
                model_id=model_id,
                prompt=prompt,
                temperature=0.7,
                max_tokens=1500,
                api_key=api_key
            )
            
            if result['success']:
                return result['response']
            
        except Exception as e:
            print(f"AI enhancement failed: {e}")
        
        return None
    
    def _format_content(self, html_content: str, css_styles: str, 
                       js_scripts: str, output_format: str, data: Dict) -> str:
        """Format content according to output format"""
        
        if output_format == 'html':
            return self._format_as_html(html_content, css_styles, js_scripts)
        
        elif output_format == 'wordpress':
            return self._format_as_wordpress(html_content, css_styles, js_scripts, data)
        
        elif output_format == 'markdown':
            return self._format_as_markdown(html_content, data)
        
        elif output_format == 'json':
            return self._format_as_json(html_content, css_styles, js_scripts, data)
        
        else:
            return html_content
    
    def _format_as_html(self, content: str, css: str, js: str) -> str:
        """Format as complete HTML page"""
        
        return f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Content</title>
    <style>
        {css}
    </style>
</head>
<body>
    {content}
    
    <script>
        {js}
    </script>
</body>
</html>"""
    
    def _format_as_wordpress(self, content: str, css: str, js: str, data: Dict) -> str:
        """Format for WordPress post content"""
        
        # WordPress shortcode format
        wordpress_content = f"""<!-- wp:html -->
{content}
<!-- /wp:html -->

<!-- wp:html -->
<style>
{css}
</style>
<!-- /wp:html -->

<!-- wp:html -->
<script>
{js}
</script>
<!-- /wp:html -->"""
        
        return wordpress_content
    
    def _format_as_markdown(self, content: str, data: Dict) -> str:
        """Convert HTML to Markdown (basic conversion)"""
        
        # Basic HTML to Markdown conversion
        import re
        
        markdown = content
        
        # Convert headers
        markdown = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', markdown)
        markdown = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', markdown)
        markdown = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', markdown)
        
        # Convert paragraphs
        markdown = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', markdown)
        
        # Convert links
        markdown = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', markdown)
        
        # Convert images
        markdown = re.sub(r'<img[^>]*src="([^"]*)"[^>]*alt="([^"]*)"[^>]*/?>', r'![\2](\1)', markdown)
        
        # Remove remaining HTML tags
        markdown = re.sub(r'<[^>]+>', '', markdown)
        
        return markdown
    
    def _format_as_json(self, content: str, css: str, js: str, data: Dict) -> str:
        """Format as JSON structure"""
        
        json_data = {
            'content': {
                'html': content,
                'css': css,
                'javascript': js
            },
            'data': data,
            'meta': {
                'generated_at': datetime.now().isoformat(),
                'content_length': len(content),
                'format': 'json'
            }
        }
        
        return json.dumps(json_data, indent=2, ensure_ascii=False)
    
    def _generate_filename(self, data: Dict, template, row_number: int, 
                          output_format: str) -> str:
        """Generate filename for the content"""
        
        # Try to use a meaningful name from data
        name_fields = ['title', 'name', 'business_name', 'product_name', 'event_title']
        filename = None
        
        for field in name_fields:
            if field in data and data[field]:
                filename = str(data[field])
                break
        
        if not filename:
            filename = f"{template.id}_row_{row_number}"
        
        # Clean filename
        filename = "".join(c for c in filename if c.isalnum() or c in (' ', '-', '_')).rstrip()
        filename = filename.replace(' ', '_').lower()
        
        # Add extension
        extensions = {
            'html': '.html',
            'wordpress': '.txt',
            'markdown': '.md',
            'json': '.json'
        }
        
        return f"{filename}{extensions.get(output_format, '.txt')}"
    
    def create_download_package(self, results: List[Dict], 
                              summary: Dict, template_name: str) -> bytes:
        """Create ZIP package for download"""
        
        zip_buffer = io.BytesIO()
        
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            
            # Add generated content files
            for result in results:
                if result['success']:
                    zip_file.writestr(
                        result['filename'],
                        result['content']
                    )
            
            # Add summary report
            summary_content = f"""Content Generation Summary
Generated at: {summary.get('generated_at', 'Unknown')}
Template: {template_name}
Output Format: {summary.get('output_format', 'Unknown')}

Statistics:
- Total rows processed: {summary.get('total_rows', 0)}
- Successful generations: {summary.get('successful', 0)}
- Failed generations: {summary.get('failed', 0)}
- Success rate: {summary.get('success_rate', 0):.1f}%

Generated Files:
"""
            
            for i, result in enumerate(results, 1):
                if result['success']:
                    summary_content += f"{i}. {result['filename']} ({result['content_length']} chars)\n"
            
            zip_file.writestr('_SUMMARY.txt', summary_content)
            
            # Add CSV template for future use
            csv_template = "# CSV Template for this content type\n"
            csv_template += "# Required fields: " + ", ".join(get_content_template_by_id(template_name).fields if get_content_template_by_id(template_name) else []) + "\n"
            zip_file.writestr('_csv_template.txt', csv_template)
        
        zip_buffer.seek(0)
        return zip_buffer.getvalue()

# Global bulk generator instance
bulk_generator = BulkContentGenerator()