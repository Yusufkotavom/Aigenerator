# 🎨 Jinja2 Template Generator System

Sistem template generator yang modular dan fleksibel untuk membuat berbagai jenis konten HTML dengan input dari CSV, JSON, atau AI. Fokus utama pada template yang beragam dan integrasi input yang mudah.

## ✨ Fitur Utama

- **Multiple Input Sources**: Support untuk CSV, JSON, dan AI-generated data
- **Modular Templates**: Template yang dapat digunakan kembali dan dikustomisasi
- **Rich Components**: Komponen UI yang kaya dan responsif
- **Batch Processing**: Generate multiple content sekaligus
- **Safe Handling**: Menangani gambar dan URL yang tidak aktif
- **Bootstrap UI**: Interface modern dengan Bootstrap 5

## 📁 Struktur Proyek

```
.
├── template_generator.py          # Main generator class
├── templates/                     # Template files
│   ├── base.html                 # Base template
│   ├── components/               # Reusable components
│   │   ├── card.html            # Card component
│   │   └── list.html            # List component
│   ├── blog_grid.html           # Blog grid template
│   ├── product_catalog.html     # Product catalog template
│   ├── news_magazine.html       # News magazine template
│   ├── portfolio_gallery.html   # Portfolio gallery template
│   ├── event_calendar.html      # Event calendar template
│   ├── testimonial_carousel.html # Testimonial carousel
│   ├── pricing_table.html       # Pricing table template
│   └── team_showcase.html       # Team showcase template
├── sample_data/                  # Sample data files
│   ├── blog_data.csv            # Sample CSV data
│   ├── product_data.json        # Sample JSON data
│   └── ai_testimonial_data.py   # Sample AI data
├── output/                       # Generated content
├── requirements.txt              # Python dependencies
└── example_usage.py             # Usage examples
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Basic Usage

```python
from template_generator import TemplateGenerator

# Initialize generator
generator = TemplateGenerator()

# Generate dari CSV
csv_data = generator.load_csv_data("sample_data/blog_data.csv")
generator.generate_content("blog_grid.html", csv_data, "output/blog.html")

# Generate dari JSON  
json_data = generator.load_json_data("sample_data/product_data.json")
generator.generate_content("product_catalog.html", json_data, "output/products.html")

# Generate dari AI data
ai_data = {"title": "AI Content", "items": [...]}
processed_data = generator.load_ai_data(ai_data)
generator.generate_content("testimonial_carousel.html", processed_data, "output/testimonials.html")
```

### 3. Run Example

```bash
python example_usage.py
```

## 📊 Template Showcase

### 1. Blog Grid Template
**File**: `templates/blog_grid.html`
**Input**: CSV/JSON dengan kolom: title, description, author, date, category, image, url, tags
**Use Case**: Blog, artikel, news feeds

### 2. Product Catalog Template  
**File**: `templates/product_catalog.html`
**Input**: JSON dengan product data, pricing, ratings
**Use Case**: E-commerce, katalog produk, marketplace

### 3. News Magazine Template
**File**: `templates/news_magazine.html`  
**Input**: News articles dengan featured content, sidebar
**Use Case**: Portal berita, magazine online

### 4. Portfolio Gallery Template
**File**: `templates/portfolio_gallery.html`
**Input**: Portfolio items dengan filtering, modal view
**Use Case**: Portfolio personal, showcase projects

### 5. Event Calendar Template
**File**: `templates/event_calendar.html`
**Input**: Event data dengan multiple view modes
**Use Case**: Event listing, calendar, schedules

### 6. Testimonial Carousel Template
**File**: `templates/testimonial_carousel.html`
**Input**: Customer reviews dengan ratings, stats
**Use Case**: Social proof, customer testimonials

### 7. Pricing Table Template
**File**: `templates/pricing_table.html`
**Input**: Pricing plans dengan feature comparison
**Use Case**: SaaS pricing, subscription plans

### 8. Team Showcase Template
**File**: `templates/team_showcase.html`
**Input**: Team member data dengan social links
**Use Case**: About us, team pages, company profiles

## 🔧 Kustomisasi Template

### Membuat Template Baru

1. Extend dari base template:
```html
{% extends "base.html" %}
{% from "components/card.html" import render_card %}
```

2. Override blocks yang diperlukan:
```html
{% block title %}Custom Title{% endblock %}
{% block content %}
<!-- Your content here -->
{% endblock %}
```

### Menggunakan Components

```html
<!-- Card component -->
{{ render_card(item, variant='hover', show_image=true) }}

