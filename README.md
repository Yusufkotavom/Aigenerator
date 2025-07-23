# 🤖 AI Generator - Multi Model Platform

**Platform AI Generator modern dengan dukungan berbagai model AI gratis** menggunakan Python Flask, Jinja2 templates, dan Tailwind CSS.

![AI Generator](https://via.placeholder.com/800x400/8b5cf6/ffffff?text=AI+Generator+Platform)

## ✨ Fitur Utama

- 🎯 **Multi-Model Support**: Groq, HuggingFace, OpenAI, Cohere
- 🆓 **Free Tier Focus**: Semua model mendukung tier gratis
- 🎨 **Modern UI**: Glassmorphism dengan Tailwind CSS
- 📱 **Responsive Design**: Optimal di desktop dan mobile
- 🔧 **Template System**: Jinja2 modular templates
- 📋 **Template Prompts**: 7+ prompt siap pakai
- 💾 **Session Storage**: History tersimpan dalam session
- 🚀 **Real-time Response**: Interface yang responsif

## 🏗️ Arsitektur Project

```
ai-generator/
├── app/                          # Main Flask application
│   ├── __init__.py              # App factory
│   ├── models/                  # Data models
│   │   ├── ai_models.py         # AI model configurations
│   │   └── prompts.py           # Prompt templates
│   ├── views/                   # Route handlers
│   │   ├── main.py              # Main routes
│   │   └── api.py               # API endpoints
│   ├── utils/                   # Utilities
│   │   └── ai_client.py         # AI API client
│   ├── templates/               # Jinja2 templates
│   │   ├── layouts/             # Base layouts
│   │   ├── components/          # Reusable components
│   │   ├── index.html           # Home page
│   │   ├── generator.html       # Main generator
│   │   └── templates.html       # Template library
│   └── static/                  # Static assets
│       ├── css/style.css        # Custom styles
│       └── js/app.js            # JavaScript utilities
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment template
└── run.py                      # Application entry point
```

## 🚀 Model AI yang Didukung

| Provider | Model | Type | Free Tier | Setup |
|----------|-------|------|-----------|-------|
| **Groq** | Llama 3.1 70B | Chat | ✅ 30 req/min | [Get key](https://console.groq.com/) |
| **HuggingFace** | GPT-2, FLAN-T5 | Text Gen | ✅ 1000 req/month | [Get token](https://huggingface.co/settings/tokens) |
| **OpenAI** | GPT-3.5 Turbo | Chat | ✅ $5 trial | [Get key](https://platform.openai.com/api-keys) |
| **Cohere** | Command | Chat | ✅ Free trial | [Get key](https://dashboard.cohere.ai/) |

## 📋 Prerequisites

### Python 3.8+
```bash
python --version  # 3.8 atau lebih baru
pip --version     # package installer
```

## 🛠️ Quick Start

### 1. Clone & Setup
```bash
git clone https://github.com/your-username/ai-generator.git
cd ai-generator

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit .env file (optional - API keys)
nano .env
```

### 3. Run Application
```bash
# Development server
python run.py

# Production dengan Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

### 4. Open Browser
```
http://localhost:5000
```

## 🔑 Setup API Keys (Optional)

### Metode 1: Environment Variables
```bash
export GROQ_API_KEY="gsk_your_groq_key"
export HUGGINGFACE_API_KEY="hf_your_token"
export OPENAI_API_KEY="sk_your_openai_key"
```

### Metode 2: .env File
```env
GROQ_API_KEY=gsk_your_groq_key_here
HUGGINGFACE_API_KEY=hf_your_token_here
OPENAI_API_KEY=sk_your_openai_key_here
```

### Metode 3: Web Interface
- Buka halaman Generator
- Klik "Show API Settings"
- Masukkan API key secara manual

## 💡 Cara Penggunaan

### 1. Pilih Model AI
- Buka halaman Generator
- Pilih model dari card yang tersedia
- Info model akan tampil di sidebar

### 2. Gunakan Template atau Custom Prompt
```python
# Template examples:
- Creative Writing: Cerita pendek kreatif
- Code Helper: Bantuan programming
- Business Analysis: Analisis ide bisnis
- Problem Solving: Pemecahan masalah sistematis
```

### 3. Atur Parameter
- **Temperature**: 0.0 (conservative) - 1.0 (creative)
- **Max Tokens**: 50 - 2000 (panjang response)
- **Top P**: 0.0 (focused) - 1.0 (diverse)

### 4. Generate & Export
- Klik "Generate AI Response"
- Copy hasil ke clipboard
- View generation history

## 🎨 Template System

### Struktur Template Jinja2
```jinja2
{% extends "layouts/base.html" %}

{% block title %}Page Title{% endblock %}

{% block content %}
<!-- Page content -->
{% include 'components/navbar.html' %}
{% endblock %}

{% block scripts %}
<script>
// Page-specific JavaScript
</script>
{% endblock %}
```

### Komponen yang Tersedia
- `layouts/base.html` - Base layout
- `components/navbar.html` - Navigation bar
- `components/footer.html` - Footer
- `components/flash_messages.html` - Notifications

## 🔧 Development

### Folder Structure Breakdown
```
app/
├── models/          # Data structures & configurations
├── views/           # Route handlers (like controllers)
├── utils/           # Helper functions & API clients
├── templates/       # Jinja2 HTML templates
│   ├── layouts/     # Base templates
│   └── components/  # Reusable template parts
└── static/          # CSS, JS, images
```

### Adding New AI Model
```python
# app/models/ai_models.py
new_model = AIModel(
    model_id='provider-model',
    name='Model Name',
    provider='Provider',
    description='Model description',
    model_type='Chat Completion',
    endpoint='https://api.provider.com/v1/chat',
    model_name='model-name',
    icon='fas fa-icon',
    color='bg-color-500'
)

AVAILABLE_MODELS.append(new_model)
```

### Adding New Template
```python
# app/models/prompts.py
new_template = PromptTemplate(
    template_id='unique-id',
    name='Template Name',
    description='Template description',
    prompt='Your prompt template here...',
    category='Category',
    tags=['tag1', 'tag2']
)

PROMPT_TEMPLATES.append(new_template)
```

## 🐳 Docker Deployment

### Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
```

### Docker Compose
```yaml
version: '3.8'
services:
  ai-generator:
    build: .
    ports:
      - "5000:5000"
    environment:
      - DEBUG=False
      - SECRET_KEY=your-secret-key
    volumes:
      - .:/app
```

## 🚀 Production Deployment

### Using Gunicorn
```bash
# Install Gunicorn
pip install gunicorn

# Run with multiple workers
gunicorn -w 4 -b 0.0.0.0:5000 run:app

# With process management
gunicorn -w 4 -b 0.0.0.0:5000 --daemon --pid /var/run/gunicorn.pid run:app
```

### Nginx Configuration
```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /static {
        alias /path/to/your/app/static;
    }
}
```

## 🛡️ Security & Best Practices

### Environment Variables
```bash
# Never commit these to version control
SECRET_KEY=your-very-secret-key-here
DEBUG=False
GROQ_API_KEY=your-api-key
```

### Rate Limiting
- Implement rate limiting for API endpoints
- Use Redis for distributed rate limiting
- Monitor API usage per provider

### CORS & Security Headers
```python
# Already configured in app/__init__.py
CORS(app)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
```

## 🚨 Troubleshooting

### Common Issues

**1. ModuleNotFoundError**
```bash
# Ensure virtual environment is activated
source venv/bin/activate
pip install -r requirements.txt
```

**2. Template Not Found**
```bash
# Check template paths in app/views/
# Ensure templates are in app/templates/
```

**3. API Key Errors**
```bash
# Check environment variables
echo $GROQ_API_KEY

# Or use web interface for manual entry
```

**4. CORS Issues**
```python
# Already handled in app/__init__.py
# Ensure CORS is properly configured
```

### Debug Mode
```bash
export DEBUG=True
python run.py
```

## 📊 Performance Tips

### Optimization
- Use Redis for session storage in production
- Implement request caching for API responses
- Use CDN for static assets
- Enable gzip compression

### Monitoring
- Log API response times
- Monitor error rates
- Track model usage statistics
- Set up health checks

## 🤝 Contributing

### Development Workflow
1. Fork repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Make changes with proper tests
4. Commit: `git commit -m 'Add amazing feature'`
5. Push: `git push origin feature/amazing-feature`
6. Create Pull Request

### Code Style
- Follow PEP 8 for Python
- Use Black for code formatting
- Add docstrings for functions
- Include type hints where possible

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Jinja2](https://jinja.palletsprojects.com/) - Template engine
- [Tailwind CSS](https://tailwindcss.com/) - Styling
- [Alpine.js](https://alpinejs.dev/) - JavaScript framework
- [Groq](https://groq.com/) - Fast AI inference
- [HuggingFace](https://huggingface.co/) - AI model hub

## 📞 Support

- 🐛 Bug reports: [Issues](https://github.com/your-username/ai-generator/issues)
- 💬 Discussions: [Discussions](https://github.com/your-username/ai-generator/discussions)
- 📧 Email: support@your-domain.com

---

**Made with ❤️ using Python Flask + Jinja2**

⭐ **Star this repo if it helps you!**