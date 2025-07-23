#!/usr/bin/env python3
"""
Demo sederhana untuk Jinja2 Template Generator System
Versi tanpa dependencies eksternal untuk demonstrasi
"""

import os
import json
from pathlib import Path

# Simple CSV parser
def load_csv_simple(filename):
    """Simple CSV loader without pandas"""
    try:
        import csv
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = []
            for row in reader:
                # Clean up quoted fields
                cleaned_row = {}
                for key, value in row.items():
                    cleaned_row[key.strip()] = value.strip().strip('"')
                data.append(cleaned_row)
            return data
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return []

# Simple Jinja2-like template processor
def process_template(template_content, data):
    """Simple template processor for demo"""
    # Replace basic variables
    result = template_content
    
    # Handle simple variable substitution
    if isinstance(data, dict):
        for key, value in data.items():
            result = result.replace(f"{{{{ {key} }}}}", str(value))
            result = result.replace(f"{{{{{key}}}}}", str(value))
    
    return result

def create_simple_html(title, items, template_type="blog"):
    """Create simple HTML from data"""
    if template_type == "blog":
        html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <header class="bg-primary text-white py-4">
        <div class="container">
            <h1>{title}</h1>
        </div>
    </header>
    
    <main class="container my-4">
        <div class="row">
"""
        
        for item in items:
            title_item = item.get('title', 'No Title')
            description = item.get('description', 'No Description')
            author = item.get('author', 'Unknown Author')
            date = item.get('date', 'No Date')
            category = item.get('category', 'General')
            image = item.get('image', 'https://via.placeholder.com/400x200')
            
            html += f"""
            <div class="col-lg-4 col-md-6 mb-4">
                <div class="card h-100">
                    <img src="{image}" class="card-img-top" alt="{title_item}" style="height: 200px; object-fit: cover;">
                    <div class="card-body">
                        <span class="badge bg-primary mb-2">{category}</span>
                        <h5 class="card-title">{title_item}</h5>
                        <p class="card-text">{description[:100]}{'...' if len(description) > 100 else ''}</p>
                        <small class="text-muted">By {author} | {date}</small>
                    </div>
                </div>
            </div>