<!-- List component -->
{{ render_list(items, style='cards', columns=3) }}
```

## 📝 Data Format Examples

### CSV Format (Blog)
```csv
title,description,author,date,category,image,url,tags
"Post Title","Description text","Author Name","2024-12-01","Tech","image.jpg","#","tag1,tag2"
```

### JSON Format (Products)
```json
{
  "title": "Product Catalog",
  "items": [
    {
      "title": "Product Name",
      "price": 100000,
      "image": "product.jpg",
      "rating": 5,
      "description": "Product description"
    }
  ]
}
```

### AI Data Format (Python Dict)
```python
ai_data = {
    "title": "Generated Content",
    "items": [
        {
            "title": "AI Generated Title",
            "content": "AI generated content...",
            "category": "AI"
        }
    ]
}
```

## 🎨 Custom Filters

Template system menyediakan custom filters:

- `markdown`: Convert markdown to HTML
- `truncate_words(n)`: Truncate text to n words  
- `capitalize_words`: Capitalize each word
- `safe_url`: Ensure URL safety

Usage:
```html
{{ content | markdown | safe }}
{{ description | truncate_words(50) }}
{{ url | safe_url }}
```

## 🔒 Safety Features

- **URL Validation**: Automatic https:// prefix untuk URLs
- **Image Fallback**: Placeholder untuk gambar yang gagal load
- **AI Data Cleaning**: Membersihkan artifacts dari AI-generated content
- **Safe Content**: XSS protection dengan Jinja2 auto-escaping

## 📦 Batch Processing

Generate multiple content dengan satu perintah:

```python
data_sources = [
    {"type": "csv", "path": "data.csv", "output": "result1.html"},
    {"type": "json", "path": "data.json", "output": "result2.html"},
    {"type": "ai", "data": ai_data, "output": "result3.html"}
]

generator.batch_generate("template.html", data_sources, "output_dir")
```

## 🎯 Use Cases

1. **Content Marketing**: Generate blog posts, articles, landing pages
2. **E-commerce**: Product catalogs, pricing pages, testimonials  
3. **Corporate**: Team pages, about us, company profiles
4. **Events**: Calendar, schedules, conference websites
5. **Portfolio**: Personal websites, agency showcases
6. **News**: Magazine layouts, news portals, content aggregation

## 🚀 Advanced Usage

### Custom Template Variables

```python
# Tambah variable custom ke template context
custom_data = {
    "site_name": "My Website",
    "analytics_id": "GA-XXXXX",
    "social_media": {
        "facebook": "https://facebook.com/mypage",
        "twitter": "https://twitter.com/myhandle"
    }
}

generator.generate_content("template.html", custom_data, "output.html")
```

### Template Inheritance

```html
<!-- child_template.html -->
{% extends "base.html" %}

{% block extra_css %}
<style>
/* Custom styles */
</style>
{% endblock %}

{% block content %}
<!-- Custom content -->
{% endblock %}
```

## 🤝 Contributing

1. Fork repository
2. Buat template baru di folder `templates/`
3. Tambah sample data di `sample_data/`
4. Update README dengan contoh penggunaan
5. Submit pull request

## 📄 License

MIT License - silakan gunakan untuk project komersial dan personal.

## 🆘 Support

Jika ada pertanyaan atau butuh bantuan:

1. Baca dokumentasi ini dengan lengkap
2. Lihat contoh di `example_usage.py`
3. Check sample data di folder `sample_data/`
4. Buat issue untuk bug report atau feature request

---

**Happy Template Generating! 🎨✨**