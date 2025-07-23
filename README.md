# AI Bulk Content Generator 🚀

Platform AI Generator modern dengan fokus pada **Bulk Content Generation** untuk WordPress. Generate ratusan halaman konten berkualitas dari data CSV menggunakan multiple AI models.

![AI Generator](https://img.shields.io/badge/AI-Generator-purple?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3+-green?style=for-the-badge&logo=flask)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=for-the-badge)

## ✨ Fitur Utama

### 🎯 Bulk Content Generator
- **CSV Upload**: Upload file CSV dengan data bisnis/produk
- **7+ Template HTML**: Template profesional untuk berbagai industri
- **WordPress Ready**: Output siap upload ke WordPress
- **Multiple Formats**: HTML, WordPress, Markdown, JSON
- **AI Enhancement**: Tingkatkan kualitas konten dengan AI
- **ZIP Download**: Download semua file dalam satu paket

### 🤖 AI Models Terintegrasi
- **Google Gemini Pro & Flash**: Model terbaru Google dengan context 1M+ tokens
- **Groq Llama 3.1 70B**: Super fast inference
- **OpenAI GPT-3.5 Turbo**: Reliable dan powerful
- **HuggingFace Models**: GPT-2, FLAN-T5 gratis
- **Cohere Command R+**: Advanced reasoning

### 📝 Content Templates
- **Business Landing Pages**: Professional business presentations
- **Product Showcases**: E-commerce product pages
- **Blog Articles**: SEO-optimized blog content
- **Restaurant Menus**: Appetizing menu displays
- **Real Estate Listings**: Property showcases
- **Event Landing Pages**: Event promotion pages
- **Portfolio Showcases**: Creative work presentations

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation

1. **Clone Repository**
```bash
git clone https://github.com/your-username/ai-bulk-generator.git
cd ai-bulk-generator
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Environment Setup**
```bash
cp .env.example .env
# Edit .env file dengan API keys (opsional)
```

4. **Run Application**
```bash
python run.py
```

5. **Access Application**
```
http://localhost:5000
```

## 📊 Bulk Generation Workflow

### Step 1: Prepare CSV Data
Create CSV file dengan field yang sesuai template:

```csv
business_name,tagline,description,cta_text,cta_link,hero_image,...
"Tech Startup","Innovation First","Leading technology solutions","Get Started","/contact","hero1.jpg",...
"Local Cafe","Fresh & Tasty","Best coffee in town","Order Now","/menu","hero2.jpg",...
```

### Step 2: Upload & Validate
- Upload CSV file via drag & drop
- System validates required fields
- Preview data untuk memastikan format benar

### Step 3: Configure Generation
- Pilih AI model (Gemini Flash recommended)
- Pilih output format (WordPress untuk blog)
- Enable AI enhancement untuk kualitas lebih baik
- Input API key atau gunakan demo mode

### Step 4: Generate & Download
- Generate ratusan file secara batch
- Download ZIP berisi semua file
- Upload langsung ke WordPress

## 🏗️ Template Structure

### Business Landing Template
```html
<!-- Hero Section dengan dynamic content -->
<section class="hero-section">
    <h1>{business_name}</h1>
    <p>{tagline}</p>
    <p>{description}</p>
    <a href="{cta_link}">{cta_text}</a>
</section>

<!-- Services Section -->
<section class="services-section">
    <!-- Dynamic service cards -->
</section>
```

**Required Fields**: 21 fields
- `business_name`, `tagline`, `description`
- `cta_text`, `cta_link`, `hero_image`
- `service1_title`, `service1_description`, `service1_image`
- Dan lainnya...

### E-commerce Product Template
```html
<!-- Product showcase dengan specifications -->
<div class="product-showcase">
    <div class="product-gallery">
        <img src="{product_image}" alt="{product_name}" />
    </div>
    <div class="product-info">
        <h1>{product_name}</h1>
        <p class="price">{price}</p>
        <div class="rating">{rating} ⭐</div>
    </div>
</div>
```

**Required Fields**: 24 fields
- `product_name`, `price`, `rating`, `description`
- `product_image`, `image2`, `image3`, `image4`
- `feature1`, `feature2`, `feature3`, `feature4`
- Dan lainnya...

## 🔧 API Configuration

### Environment Variables
```bash
# AI API Keys (Optional)
GROQ_API_KEY=gsk_your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=sk_your_openai_api_key_here
HUGGINGFACE_API_KEY=hf_your_token_here
COHERE_API_KEY=your_cohere_api_key_here

# Flask Settings
DEBUG=True
SECRET_KEY=your-secret-key-here
```

### API Endpoints
```bash
# Bulk Generation
POST /api/bulk/validate-csv    # Validate CSV data
POST /api/bulk/generate        # Generate bulk content
POST /api/bulk/download        # Download ZIP package

# Single Generation
POST /api/generate             # Single AI generation
GET  /api/models              # Available AI models
GET  /api/templates/search    # Search templates
```

## 💡 Use Cases

### 1. E-commerce Bulk Pages
Generate product pages untuk ratusan produk:
```csv
product_name,price,description,image_url,...
"Smartphone X","$299","Latest smartphone","phone1.jpg",...
"Laptop Pro","$899","Professional laptop","laptop1.jpg",...
```

### 2. Real Estate Listings
Generate property listing pages:
```csv
property_title,price,bedrooms,bathrooms,address,...
"Modern Villa","$450,000","4","3","123 Oak Street",...
"City Apartment","$200,000","2","1","456 Main Ave",...
```

### 3. Restaurant Menus
Generate menu pages untuk multiple outlets:
```csv
restaurant_name,cuisine_type,appetizer1_name,main1_name,...
"Pizza Palace","Italian","Bruschetta","Margherita Pizza",...
"Sushi Master","Japanese","Edamame","Salmon Sashimi",...
```

### 4. Business Directories
Generate landing pages untuk multiple businesses:
```csv
business_name,industry,services,contact_info,...
"Tech Solutions","IT","Web Development","tech@email.com",...
"Design Studio","Creative","Branding","design@email.com",...
```

## 🎨 Output Formats

### WordPress Format
```html
<!-- wp:html -->
<div class="business-landing">
    <!-- Template content -->
</div>
<!-- /wp:html -->

<!-- wp:html -->
<style>
/* Template CSS */
</style>
<!-- /wp:html -->
```

### HTML Format
```html
<!DOCTYPE html>
<html>
<head>
    <title>Generated Content</title>
    <style>/* Template CSS */</style>
</head>
<body>
    <!-- Template content -->
    <script>/* Template JS */</script>
</body>
</html>
```

### Markdown Format
```markdown
# Business Name

**Tagline**: Innovation First

**Description**: Leading technology solutions...

## Services
- Service 1: Description
- Service 2: Description

[Get Started](/contact)
```

### JSON Format
```json
{
  "content": {
    "html": "<!-- Template HTML -->",
    "css": "/* Template CSS */",
    "javascript": "/* Template JS */"
  },
  "data": {
    "business_name": "Tech Startup",
    "tagline": "Innovation First"
  },
  "meta": {
    "generated_at": "2024-01-01T00:00:00",
    "format": "json"
  }
}
```

## 🔒 Security & Best Practices

### API Key Security
- Gunakan environment variables untuk API keys
- Jangan commit API keys ke version control
- Rotasi API keys secara berkala

### Input Validation
- CSV data divalidasi sebelum processing
- XSS protection pada user input
- File upload size limits

### Rate Limiting
- Respect AI provider rate limits
- Implement exponential backoff
- Queue system untuk bulk processing

## 🚀 Deployment

### Local Development
```bash
python run.py
# Access: http://localhost:5000
```

### Production with Gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app"]
```

```bash
docker build -t ai-generator .
docker run -p 5000:5000 ai-generator
```

### Environment Configuration
```bash
# Production settings
DEBUG=False
SECRET_KEY=your-production-secret-key
CORS_ORIGINS=yourdomain.com
```

## 📈 Performance Optimization

### Bulk Processing
- Parallel processing untuk multiple records
- Streaming responses untuk large datasets
- Progress tracking untuk user feedback

### Caching
- Template caching untuk faster rendering
- AI response caching untuk repeated content
- Static asset optimization

### Monitoring
- Generation success/failure rates
- API response times
- Error tracking dan logging

## 🤝 Contributing

### Development Setup
1. Fork repository
2. Create feature branch
3. Install development dependencies
4. Make changes
5. Test thoroughly
6. Submit pull request

### Adding New Templates
1. Create template in `app/models/content_templates.py`
2. Define required fields
3. Write HTML template dengan placeholders
4. Add CSS styling
5. Test dengan sample CSV data

### Adding New AI Models
1. Update `app/models/ai_models.py`
2. Implement API client in `app/utils/ai_client.py`
3. Add API key mapping
4. Test integration
5. Update documentation

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🆘 Support

### Common Issues

**Q: CSV validation fails**
A: Pastikan CSV memiliki semua required fields untuk template yang dipilih

**Q: AI generation returns demo response**
A: Set API key yang valid di environment variables atau input form

**Q: Download ZIP empty**
A: Check generation results - pastikan ada content yang berhasil di-generate

**Q: WordPress format tidak ter-import**
A: Gunakan WordPress import plugin atau copy-paste content manual

### Get Help
- 📧 Email: support@your-domain.com
- 💬 GitHub Issues: [Create Issue](https://github.com/your-username/ai-bulk-generator/issues)
- 📖 Documentation: [Wiki](https://github.com/your-username/ai-bulk-generator/wiki)

## 🎯 Roadmap

### Version 2.0
- [ ] Advanced template editor
- [ ] Custom field mapping
- [ ] Batch API key management
- [ ] Advanced AI parameters
- [ ] Template marketplace

### Version 2.1
- [ ] WordPress plugin integration
- [ ] Automatic content posting
- [ ] SEO optimization tools
- [ ] Analytics dashboard
- [ ] Team collaboration features

---

**Made with ❤️ for content creators and WordPress developers**

*Generate smarter, not harder with AI Bulk Content Generator*