"""
        
        html += """
        </div>
    </main>
    
    <footer class="bg-light py-4 mt-5">
        <div class="container text-center">
            <p class="mb-0 text-muted">Generated with Jinja2 Template System</p>
        </div>
    </footer>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""
        
    elif template_type == "products":
        html = f"""<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        .price-tag {{ font-size: 1.2rem; font-weight: bold; color: #28a745; }}
        .product-card:hover {{ transform: translateY(-5px); transition: all 0.3s; }}
    </style>
</head>
<body>
    <header class="bg-success text-white py-4">
        <div class="container">
            <h1>{title}</h1>
        </div>
    </header>
    
    <main class="container my-4">
        <div class="row">
"""
        
        for item in items:
            title_item = item.get('title', 'Product')
            description = item.get('description', 'No Description')
            price = item.get('price', '0')
            image = item.get('image', 'https://via.placeholder.com/300x300')
            brand = item.get('brand', 'Unknown')
            rating = item.get('rating', '0')
            
            # Format price if it's numeric
            try:
                price_num = float(price)
                price_formatted = f"Rp {price_num:,.0f}"
            except:
                price_formatted = str(price)
            
            # Generate star rating
            stars = ""
            try:
                rating_num = int(float(rating))
                for i in range(5):
                    if i < rating_num:
                        stars += "★"
                    else:
                        stars += "☆"
            except:
                stars = "No Rating"
            
            html += f"""
            <div class="col-xl-3 col-lg-4 col-md-6 mb-4">
                <div class="card product-card h-100">
                    <img src="{image}" class="card-img-top" alt="{title_item}" style="height: 250px; object-fit: cover;">
                    <div class="card-body">
                        <small class="text-muted">{brand}</small>
                        <h6 class="card-title">{title_item}</h6>
                        <p class="card-text small">{description[:80]}{'...' if len(description) > 80 else ''}</p>
                        <div class="mb-2 text-warning">{stars}</div>
                        <div class="price-tag">{price_formatted}</div>
                    </div>
                    <div class="card-footer bg-transparent">
                        <button class="btn btn-success btn-sm w-100">
                            <i class="fas fa-shopping-cart"></i> Beli
                        </button>
                    </div>
                </div>
            </div>
"""
        
        html += """
        </div>
    </main>
    
    <footer class="bg-light py-4 mt-5">
        <div class="container text-center">
            <p class="mb-0 text-muted">Generated with Jinja2 Template System</p>
        </div>
    </footer>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""
    
    return html

def main():
    print("🎨 Jinja2 Template Generator System - Simple Demo")
    print("=" * 55)
    
    # Create output directory
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # 1. Generate blog dari CSV
    print("\n1. Generate Blog dari CSV...")
    try:
        csv_data = load_csv_simple("sample_data/blog_data.csv")
        if csv_data:
            html_content = create_simple_html("Blog Grid - Generated from CSV", csv_data, "blog")
            
            with open("output/blog_from_csv.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            
            print(f"✅ Blog berhasil di-generate dengan {len(csv_data)} artikel")
            print(f"   📁 File: output/blog_from_csv.html")
        else:
            print("❌ Data CSV tidak ditemukan atau kosong")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # 2. Generate product catalog dari JSON
    print("\n2. Generate Product Catalog dari JSON...")
    try:
        with open("sample_data/product_data.json", "r", encoding="utf-8") as f:
            json_data = json.load(f)
        
        if json_data and "items" in json_data:
            title = json_data.get("title", "Product Catalog")
            items = json_data["items"]
            
            html_content = create_simple_html(title, items, "products")
            
            with open("output/products_from_json.html", "w", encoding="utf-8") as f:
                f.write(html_content)
            
            print(f"✅ Product catalog berhasil di-generate dengan {len(items)} produk")
            print(f"   📁 File: output/products_from_json.html")
        else:
            print("❌ Data JSON tidak valid")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # 3. Generate sample testimonials
    print("\n3. Generate Testimonials...")
    try:
        testimonial_data = [
            {
                "title": "Testimoni Customer 1",
                "description": "Layanan yang luar biasa! Tim mereka sangat profesional dan responsif. Hasil kerja melebihi ekspektasi kami.",
                "author": "Budi Santoso",
                "date": "2024-11-15",
                "category": "CEO - Tech Startup",
                "image": "https://via.placeholder.com/400x200/28a745/ffffff?text=Testimonial"
            },
            {
                "title": "Testimoni Customer 2", 
                "description": "Platform mereka sangat user-friendly dan powerful. Customer support juga sangat membantu dalam setiap kendala.",
                "author": "Sari Dewi",
                "date": "2024-11-10",
                "category": "Marketing Manager",
                "image": "https://via.placeholder.com/400x200/17a2b8/ffffff?text=Review"
            },
            {
                "title": "Testimoni Customer 3",
                "description": "ROI yang didapat sangat signifikan. Tim support selalu siap membantu 24/7 dengan response time yang cepat.",
                "author": "Ahmad Rahman",
                "date": "2024-11-05", 
                "category": "CTO - Digital Agency",
                "image": "https://via.placeholder.com/400x200/ffc107/000000?text=5+Stars"
            }
        ]
        
        html_content = create_simple_html("Customer Testimonials", testimonial_data, "blog")
        
        with open("output/testimonials_demo.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print(f"✅ Testimonials berhasil di-generate dengan {len(testimonial_data)} review")
        print(f"   📁 File: output/testimonials_demo.html")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # 4. Create template overview
    print("\n4. Generate Template Overview...")
    try:
        templates_info = [
            {
                "title": "Blog Grid Template",
                "description": "Template untuk menampilkan artikel blog dalam format grid responsif dengan card design",
                "author": "Template System",
                "date": "2024-12-01",
                "category": "Blog Layout",
                "image": "https://via.placeholder.com/400x200/007bff/ffffff?text=Blog+Grid"
            },
            {
                "title": "Product Catalog Template",
                "description": "Template e-commerce untuk showcase produk dengan pricing, rating, dan filter kategori",
                "author": "Template System", 
                "date": "2024-12-01",
                "category": "E-commerce",
                "image": "https://via.placeholder.com/400x200/28a745/ffffff?text=Products"
            },
            {
                "title": "News Magazine Template",
                "description": "Template portal berita dengan featured article, sidebar, dan layout magazine style",
                "author": "Template System",
                "date": "2024-12-01",
                "category": "News Layout",
                "image": "https://via.placeholder.com/400x200/dc3545/ffffff?text=News"
            },
            {
                "title": "Portfolio Gallery Template",
                "description": "Template showcase portfolio dengan filtering, masonry layout, dan modal view",
                "author": "Template System",
                "date": "2024-12-01", 
                "category": "Portfolio",
                "image": "https://via.placeholder.com/400x200/6f42c1/ffffff?text=Portfolio"
            },
            {
                "title": "Event Calendar Template",
                "description": "Template event listing dengan multiple view modes: list, grid, dan calendar view",
                "author": "Template System",
                "date": "2024-12-01",
                "category": "Events",
                "image": "https://via.placeholder.com/400x200/fd7e14/ffffff?text=Calendar"
            },
            {
                "title": "Testimonial Carousel Template",
                "description": "Template untuk menampilkan customer testimonials dengan carousel dan rating system",
                "author": "Template System",
                "date": "2024-12-01",
                "category": "Social Proof",
                "image": "https://via.placeholder.com/400x200/20c997/ffffff?text=Reviews"
            },
            {
                "title": "Pricing Table Template", 
                "description": "Template pricing plans dengan feature comparison dan billing options toggle",
                "author": "Template System",
                "date": "2024-12-01",
                "category": "Pricing",
                "image": "https://via.placeholder.com/400x200/e83e8c/ffffff?text=Pricing"
            },
            {
                "title": "Team Showcase Template",
                "description": "Template untuk menampilkan team members dengan social links dan department filtering",
                "author": "Template System",
                "date": "2024-12-01",
                "category": "About Us",
                "image": "https://via.placeholder.com/400x200/6c757d/ffffff?text=Team"
            }
        ]
        
        html_content = create_simple_html("Jinja2 Template Collection - Available Templates", templates_info, "blog")
        
        with open("output/template_overview.html", "w", encoding="utf-8") as f:
            f.write(html_content)
        
        print(f"✅ Template overview berhasil di-generate dengan {len(templates_info)} template")
        print(f"   📁 File: output/template_overview.html")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    print(f"\n🎉 Demo selesai!")
    print(f"📁 Hasil dapat dilihat di folder 'output/':")
    
    # List generated files
    for file in output_dir.glob("*.html"):
        file_size = file.stat().st_size
        print(f"   📄 {file.name} ({file_size:,} bytes)")
    
    print(f"\n📋 Template Files Tersedia:")
    template_dir = Path("templates")
    if template_dir.exists():
        for i, template in enumerate(template_dir.glob("*.html"), 1):
            print(f"   {i}. {template.name}")
    
    print(f"\n💡 Cara menggunakan:")
    print(f"   1. Buka file HTML di browser untuk melihat hasil")
    print(f"   2. Edit data di sample_data/ untuk konten custom")
    print(f"   3. Modifikasi template di templates/ untuk design custom")
    print(f"   4. Gunakan template_generator.py untuk integrasi penuh")

if __name__ == "__main__":
    main()