import os
import json
import csv
import pandas as pd
from jinja2 import Environment, FileSystemLoader, Template
from typing import Dict, List, Any, Union
import yaml
from pathlib import Path

class TemplateGenerator:
    """
    Modular template generator dengan support untuk input CSV, JSON, dan AI
    """
    
    def __init__(self, templates_dir: str = "templates"):
        self.templates_dir = Path(templates_dir)
        self.templates_dir.mkdir(exist_ok=True)
        
        # Setup Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(self.templates_dir),
            trim_blocks=True,
            lstrip_blocks=True
        )
        
        # Custom filters untuk template
        self.env.filters['markdown'] = self._markdown_filter
        self.env.filters['truncate_words'] = self._truncate_words
        self.env.filters['capitalize_words'] = self._capitalize_words
        self.env.filters['safe_url'] = self._safe_url_filter
    
    def _markdown_filter(self, text):
        """Convert markdown to HTML"""
        try:
            import markdown
            return markdown.markdown(text)
        except ImportError:
            return text
    
    def _truncate_words(self, text, length=100):
        """Truncate text to specified word count"""
        words = str(text).split()
        if len(words) > length:
            return ' '.join(words[:length]) + '...'
        return text
    
    def _capitalize_words(self, text):
        """Capitalize each word"""
        return str(text).title()
    
    def _safe_url_filter(self, url):
        """Ensure URL is safe and formatted correctly"""
        if not url:
            return "#"
        if not url.startswith(('http://', 'https://')):
            return f"https://{url}"
        return url
    
    def load_csv_data(self, csv_file: str) -> List[Dict]:
        """Load data from CSV file"""
        try:
            df = pd.read_csv(csv_file)
            return df.to_dict('records')
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return []
    
    def load_json_data(self, json_file: str) -> Union[Dict, List]:
        """Load data from JSON file"""
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading JSON: {e}")
            return {}
    
    def load_ai_data(self, ai_data: Dict) -> Dict:
        """Process AI-generated data"""
        # Handle potential issues with AI data
        processed_data = {}
        
        for key, value in ai_data.items():
            if isinstance(value, str):
                # Clean up potential AI artifacts
                value = value.replace('```', '').strip()
                # Handle potential image references
                if 'image' in key.lower() and not value.startswith(('http', 'data:')):
                    value = f"/static/images/{value}"
            
            processed_data[key] = value
        
        return processed_data
    
    def generate_content(self, template_name: str, data: Union[Dict, List], output_file: str = None) -> str:
        """Generate content using specified template and data"""
        try:
            template = self.env.get_template(template_name)
            
            if isinstance(data, list):
                # For CSV data (list of dictionaries)
                content = template.render(items=data, data=data)
            else:
                # For JSON or AI data (dictionary)
                content = template.render(**data, data=data)
            
            if output_file:
                output_path = Path(output_file)
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Content generated: {output_file}")
            
            return content
            
        except Exception as e:
            print(f"Error generating content: {e}")
            return ""
    
    def batch_generate(self, template_name: str, data_sources: List[Dict], output_dir: str = "output"):
        """Generate multiple content files from various data sources"""
        output_path = Path(output_dir)
        output_path.mkdir(exist_ok=True)
        
        for i, source in enumerate(data_sources):
            source_type = source.get('type')
            source_path = source.get('path')
            output_name = source.get('output', f"content_{i}.html")
            
            if source_type == 'csv':
                data = self.load_csv_data(source_path)
            elif source_type == 'json':
                data = self.load_json_data(source_path)
            elif source_type == 'ai':
                data = self.load_ai_data(source.get('data', {}))
            else:
                continue
            
            output_file = output_path / output_name
            self.generate_content(template_name, data, str(output_file))
    
    def list_templates(self) -> List[str]:
        """List available templates"""
        templates = []
        for file in self.templates_dir.glob("*.html"):
            templates.append(file.name)
        return templates