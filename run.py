#!/usr/bin/env python3
"""
AI Generator - Flask Application
Main entry point for the AI Generator application
"""

import os
from app import create_app

# Create Flask application
app = create_app()

if __name__ == '__main__':
    # Get configuration from environment
    debug = os.getenv('DEBUG', 'True').lower() == 'true'
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 5000))
    
    print(f"""
🤖 AI Generator - Starting Server
================================

Server: http://{host}:{port}
Debug: {debug}
Environment: {os.getenv('NODE_ENV', 'development')}

Available AI Models:
- Groq (Llama 3.1 70B) - Free tier
- HuggingFace - Free tier  
- OpenAI GPT-3.5 - API key required
- Cohere - Free trial

Setup Instructions:
1. Set API keys as environment variables (optional):
   export GROQ_API_KEY="your_groq_key"
   export HUGGINGFACE_API_KEY="your_hf_token"
   export OPENAI_API_KEY="your_openai_key"

2. Or configure via web interface

Ready to generate! 🚀
    """)
    
    app.run(
        host=host,
        port=port,
        debug=debug,
        threaded=True
    )