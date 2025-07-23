from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

def create_app(config_name='development'):
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Enable CORS
    CORS(app)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    app.config['DEBUG'] = os.getenv('DEBUG', 'True').lower() == 'true'
    
    # Register blueprints
    from app.views.main import main_bp
    from app.views.api import api_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # Custom template filters
    @app.template_filter('truncate_words')
    def truncate_words(text, count=20):
        """Truncate text to specified word count"""
        words = text.split()
        if len(words) <= count:
            return text
        return ' '.join(words[:count]) + '...'
    
    @app.template_filter('format_timestamp')
    def format_timestamp(timestamp):
        """Format timestamp for display"""
        from datetime import datetime
        if isinstance(timestamp, str):
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
        else:
            dt = timestamp
        return dt.strftime('%d %b %Y, %H:%M')
    
    return app