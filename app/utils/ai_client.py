"""AI Client utility for handling API calls to different AI providers"""

import requests
import json
import os
from typing import Dict, Any, Optional
import time
import random

class AIClient:
    """Client for making requests to various AI APIs"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'AI-Generator/1.0'
        })
    
    def generate_response(self, model_id: str, prompt: str, 
                         temperature: float = 0.7, max_tokens: int = 500, 
                         top_p: float = 0.9, api_key: Optional[str] = None) -> Dict[str, Any]:
        """Generate response from AI model"""
        
        from app.models.ai_models import get_model_by_id
        
        model = get_model_by_id(model_id)
        if not model:
            return {
                'success': False,
                'error': f'Model {model_id} not found'
            }
        
        # Check for API key
        if not api_key:
            api_key = self._get_api_key(model.provider)
        
        if not api_key:
            return self._simulate_response(prompt, model)
        
        try:
            if model.provider == 'Groq':
                return self._call_groq(model, prompt, temperature, max_tokens, top_p, api_key)
            elif model.provider == 'HuggingFace':
                return self._call_huggingface(model, prompt, temperature, max_tokens, top_p, api_key)
            elif model.provider == 'OpenAI':
                return self._call_openai(model, prompt, temperature, max_tokens, top_p, api_key)
            else:
                return self._simulate_response(prompt, model)
                
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'response': None
            }
    
    def _get_api_key(self, provider: str) -> Optional[str]:
        """Get API key from environment variables"""
        key_map = {
            'Groq': 'GROQ_API_KEY',
            'HuggingFace': 'HUGGINGFACE_API_KEY',
            'OpenAI': 'OPENAI_API_KEY'
        }
        return os.getenv(key_map.get(provider))
    
    def _call_groq(self, model, prompt: str, temperature: float, 
                   max_tokens: int, top_p: float, api_key: str) -> Dict[str, Any]:
        """Call Groq API"""
        
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'model': model.model_name,
            'messages': [
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            'temperature': temperature,
            'max_tokens': max_tokens,
            'top_p': top_p
        }
        
        response = self.session.post(model.endpoint, headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return {
                'success': True,
                'response': result['choices'][0]['message']['content'],
                'model': model.name,
                'provider': model.provider
            }
        else:
            return {
                'success': False,
                'error': f'Groq API error: {response.status_code}',
                'response': None
            }
    
    def _call_huggingface(self, model, prompt: str, temperature: float,
                         max_tokens: int, top_p: float, api_key: str) -> Dict[str, Any]:
        """Call HuggingFace API"""
        
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'inputs': prompt,
            'parameters': {
                'temperature': temperature,
                'max_new_tokens': max_tokens,
                'top_p': top_p,
                'return_full_text': False
            }
        }
        
        response = self.session.post(model.endpoint, headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            
            # Handle different response formats
            if isinstance(result, list) and len(result) > 0:
                generated_text = result[0].get('generated_text', '')
            elif isinstance(result, dict):
                generated_text = result.get('generated_text', '')
            else:
                generated_text = str(result)
            
            return {
                'success': True,
                'response': generated_text,
                'model': model.name,
                'provider': model.provider
            }
        else:
            return {
                'success': False,
                'error': f'HuggingFace API error: {response.status_code}',
                'response': None
            }
    
    def _call_openai(self, model, prompt: str, temperature: float,
                    max_tokens: int, top_p: float, api_key: str) -> Dict[str, Any]:
        """Call OpenAI API"""
        
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
        data = {
            'model': model.model_name,
            'messages': [
                {
                    'role': 'user',
                    'content': prompt
                }
            ],
            'temperature': temperature,
            'max_tokens': max_tokens,
            'top_p': top_p
        }
        
        response = self.session.post(model.endpoint, headers=headers, json=data, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return {
                'success': True,
                'response': result['choices'][0]['message']['content'],
                'model': model.name,
                'provider': model.provider
            }
        else:
            return {
                'success': False,
                'error': f'OpenAI API error: {response.status_code}',
                'response': None
            }
    
    def _simulate_response(self, prompt: str, model) -> Dict[str, Any]:
        """Simulate AI response for demo purposes"""
        
        # Simulate processing time
        time.sleep(random.uniform(1, 3))
        
        demo_responses = [
            f"Ini adalah respons demo dari {model.name}! 🤖\n\nPrompt Anda: \"{prompt[:100]}{'...' if len(prompt) > 100 else ''}\"\n\nUntuk menggunakan AI model yang sebenarnya, silakan:\n1. Dapatkan API key gratis dari {model.provider}\n2. Set environment variable atau masukkan via form\n3. Nikmati AI yang powerful!\n\nDemo mode ini menunjukkan bagaimana interface bekerja dengan response yang sesungguhnya.",
            
            f"🎯 Respons Demo dari {model.provider}\n\nSaya memahami permintaan Anda tentang: \"{prompt[:80]}{'...' if len(prompt) > 80 else ''}\"\n\nDalam mode demo ini, saya memberikan respons simulasi. Untuk mendapatkan analisis AI yang sesungguhnya:\n\n✅ Daftar API key gratis di platform {model.provider}\n✅ Konfigurasi key di environment\n✅ Restart aplikasi\n\nInterface ini sudah siap untuk integrasi real AI!",
            
            f"🔮 Demo Response Generator\n\nModel: {model.name}\nProvider: {model.provider}\n\nAnda bertanya: \"{prompt[:60]}{'...' if len(prompt) > 60 else ''}\"\n\nIni adalah simulasi respons AI. Fitur-fitur yang tersedia:\n• Template prompts\n• Parameter tuning\n• History penyimpanan\n• Export results\n\nSiap upgrade ke real AI? Dapatkan API key gratis dan rasakan perbedaannya!"
        ]
        
        return {
            'success': True,
            'response': random.choice(demo_responses),
            'model': f"{model.name} (Demo)",
            'provider': model.provider,
            'is_demo': True
        }

# Global AI client instance
ai_client = AIClient()