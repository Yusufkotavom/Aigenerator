"""AI Models configuration and data structures"""

class AIModel:
    """AI Model data structure"""
    
    def __init__(self, model_id, name, provider, description, model_type, 
                 endpoint, model_name, icon, color, free_tier=True, 
                 rate_limit=None, context_length=None):
        self.id = model_id
        self.name = name
        self.provider = provider
        self.description = description
        self.type = model_type
        self.endpoint = endpoint
        self.model_name = model_name
        self.icon = icon
        self.color = color
        self.free_tier = free_tier
        self.rate_limit = rate_limit
        self.context_length = context_length
    
    def to_dict(self):
        """Convert model to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'provider': self.provider,
            'description': self.description,
            'type': self.type,
            'endpoint': self.endpoint,
            'model_name': self.model_name,
            'icon': self.icon,
            'color': self.color,
            'free_tier': self.free_tier,
            'rate_limit': self.rate_limit,
            'context_length': self.context_length
        }

# Available AI Models
AVAILABLE_MODELS = [
    AIModel(
        model_id='groq-llama',
        name='Llama 3.1 70B',
        provider='Groq',
        description='Lightning-fast inference dengan Groq',
        model_type='Chat Completion',
        endpoint='https://api.groq.com/openai/v1/chat/completions',
        model_name='llama-3.1-70b-versatile',
        icon='fas fa-rocket',
        color='bg-orange-500',
        rate_limit='30 requests/minute',
        context_length=32768
    ),
    AIModel(
        model_id='gemini-pro',
        name='Gemini Pro',
        provider='Google',
        description='Google Gemini Pro - Advanced reasoning',
        model_type='Chat Completion',
        endpoint='https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent',
        model_name='gemini-pro',
        icon='fas fa-google',
        color='bg-blue-500',
        rate_limit='60 requests/minute',
        context_length=32768
    ),
    AIModel(
        model_id='gemini-flash',
        name='Gemini 1.5 Flash',
        provider='Google',
        description='Google Gemini Flash - Fast & efficient',
        model_type='Chat Completion',
        endpoint='https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent',
        model_name='gemini-1.5-flash',
        icon='fas fa-bolt',
        color='bg-yellow-500',
        rate_limit='1500 requests/day',
        context_length=1048576
    ),
    AIModel(
        model_id='huggingface-gpt2',
        name='GPT-2 Medium',
        provider='HuggingFace',
        description='Text generation via HuggingFace',
        model_type='Text Generation',
        endpoint='https://api-inference.huggingface.co/models/gpt2-medium',
        model_name='gpt2-medium',
        icon='fas fa-brain',
        color='bg-yellow-600',
        rate_limit='1000 requests/month',
        context_length=1024
    ),
    AIModel(
        model_id='huggingface-flan',
        name='FLAN-T5 Large',
        provider='HuggingFace',
        description='Instruction-tuned model via HuggingFace',
        model_type='Text Generation',
        endpoint='https://api-inference.huggingface.co/models/google/flan-t5-large',
        model_name='google/flan-t5-large',
        icon='fas fa-lightbulb',
        color='bg-green-500',
        rate_limit='1000 requests/month',
        context_length=512
    ),
    AIModel(
        model_id='openai-gpt35',
        name='GPT-3.5 Turbo',
        provider='OpenAI',
        description='OpenAI GPT-3.5 Turbo model',
        model_type='Chat Completion',
        endpoint='https://api.openai.com/v1/chat/completions',
        model_name='gpt-3.5-turbo',
        icon='fas fa-magic',
        color='bg-blue-600',
        rate_limit='3 requests/minute (free)',
        context_length=4096
    ),
    AIModel(
        model_id='cohere-command',
        name='Command R+',
        provider='Cohere',
        description='Cohere Command R+ model',
        model_type='Chat Completion',
        endpoint='https://api.cohere.ai/v1/chat',
        model_name='command-r-plus',
        icon='fas fa-comments',
        color='bg-purple-500',
        rate_limit='Free trial available',
        context_length=128000
    )
]

# Model registry for easy access
MODEL_REGISTRY = {model.id: model for model in AVAILABLE_MODELS}

def get_model_by_id(model_id):
    """Get model by ID"""
    return MODEL_REGISTRY.get(model_id)

def get_all_models():
    """Get all available models"""
    return AVAILABLE_MODELS

def get_models_by_provider(provider):
    """Get models by provider"""
    return [model for model in AVAILABLE_MODELS if model.provider == provider]