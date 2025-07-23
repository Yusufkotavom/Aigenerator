"""Content Templates for WordPress Bulk Generation"""

class ContentTemplate:
    """Content template data structure for WordPress generation"""
    
    def __init__(self, template_id, name, description, category, purpose, 
                 html_template, css_styles=None, js_scripts=None, 
                 fields=None, tags=None, industry=None):
        self.id = template_id
        self.name = name
        self.description = description
        self.category = category
        self.purpose = purpose
        self.html_template = html_template
        self.css_styles = css_styles or ""
        self.js_scripts = js_scripts or ""
        self.fields = fields or []  # Required CSV fields
        self.tags = tags or []
        self.industry = industry or "General"
    
    def to_dict(self):
        """Convert template to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'purpose': self.purpose,
            'html_template': self.html_template,
            'css_styles': self.css_styles,
            'js_scripts': self.js_scripts,
            'fields': self.fields,
            'tags': self.tags,
            'industry': self.industry
        }

# Content Templates Collection
CONTENT_TEMPLATES = [
    
    # BUSINESS TEMPLATES
    ContentTemplate(
        template_id='business-landing',
        name='Business Landing Page',
        description='Professional business landing page with hero section, services, and CTA',
        category='Business',
        purpose='Lead generation and business presentation',
        html_template='''
<div class="business-landing">
    <!-- Hero Section -->
    <section class="hero-section">
        <div class="container">
            <div class="hero-content">
                <h1 class="hero-title">{business_name}</h1>
                <p class="hero-subtitle">{tagline}</p>
                <p class="hero-description">{description}</p>
                <div class="hero-cta">
                    <a href="{cta_link}" class="btn-primary">{cta_text}</a>
                    <a href="{secondary_link}" class="btn-secondary">{secondary_text}</a>
                </div>
            </div>
            <div class="hero-image">
                <img src="{hero_image}" alt="{business_name}" />
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section class="services-section">
        <div class="container">
            <h2>Our Services</h2>
            <div class="services-grid">
                <div class="service-card">
                    <img src="{service1_image}" alt="{service1_title}" />
                    <h3>{service1_title}</h3>
                    <p>{service1_description}</p>
                </div>
                <div class="service-card">
                    <img src="{service2_image}" alt="{service2_title}" />
                    <h3>{service2_title}</h3>
                    <p>{service2_description}</p>
                </div>
                <div class="service-card">
                    <img src="{service3_image}" alt="{service3_title}" />
                    <h3>{service3_title}</h3>
                    <p>{service3_description}</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact-section">
        <div class="container">
            <h2>Get In Touch</h2>
            <div class="contact-info">
                <p><strong>Phone:</strong> {phone}</p>
                <p><strong>Email:</strong> {email}</p>
                <p><strong>Address:</strong> {address}</p>
            </div>
        </div>
    </section>
</div>
        ''',
        css_styles='''
.business-landing { font-family: 'Arial', sans-serif; }
.hero-section { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 80px 0; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.hero-content { text-align: center; }
.hero-title { font-size: 3rem; font-weight: bold; margin-bottom: 1rem; }
.hero-subtitle { font-size: 1.5rem; margin-bottom: 1rem; }
.hero-description { font-size: 1.1rem; margin-bottom: 2rem; }
.btn-primary { background: #ff6b6b; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; margin-right: 10px; }
.btn-secondary { background: transparent; color: white; padding: 15px 30px; text-decoration: none; border: 2px solid white; border-radius: 5px; }
.services-section { padding: 80px 0; }
.services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
.service-card { text-align: center; padding: 30px; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
.contact-section { background: #f8f9fa; padding: 80px 0; }
        ''',
        fields=['business_name', 'tagline', 'description', 'cta_text', 'cta_link', 'secondary_text', 'secondary_link', 'hero_image', 'service1_title', 'service1_description', 'service1_image', 'service2_title', 'service2_description', 'service2_image', 'service3_title', 'service3_description', 'service3_image', 'phone', 'email', 'address'],
        tags=['business', 'landing', 'services', 'professional'],
        industry='Business Services'
    ),

    ContentTemplate(
        template_id='product-showcase',
        name='Product Showcase',
        description='Elegant product showcase with features, specifications, and purchase options',
        category='E-commerce',
        purpose='Product marketing and sales conversion',
        html_template='''
<div class="product-showcase">
    <!-- Product Hero -->
    <section class="product-hero">
        <div class="container">
            <div class="product-gallery">
                <img src="{product_image}" alt="{product_name}" class="main-image" />
                <div class="thumbnail-gallery">
                    <img src="{image2}" alt="{product_name}" />
                    <img src="{image3}" alt="{product_name}" />
                    <img src="{image4}" alt="{product_name}" />
                </div>
            </div>
            <div class="product-info">
                <h1 class="product-title">{product_name}</h1>
                <p class="product-price">{price}</p>
                <div class="product-rating">
                    <span class="rating">{rating} ⭐</span>
                    <span class="reviews">({review_count} reviews)</span>
                </div>
                <p class="product-description">{description}</p>
                
                <div class="product-features">
                    <h3>Key Features:</h3>
                    <ul>
                        <li>{feature1}</li>
                        <li>{feature2}</li>
                        <li>{feature3}</li>
                        <li>{feature4}</li>
                    </ul>
                </div>

                <div class="purchase-section">
                    <button class="btn-buy">{buy_button_text}</button>
                    <button class="btn-cart">{add_to_cart_text}</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Specifications -->
    <section class="specifications">
        <div class="container">
            <h2>Specifications</h2>
            <div class="spec-grid">
                <div class="spec-item">
                    <strong>Dimensions:</strong> {dimensions}
                </div>
                <div class="spec-item">
                    <strong>Weight:</strong> {weight}
                </div>
                <div class="spec-item">
                    <strong>Material:</strong> {material}
                </div>
                <div class="spec-item">
                    <strong>Warranty:</strong> {warranty}
                </div>
            </div>
        </div>
    </section>

    <!-- Reviews Section -->
    <section class="reviews-section">
        <div class="container">
            <h2>Customer Reviews</h2>
            <div class="review-card">
                <div class="reviewer-info">
                    <img src="{reviewer1_avatar}" alt="{reviewer1_name}" />
                    <div>
                        <h4>{reviewer1_name}</h4>
                        <span class="review-rating">{reviewer1_rating} ⭐</span>
                    </div>
                </div>
                <p>"{reviewer1_comment}"</p>
            </div>
        </div>
    </section>
</div>
        ''',
        css_styles='''
.product-showcase { font-family: 'Arial', sans-serif; }
.product-hero { padding: 60px 0; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; gap: 40px; }
.product-gallery { flex: 1; }
.main-image { width: 100%; border-radius: 10px; }
.thumbnail-gallery { display: flex; gap: 10px; margin-top: 15px; }
.thumbnail-gallery img { width: 80px; height: 80px; object-fit: cover; border-radius: 5px; cursor: pointer; }
.product-info { flex: 1; }
.product-title { font-size: 2.5rem; margin-bottom: 1rem; }
.product-price { font-size: 2rem; color: #e74c3c; font-weight: bold; margin-bottom: 1rem; }
.product-rating { margin-bottom: 1rem; }
.product-features ul { list-style: none; padding: 0; }
.product-features li { padding: 5px 0; position: relative; padding-left: 20px; }
.product-features li::before { content: "✓"; color: #27ae60; position: absolute; left: 0; }
.btn-buy { background: #e74c3c; color: white; padding: 15px 30px; border: none; border-radius: 5px; margin-right: 10px; font-size: 1.1rem; cursor: pointer; }
.btn-cart { background: #3498db; color: white; padding: 15px 30px; border: none; border-radius: 5px; font-size: 1.1rem; cursor: pointer; }
.specifications { background: #f8f9fa; padding: 60px 0; }
.spec-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; }
.spec-item { background: white; padding: 20px; border-radius: 8px; }
.reviews-section { padding: 60px 0; }
.review-card { background: #f8f9fa; padding: 30px; border-radius: 10px; margin-bottom: 20px; }
.reviewer-info { display: flex; align-items: center; gap: 15px; margin-bottom: 15px; }
.reviewer-info img { width: 50px; height: 50px; border-radius: 50%; }
        ''',
        fields=['product_name', 'price', 'rating', 'review_count', 'description', 'product_image', 'image2', 'image3', 'image4', 'feature1', 'feature2', 'feature3', 'feature4', 'buy_button_text', 'add_to_cart_text', 'dimensions', 'weight', 'material', 'warranty', 'reviewer1_name', 'reviewer1_rating', 'reviewer1_comment', 'reviewer1_avatar'],
        tags=['product', 'ecommerce', 'showcase', 'sales'],
        industry='E-commerce'
    ),

    ContentTemplate(
        template_id='blog-article',
        name='Blog Article Layout',
        description='SEO-optimized blog article template with author info and related posts',
        category='Content',
        purpose='Blog content and SEO optimization',
        html_template='''
<article class="blog-article">
    <!-- Article Header -->
    <header class="article-header">
        <div class="container">
            <div class="breadcrumb">
                <a href="{home_url}">Home</a> > 
                <a href="{category_url}">{category}</a> > 
                <span>{title}</span>
            </div>
            <h1 class="article-title">{title}</h1>
            <div class="article-meta">
                <img src="{author_avatar}" alt="{author_name}" class="author-avatar" />
                <div class="meta-info">
                    <span class="author">By <a href="{author_url}">{author_name}</a></span>
                    <span class="date">{publish_date}</span>
                    <span class="read-time">{read_time} min read</span>
                </div>
            </div>
            <img src="{featured_image}" alt="{title}" class="featured-image" />
        </div>
    </header>

    <!-- Article Content -->
    <div class="article-content">
        <div class="container">
            <div class="content-wrapper">
                <div class="main-content">
                    <!-- Introduction -->
                    <div class="article-intro">
                        <p class="lead">{introduction}</p>
                    </div>

                    <!-- Main Content Sections -->
                    <section class="content-section">
                        <h2>{section1_title}</h2>
                        <p>{section1_content}</p>
                        <img src="{section1_image}" alt="{section1_title}" class="content-image" />
                    </section>

                    <section class="content-section">
                        <h2>{section2_title}</h2>
                        <p>{section2_content}</p>
                        
                        <!-- Quote/Highlight -->
                        <blockquote class="highlight-quote">
                            <p>"{quote}"</p>
                            <cite>— {quote_author}</cite>
                        </blockquote>
                    </section>

                    <section class="content-section">
                        <h2>{section3_title}</h2>
                        <p>{section3_content}</p>
                        
                        <!-- Key Points List -->
                        <div class="key-points">
                            <h3>Key Takeaways:</h3>
                            <ul>
                                <li>{takeaway1}</li>
                                <li>{takeaway2}</li>
                                <li>{takeaway3}</li>
                                <li>{takeaway4}</li>
                            </ul>
                        </div>
                    </section>

                    <!-- Conclusion -->
                    <section class="conclusion">
                        <h2>Conclusion</h2>
                        <p>{conclusion}</p>
                    </section>

                    <!-- Call to Action -->
                    <div class="article-cta">
                        <h3>{cta_title}</h3>
                        <p>{cta_description}</p>
                        <a href="{cta_link}" class="btn-cta">{cta_button_text}</a>
                    </div>
                </div>

                <!-- Sidebar -->
                <aside class="sidebar">
                    <!-- Author Bio -->
                    <div class="author-bio">
                        <img src="{author_avatar}" alt="{author_name}" />
                        <h3>{author_name}</h3>
                        <p>{author_bio}</p>
                        <div class="social-links">
                            <a href="{author_twitter}">Twitter</a>
                            <a href="{author_linkedin}">LinkedIn</a>
                        </div>
                    </div>

                    <!-- Related Posts -->
                    <div class="related-posts">
                        <h3>Related Articles</h3>
                        <div class="related-post">
                            <img src="{related1_image}" alt="{related1_title}" />
                            <h4><a href="{related1_url}">{related1_title}</a></h4>
                        </div>
                        <div class="related-post">
                            <img src="{related2_image}" alt="{related2_title}" />
                            <h4><a href="{related2_url}">{related2_title}</a></h4>
                        </div>
                    </div>
                </aside>
            </div>
        </div>
    </div>
</article>
        ''',
        css_styles='''
.blog-article { font-family: 'Georgia', serif; line-height: 1.6; }
.article-header { background: #f8f9fa; padding: 40px 0; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.breadcrumb { font-size: 0.9rem; margin-bottom: 20px; color: #6c757d; }
.breadcrumb a { color: #007bff; text-decoration: none; }
.article-title { font-size: 3rem; margin-bottom: 20px; color: #333; }
.article-meta { display: flex; align-items: center; gap: 15px; margin-bottom: 30px; }
.author-avatar { width: 50px; height: 50px; border-radius: 50%; }
.meta-info span { margin-right: 15px; color: #6c757d; }
.featured-image { width: 100%; border-radius: 10px; }
.article-content { padding: 60px 0; }
.content-wrapper { display: grid; grid-template-columns: 2fr 1fr; gap: 40px; }
.main-content { max-width: none; }
.article-intro .lead { font-size: 1.3rem; color: #6c757d; margin-bottom: 40px; }
.content-section { margin-bottom: 40px; }
.content-section h2 { font-size: 2rem; margin-bottom: 20px; color: #333; }
.content-image { width: 100%; border-radius: 8px; margin: 20px 0; }
.highlight-quote { background: #f8f9fa; border-left: 4px solid #007bff; padding: 20px; margin: 30px 0; font-style: italic; }
.key-points { background: #e7f3ff; padding: 25px; border-radius: 8px; margin: 30px 0; }
.key-points ul { list-style: none; padding: 0; }
.key-points li { padding: 8px 0; position: relative; padding-left: 25px; }
.key-points li::before { content: "✓"; color: #28a745; position: absolute; left: 0; font-weight: bold; }
.article-cta { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 40px; border-radius: 10px; text-align: center; margin-top: 50px; }
.btn-cta { background: #ff6b6b; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold; }
.sidebar { }
.author-bio { background: #f8f9fa; padding: 25px; border-radius: 10px; text-align: center; margin-bottom: 30px; }
.author-bio img { width: 80px; height: 80px; border-radius: 50%; margin-bottom: 15px; }
.social-links a { margin: 0 10px; color: #007bff; text-decoration: none; }
.related-posts { background: #f8f9fa; padding: 25px; border-radius: 10px; }
.related-post { display: flex; gap: 15px; margin-bottom: 20px; }
.related-post img { width: 80px; height: 60px; object-fit: cover; border-radius: 5px; }
.related-post h4 { margin: 0; font-size: 1rem; }
.related-post a { color: #333; text-decoration: none; }
        ''',
        fields=['title', 'category', 'category_url', 'home_url', 'author_name', 'author_avatar', 'author_url', 'publish_date', 'read_time', 'featured_image', 'introduction', 'section1_title', 'section1_content', 'section1_image', 'section2_title', 'section2_content', 'quote', 'quote_author', 'section3_title', 'section3_content', 'takeaway1', 'takeaway2', 'takeaway3', 'takeaway4', 'conclusion', 'cta_title', 'cta_description', 'cta_link', 'cta_button_text', 'author_bio', 'author_twitter', 'author_linkedin', 'related1_title', 'related1_url', 'related1_image', 'related2_title', 'related2_url', 'related2_image'],
        tags=['blog', 'article', 'content', 'seo'],
        industry='Publishing'
    ),

    ContentTemplate(
        template_id='restaurant-menu',
        name='Restaurant Menu Page',
        description='Appetizing restaurant menu with categories, prices, and food images',
        category='Food & Restaurant',
        purpose='Menu display and online ordering',
        html_template='''
<div class="restaurant-menu">
    <!-- Header -->
    <header class="menu-header">
        <div class="container">
            <h1 class="restaurant-name">{restaurant_name}</h1>
            <p class="restaurant-tagline">{tagline}</p>
            <div class="restaurant-info">
                <span>{cuisine_type}</span> • 
                <span>{location}</span> • 
                <span>{phone}</span>
            </div>
        </div>
    </header>

    <!-- Menu Categories -->
    <nav class="menu-nav">
        <div class="container">
            <ul class="category-tabs">
                <li><a href="#appetizers" class="active">Appetizers</a></li>
                <li><a href="#mains">Main Courses</a></li>
                <li><a href="#desserts">Desserts</a></li>
                <li><a href="#beverages">Beverages</a></li>
            </ul>
        </div>
    </nav>

    <!-- Menu Content -->
    <main class="menu-content">
        <div class="container">
            <!-- Appetizers -->
            <section id="appetizers" class="menu-section">
                <h2 class="section-title">Appetizers</h2>
                <div class="menu-grid">
                    <div class="menu-item">
                        <img src="{appetizer1_image}" alt="{appetizer1_name}" />
                        <div class="item-info">
                            <h3 class="item-name">{appetizer1_name}</h3>
                            <p class="item-description">{appetizer1_description}</p>
                            <div class="item-footer">
                                <span class="price">{appetizer1_price}</span>
                                <button class="order-btn">Order Now</button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="menu-item">
                        <img src="{appetizer2_image}" alt="{appetizer2_name}" />
                        <div class="item-info">
                            <h3 class="item-name">{appetizer2_name}</h3>
                            <p class="item-description">{appetizer2_description}</p>
                            <div class="item-footer">
                                <span class="price">{appetizer2_price}</span>
                                <button class="order-btn">Order Now</button>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Main Courses -->
            <section id="mains" class="menu-section">
                <h2 class="section-title">Main Courses</h2>
                <div class="menu-grid">
                    <div class="menu-item featured">
                        <div class="featured-badge">Chef's Special</div>
                        <img src="{main1_image}" alt="{main1_name}" />
                        <div class="item-info">
                            <h3 class="item-name">{main1_name}</h3>
                            <p class="item-description">{main1_description}</p>
                            <div class="item-footer">
                                <span class="price">{main1_price}</span>
                                <button class="order-btn">Order Now</button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="menu-item">
                        <img src="{main2_image}" alt="{main2_name}" />
                        <div class="item-info">
                            <h3 class="item-name">{main2_name}</h3>
                            <p class="item-description">{main2_description}</p>
                            <div class="item-footer">
                                <span class="price">{main2_price}</span>
                                <button class="order-btn">Order Now</button>
                            </div>
                        </div>
                    </div>

                    <div class="menu-item">
                        <img src="{main3_image}" alt="{main3_name}" />
                        <div class="item-info">
                            <h3 class="item-name">{main3_name}</h3>
                            <p class="item-description">{main3_description}</p>
                            <div class="item-footer">
                                <span class="price">{main3_price}</span>
                                <button class="order-btn">Order Now</button>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Desserts -->
            <section id="desserts" class="menu-section">
                <h2 class="section-title">Desserts</h2>
                <div class="menu-grid">
                    <div class="menu-item">
                        <img src="{dessert1_image}" alt="{dessert1_name}" />
                        <div class="item-info">
                            <h3 class="item-name">{dessert1_name}</h3>
                            <p class="item-description">{dessert1_description}</p>
                            <div class="item-footer">
                                <span class="price">{dessert1_price}</span>
                                <button class="order-btn">Order Now</button>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- Contact & Hours -->
            <section class="restaurant-footer">
                <div class="footer-info">
                    <h3>Visit Us</h3>
                    <p><strong>Address:</strong> {address}</p>
                    <p><strong>Hours:</strong> {hours}</p>
                    <p><strong>Reservations:</strong> {reservation_phone}</p>
                </div>
            </section>
        </div>
    </main>
</div>
        ''',
        css_styles='''
.restaurant-menu { font-family: 'Arial', sans-serif; }
.menu-header { background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('restaurant-bg.jpg'); background-size: cover; color: white; padding: 80px 0; text-align: center; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.restaurant-name { font-size: 3.5rem; margin-bottom: 1rem; font-weight: bold; }
.restaurant-tagline { font-size: 1.3rem; margin-bottom: 1rem; opacity: 0.9; }
.restaurant-info { font-size: 1.1rem; }
.menu-nav { background: #2c3e50; padding: 0; position: sticky; top: 0; z-index: 100; }
.category-tabs { list-style: none; padding: 0; margin: 0; display: flex; }
.category-tabs li { flex: 1; }
.category-tabs a { display: block; padding: 20px; text-align: center; color: white; text-decoration: none; transition: background 0.3s; }
.category-tabs a:hover, .category-tabs a.active { background: #34495e; }
.menu-content { padding: 60px 0; }
.menu-section { margin-bottom: 80px; }
.section-title { font-size: 2.5rem; text-align: center; margin-bottom: 50px; color: #2c3e50; }
.menu-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; }
.menu-item { background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s; position: relative; }
.menu-item:hover { transform: translateY(-5px); }
.menu-item.featured { border: 3px solid #e74c3c; }
.featured-badge { position: absolute; top: 15px; right: 15px; background: #e74c3c; color: white; padding: 5px 15px; border-radius: 20px; font-size: 0.8rem; z-index: 10; }
.menu-item img { width: 100%; height: 200px; object-fit: cover; }
.item-info { padding: 25px; }
.item-name { font-size: 1.4rem; margin-bottom: 10px; color: #2c3e50; }
.item-description { color: #7f8c8d; margin-bottom: 20px; line-height: 1.6; }
.item-footer { display: flex; justify-content: space-between; align-items: center; }
.price { font-size: 1.3rem; font-weight: bold; color: #e74c3c; }
.order-btn { background: #27ae60; color: white; border: none; padding: 10px 20px; border-radius: 25px; cursor: pointer; transition: background 0.3s; }
.order-btn:hover { background: #219a52; }
.restaurant-footer { background: #ecf0f1; padding: 40px; border-radius: 10px; text-align: center; margin-top: 60px; }
.footer-info h3 { color: #2c3e50; margin-bottom: 20px; }
.footer-info p { margin-bottom: 10px; color: #7f8c8d; }
        ''',
        fields=['restaurant_name', 'tagline', 'cuisine_type', 'location', 'phone', 'appetizer1_name', 'appetizer1_description', 'appetizer1_price', 'appetizer1_image', 'appetizer2_name', 'appetizer2_description', 'appetizer2_price', 'appetizer2_image', 'main1_name', 'main1_description', 'main1_price', 'main1_image', 'main2_name', 'main2_description', 'main2_price', 'main2_image', 'main3_name', 'main3_description', 'main3_price', 'main3_image', 'dessert1_name', 'dessert1_description', 'dessert1_price', 'dessert1_image', 'address', 'hours', 'reservation_phone'],
        tags=['restaurant', 'menu', 'food', 'ordering'],
        industry='Food & Beverage'
    ),

    ContentTemplate(
        template_id='real-estate-listing',
        name='Real Estate Property Listing',
        description='Comprehensive property listing with gallery, details, and contact form',
        category='Real Estate',
        purpose='Property marketing and lead generation',
        html_template='''
<div class="property-listing">
    <!-- Property Header -->
    <header class="property-header">
        <div class="container">
            <div class="property-gallery">
                <div class="main-photo">
                    <img src="{main_image}" alt="{property_title}" />
                    <div class="property-badge">{property_status}</div>
                </div>
                <div class="photo-grid">
                    <img src="{image2}" alt="Property view 2" />
                    <img src="{image3}" alt="Property view 3" />
                    <img src="{image4}" alt="Property view 4" />
                    <div class="more-photos">+{more_photos_count} more</div>
                </div>
            </div>
        </div>
    </header>

    <!-- Property Details -->
    <section class="property-details">
        <div class="container">
            <div class="details-grid">
                <div class="main-details">
                    <h1 class="property-title">{property_title}</h1>
                    <p class="property-address">{address}</p>
                    <div class="price-section">
                        <span class="price">{price}</span>
                        <span class="price-note">{price_note}</span>
                    </div>

                    <!-- Key Features -->
                    <div class="key-features">
                        <div class="feature-item">
                            <i class="icon-bed"></i>
                            <span>{bedrooms} Bedrooms</span>
                        </div>
                        <div class="feature-item">
                            <i class="icon-bath"></i>
                            <span>{bathrooms} Bathrooms</span>
                        </div>
                        <div class="feature-item">
                            <i class="icon-area"></i>
                            <span>{square_feet} sq ft</span>
                        </div>
                        <div class="feature-item">
                            <i class="icon-car"></i>
                            <span>{garage_spaces} Garage</span>
                        </div>
                    </div>

                    <!-- Description -->
                    <div class="property-description">
                        <h2>Property Description</h2>
                        <p>{description}</p>
                    </div>

                    <!-- Features & Amenities -->
                    <div class="features-section">
                        <h2>Features & Amenities</h2>
                        <div class="features-grid">
                            <div class="feature-category">
                                <h3>Interior Features</h3>
                                <ul>
                                    <li>{interior_feature1}</li>
                                    <li>{interior_feature2}</li>
                                    <li>{interior_feature3}</li>
                                    <li>{interior_feature4}</li>
                                </ul>
                            </div>
                            <div class="feature-category">
                                <h3>Exterior Features</h3>
                                <ul>
                                    <li>{exterior_feature1}</li>
                                    <li>{exterior_feature2}</li>
                                    <li>{exterior_feature3}</li>
                                    <li>{exterior_feature4}</li>
                                </ul>
                            </div>
                        </div>
                    </div>

                    <!-- Neighborhood Info -->
                    <div class="neighborhood-section">
                        <h2>Neighborhood</h2>
                        <p>{neighborhood_description}</p>
                        <div class="nearby-places">
                            <div class="nearby-item">
                                <strong>Schools:</strong> {nearby_schools}
                            </div>
                            <div class="nearby-item">
                                <strong>Shopping:</strong> {nearby_shopping}
                            </div>
                            <div class="nearby-item">
                                <strong>Transportation:</strong> {nearby_transport}
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Sidebar -->
                <aside class="property-sidebar">
                    <!-- Agent Info -->
                    <div class="agent-card">
                        <img src="{agent_photo}" alt="{agent_name}" class="agent-photo" />
                        <h3>{agent_name}</h3>
                        <p class="agent-title">{agent_title}</p>
                        <div class="agent-contact">
                            <p><strong>Phone:</strong> {agent_phone}</p>
                            <p><strong>Email:</strong> {agent_email}</p>
                        </div>
                        <button class="btn-contact">Contact Agent</button>
                    </div>

                    <!-- Quick Stats -->
                    <div class="property-stats">
                        <h3>Property Details</h3>
                        <div class="stat-item">
                            <span class="label">Property Type:</span>
                            <span class="value">{property_type}</span>
                        </div>
                        <div class="stat-item">
                            <span class="label">Year Built:</span>
                            <span class="value">{year_built}</span>
                        </div>
                        <div class="stat-item">
                            <span class="label">Lot Size:</span>
                            <span class="value">{lot_size}</span>
                        </div>
                        <div class="stat-item">
                            <span class="label">HOA Fees:</span>
                            <span class="value">{hoa_fees}</span>
                        </div>
                        <div class="stat-item">
                            <span class="label">Property Tax:</span>
                            <span class="value">{property_tax}</span>
                        </div>
                    </div>

                    <!-- Schedule Tour -->
                    <div class="schedule-tour">
                        <h3>Schedule a Tour</h3>
                        <p>See this property in person</p>
                        <button class="btn-tour">Schedule Tour</button>
                        <button class="btn-virtual">Virtual Tour</button>
                    </div>
                </aside>
            </div>
        </div>
    </section>
</div>
        ''',
        css_styles='''
.property-listing { font-family: 'Arial', sans-serif; }
.property-header { padding: 0; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; }
.property-gallery { }
.main-photo { position: relative; margin-bottom: 15px; }
.main-photo img { width: 100%; height: 400px; object-fit: cover; border-radius: 10px; }
.property-badge { position: absolute; top: 20px; left: 20px; background: #e74c3c; color: white; padding: 8px 15px; border-radius: 5px; font-weight: bold; }
.photo-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
.photo-grid img { width: 100%; height: 100px; object-fit: cover; border-radius: 5px; }
.more-photos { background: #2c3e50; color: white; display: flex; align-items: center; justify-content: center; border-radius: 5px; font-weight: bold; }
.property-details { padding: 40px 0; }
.details-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 40px; }
.property-title { font-size: 2.5rem; margin-bottom: 10px; color: #2c3e50; }
.property-address { color: #7f8c8d; font-size: 1.2rem; margin-bottom: 20px; }
.price-section { margin-bottom: 30px; }
.price { font-size: 2.5rem; font-weight: bold; color: #27ae60; }
.price-note { color: #7f8c8d; margin-left: 10px; }
.key-features { display: flex; gap: 30px; margin-bottom: 40px; flex-wrap: wrap; }
.feature-item { display: flex; align-items: center; gap: 8px; background: #ecf0f1; padding: 15px 20px; border-radius: 8px; }
.property-description, .features-section, .neighborhood-section { margin-bottom: 40px; }
.property-description h2, .features-section h2, .neighborhood-section h2 { color: #2c3e50; margin-bottom: 20px; }
.features-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 30px; }
.feature-category ul { list-style: none; padding: 0; }
.feature-category li { padding: 8px 0; border-bottom: 1px solid #ecf0f1; }
.nearby-places { display: grid; grid-template-columns: 1fr; gap: 15px; }
.nearby-item { background: #f8f9fa; padding: 15px; border-radius: 8px; }
.property-sidebar { }
.agent-card { background: #f8f9fa; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 30px; }
.agent-photo { width: 100px; height: 100px; border-radius: 50%; margin-bottom: 15px; }
.agent-card h3 { margin-bottom: 5px; color: #2c3e50; }
.agent-title { color: #7f8c8d; margin-bottom: 20px; }
.agent-contact p { margin-bottom: 8px; text-align: left; }
.btn-contact { background: #3498db; color: white; padding: 12px 25px; border: none; border-radius: 5px; width: 100%; cursor: pointer; margin-top: 15px; }
.property-stats { background: #f8f9fa; padding: 25px; border-radius: 10px; margin-bottom: 30px; }
.stat-item { display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #ecf0f1; }
.stat-item:last-child { border-bottom: none; }
.label { color: #7f8c8d; }
.value { font-weight: bold; color: #2c3e50; }
.schedule-tour { background: #2c3e50; color: white; padding: 25px; border-radius: 10px; text-align: center; }
.btn-tour, .btn-virtual { background: #e74c3c; color: white; padding: 12px 20px; border: none; border-radius: 5px; margin: 5px; cursor: pointer; }
.btn-virtual { background: #27ae60; }
        ''',
        fields=['property_title', 'address', 'price', 'price_note', 'main_image', 'image2', 'image3', 'image4', 'more_photos_count', 'property_status', 'bedrooms', 'bathrooms', 'square_feet', 'garage_spaces', 'description', 'interior_feature1', 'interior_feature2', 'interior_feature3', 'interior_feature4', 'exterior_feature1', 'exterior_feature2', 'exterior_feature3', 'exterior_feature4', 'neighborhood_description', 'nearby_schools', 'nearby_shopping', 'nearby_transport', 'agent_name', 'agent_title', 'agent_phone', 'agent_email', 'agent_photo', 'property_type', 'year_built', 'lot_size', 'hoa_fees', 'property_tax'],
        tags=['real-estate', 'property', 'listing', 'marketing'],
        industry='Real Estate'
    ),

    ContentTemplate(
        template_id='event-landing',
        name='Event Landing Page',
        description='Engaging event landing page with schedule, speakers, and registration',
        category='Events',
        purpose='Event promotion and ticket sales',
        html_template='''
<div class="event-landing">
    <!-- Hero Section -->
    <header class="event-hero">
        <div class="container">
            <div class="hero-content">
                <div class="event-date">{event_date}</div>
                <h1 class="event-title">{event_title}</h1>
                <p class="event-subtitle">{subtitle}</p>
                <div class="event-location">
                    <i class="icon-location"></i>
                    <span>{location}</span>
                </div>
                <div class="hero-cta">
                    <a href="{register_link}" class="btn-register">{register_button_text}</a>
                    <div class="ticket-info">
                        <span class="price">{ticket_price}</span>
                        <span class="seats-left">{seats_available} seats left</span>
                    </div>
                </div>
            </div>
            <div class="hero-image">
                <img src="{hero_image}" alt="{event_title}" />
            </div>
        </div>
    </header>

    <!-- Event Highlights -->
    <section class="event-highlights">
        <div class="container">
            <h2>Why Attend?</h2>
            <div class="highlights-grid">
                <div class="highlight-item">
                    <div class="highlight-icon">
                        <i class="icon-users"></i>
                    </div>
                    <h3>{highlight1_title}</h3>
                    <p>{highlight1_description}</p>
                </div>
                <div class="highlight-item">
                    <div class="highlight-icon">
                        <i class="icon-trophy"></i>
                    </div>
                    <h3>{highlight2_title}</h3>
                    <p>{highlight2_description}</p>
                </div>
                <div class="highlight-item">
                    <div class="highlight-icon">
                        <i class="icon-certificate"></i>
                    </div>
                    <h3>{highlight3_title}</h3>
                    <p>{highlight3_description}</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Speakers Section -->
    <section class="speakers-section">
        <div class="container">
            <h2>Featured Speakers</h2>
            <div class="speakers-grid">
                <div class="speaker-card">
                    <img src="{speaker1_photo}" alt="{speaker1_name}" />
                    <h3>{speaker1_name}</h3>
                    <p class="speaker-title">{speaker1_title}</p>
                    <p class="speaker-company">{speaker1_company}</p>
                    <p class="speaker-bio">{speaker1_bio}</p>
                </div>
                <div class="speaker-card">
                    <img src="{speaker2_photo}" alt="{speaker2_name}" />
                    <h3>{speaker2_name}</h3>
                    <p class="speaker-title">{speaker2_title}</p>
                    <p class="speaker-company">{speaker2_company}</p>
                    <p class="speaker-bio">{speaker2_bio}</p>
                </div>
                <div class="speaker-card">
                    <img src="{speaker3_photo}" alt="{speaker3_name}" />
                    <h3>{speaker3_name}</h3>
                    <p class="speaker-title">{speaker3_title}</p>
                    <p class="speaker-company">{speaker3_company}</p>
                    <p class="speaker-bio">{speaker3_bio}</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Schedule -->
    <section class="schedule-section">
        <div class="container">
            <h2>Event Schedule</h2>
            <div class="schedule-timeline">
                <div class="schedule-item">
                    <div class="time">{session1_time}</div>
                    <div class="session-info">
                        <h3>{session1_title}</h3>
                        <p>{session1_description}</p>
                        <span class="speaker">Speaker: {session1_speaker}</span>
                    </div>
                </div>
                <div class="schedule-item">
                    <div class="time">{session2_time}</div>
                    <div class="session-info">
                        <h3>{session2_title}</h3>
                        <p>{session2_description}</p>
                        <span class="speaker">Speaker: {session2_speaker}</span>
                    </div>
                </div>
                <div class="schedule-item">
                    <div class="time">{session3_time}</div>
                    <div class="session-info">
                        <h3>{session3_title}</h3>
                        <p>{session3_description}</p>
                        <span class="speaker">Speaker: {session3_speaker}</span>
                    </div>
                </div>
                <div class="schedule-item">
                    <div class="time">{session4_time}</div>
                    <div class="session-info">
                        <h3>{session4_title}</h3>
                        <p>{session4_description}</p>
                        <span class="speaker">Speaker: {session4_speaker}</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Registration CTA -->
    <section class="registration-cta">
        <div class="container">
            <div class="cta-content">
                <h2>Ready to Join Us?</h2>
                <p>Don't miss this opportunity to {cta_description}</p>
                <div class="urgency-info">
                    <span class="limited-time">Early Bird Price: {early_bird_price}</span>
                    <span class="deadline">Ends {early_bird_deadline}</span>
                </div>
                <a href="{register_link}" class="btn-register-large">Register Now - {ticket_price}</a>
                <p class="guarantee">{money_back_guarantee}</p>
            </div>
        </div>
    </section>

    <!-- Event Info -->
    <section class="event-info">
        <div class="container">
            <div class="info-grid">
                <div class="info-item">
                    <h3>Event Details</h3>
                    <p><strong>Date:</strong> {event_date}</p>
                    <p><strong>Time:</strong> {event_time}</p>
                    <p><strong>Duration:</strong> {event_duration}</p>
                    <p><strong>Format:</strong> {event_format}</p>
                </div>
                <div class="info-item">
                    <h3>Location</h3>
                    <p><strong>Venue:</strong> {venue_name}</p>
                    <p><strong>Address:</strong> {venue_address}</p>
                    <p><strong>Parking:</strong> {parking_info}</p>
                </div>
                <div class="info-item">
                    <h3>Contact</h3>
                    <p><strong>Email:</strong> {contact_email}</p>
                    <p><strong>Phone:</strong> {contact_phone}</p>
                    <p><strong>Support:</strong> {support_hours}</p>
                </div>
            </div>
        </div>
    </section>
</div>
        ''',
        css_styles='''
.event-landing { font-family: 'Arial', sans-serif; }
.event-hero { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 80px 0; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; align-items: center; gap: 40px; }
.hero-content { flex: 1; }
.event-date { background: rgba(255,255,255,0.2); padding: 8px 15px; border-radius: 20px; display: inline-block; margin-bottom: 20px; font-weight: bold; }
.event-title { font-size: 3.5rem; margin-bottom: 1rem; font-weight: bold; }
.event-subtitle { font-size: 1.3rem; margin-bottom: 1.5rem; opacity: 0.9; }
.event-location { display: flex; align-items: center; gap: 10px; margin-bottom: 2rem; font-size: 1.1rem; }
.hero-cta { }
.btn-register { background: #e74c3c; color: white; padding: 18px 35px; text-decoration: none; border-radius: 8px; font-size: 1.2rem; font-weight: bold; display: inline-block; margin-bottom: 15px; }
.ticket-info { }
.price { font-size: 1.5rem; font-weight: bold; margin-right: 15px; }
.seats-left { color: #f39c12; font-weight: bold; }
.hero-image { flex: 1; }
.hero-image img { width: 100%; border-radius: 15px; }
.event-highlights { padding: 80px 0; background: #f8f9fa; }
.event-highlights .container { display: block; }
.event-highlights h2 { text-align: center; font-size: 2.5rem; margin-bottom: 50px; color: #2c3e50; }
.highlights-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; }
.highlight-item { text-align: center; }
.highlight-icon { background: #3498db; color: white; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 2rem; }
.speakers-section { padding: 80px 0; }
.speakers-section .container { display: block; }
.speakers-section h2 { text-align: center; font-size: 2.5rem; margin-bottom: 50px; color: #2c3e50; }
.speakers-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
.speaker-card { background: white; padding: 30px; border-radius: 15px; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
.speaker-card img { width: 120px; height: 120px; border-radius: 50%; margin-bottom: 20px; object-fit: cover; }
.speaker-card h3 { color: #2c3e50; margin-bottom: 5px; }
.speaker-title { color: #3498db; font-weight: bold; margin-bottom: 5px; }
.speaker-company { color: #7f8c8d; margin-bottom: 15px; }
.speaker-bio { color: #7f8c8d; line-height: 1.6; }
.schedule-section { padding: 80px 0; background: #f8f9fa; }
.schedule-section .container { display: block; }
.schedule-section h2 { text-align: center; font-size: 2.5rem; margin-bottom: 50px; color: #2c3e50; }
.schedule-timeline { max-width: 800px; margin: 0 auto; }
.schedule-item { display: flex; gap: 30px; margin-bottom: 30px; padding: 25px; background: white; border-radius: 10px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
.time { background: #3498db; color: white; padding: 15px 20px; border-radius: 8px; font-weight: bold; min-width: 120px; text-align: center; }
.session-info h3 { color: #2c3e50; margin-bottom: 10px; }
.session-info p { color: #7f8c8d; margin-bottom: 10px; }
.speaker { color: #3498db; font-weight: bold; }
.registration-cta { background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); color: white; padding: 80px 0; text-align: center; }
.registration-cta .container { display: block; }
.cta-content h2 { font-size: 2.5rem; margin-bottom: 20px; }
.urgency-info { margin: 30px 0; }
.limited-time { background: rgba(255,255,255,0.2); padding: 10px 20px; border-radius: 25px; margin-right: 15px; }
.deadline { font-weight: bold; }
.btn-register-large { background: white; color: #e74c3c; padding: 20px 40px; text-decoration: none; border-radius: 8px; font-size: 1.3rem; font-weight: bold; display: inline-block; margin: 20px 0; }
.guarantee { opacity: 0.8; margin-top: 15px; }
.event-info { padding: 80px 0; }
.event-info .container { display: block; }
.info-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 40px; }
.info-item h3 { color: #2c3e50; margin-bottom: 20px; }
.info-item p { margin-bottom: 10px; color: #7f8c8d; }
        ''',
        fields=['event_title', 'subtitle', 'event_date', 'location', 'register_link', 'register_button_text', 'ticket_price', 'seats_available', 'hero_image', 'highlight1_title', 'highlight1_description', 'highlight2_title', 'highlight2_description', 'highlight3_title', 'highlight3_description', 'speaker1_name', 'speaker1_title', 'speaker1_company', 'speaker1_bio', 'speaker1_photo', 'speaker2_name', 'speaker2_title', 'speaker2_company', 'speaker2_bio', 'speaker2_photo', 'speaker3_name', 'speaker3_title', 'speaker3_company', 'speaker3_bio', 'speaker3_photo', 'session1_time', 'session1_title', 'session1_description', 'session1_speaker', 'session2_time', 'session2_title', 'session2_description', 'session2_speaker', 'session3_time', 'session3_title', 'session3_description', 'session3_speaker', 'session4_time', 'session4_title', 'session4_description', 'session4_speaker', 'cta_description', 'early_bird_price', 'early_bird_deadline', 'money_back_guarantee', 'event_time', 'event_duration', 'event_format', 'venue_name', 'venue_address', 'parking_info', 'contact_email', 'contact_phone', 'support_hours'],
        tags=['event', 'conference', 'registration', 'speakers'],
        industry='Events & Conferences'
    ),

    ContentTemplate(
        template_id='portfolio-showcase',
        name='Portfolio Showcase',
        description='Creative portfolio showcase for designers, photographers, or agencies',
        category='Portfolio',
        purpose='Creative work presentation and client acquisition',
        html_template='''
<div class="portfolio-showcase">
    <!-- Hero Section -->
    <header class="portfolio-hero">
        <div class="container">
            <div class="hero-content">
                <h1 class="portfolio-title">{portfolio_title}</h1>
                <p class="portfolio-subtitle">{subtitle}</p>
                <p class="portfolio-description">{description}</p>
                <div class="hero-cta">
                    <a href="{contact_link}" class="btn-contact">{contact_button_text}</a>
                    <a href="{portfolio_link}" class="btn-portfolio">{portfolio_button_text}</a>
                </div>
            </div>
            <div class="hero-visual">
                <img src="{hero_image}" alt="{portfolio_title}" />
            </div>
        </div>
    </header>

    <!-- Featured Work -->
    <section class="featured-work">
        <div class="container">
            <h2>Featured Projects</h2>
            <div class="projects-grid">
                <div class="project-card featured">
                    <div class="project-image">
                        <img src="{project1_image}" alt="{project1_title}" />
                        <div class="project-overlay">
                            <h3>{project1_title}</h3>
                            <p>{project1_category}</p>
                            <a href="{project1_link}" class="view-project">View Project</a>
                        </div>
                    </div>
                    <div class="project-info">
                        <h3>{project1_title}</h3>
                        <p class="project-category">{project1_category}</p>
                        <p class="project-description">{project1_description}</p>
                    </div>
                </div>

                <div class="project-card">
                    <div class="project-image">
                        <img src="{project2_image}" alt="{project2_title}" />
                        <div class="project-overlay">
                            <h3>{project2_title}</h3>
                            <p>{project2_category}</p>
                            <a href="{project2_link}" class="view-project">View Project</a>
                        </div>
                    </div>
                    <div class="project-info">
                        <h3>{project2_title}</h3>
                        <p class="project-category">{project2_category}</p>
                        <p class="project-description">{project2_description}</p>
                    </div>
                </div>

                <div class="project-card">
                    <div class="project-image">
                        <img src="{project3_image}" alt="{project3_title}" />
                        <div class="project-overlay">
                            <h3>{project3_title}</h3>
                            <p>{project3_category}</p>
                            <a href="{project3_link}" class="view-project">View Project</a>
                        </div>
                    </div>
                    <div class="project-info">
                        <h3>{project3_title}</h3>
                        <p class="project-category">{project3_category}</p>
                        <p class="project-description">{project3_description}</p>
                    </div>
                </div>

                <div class="project-card">
                    <div class="project-image">
                        <img src="{project4_image}" alt="{project4_title}" />
                        <div class="project-overlay">
                            <h3>{project4_title}</h3>
                            <p>{project4_category}</p>
                            <a href="{project4_link}" class="view-project">View Project</a>
                        </div>
                    </div>
                    <div class="project-info">
                        <h3>{project4_title}</h3>
                        <p class="project-category">{project4_category}</p>
                        <p class="project-description">{project4_description}</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services -->
    <section class="services-section">
        <div class="container">
            <h2>What I Do</h2>
            <div class="services-grid">
                <div class="service-item">
                    <div class="service-icon">
                        <i class="icon-design"></i>
                    </div>
                    <h3>{service1_title}</h3>
                    <p>{service1_description}</p>
                </div>
                <div class="service-item">
                    <div class="service-icon">
                        <i class="icon-code"></i>
                    </div>
                    <h3>{service2_title}</h3>
                    <p>{service2_description}</p>
                </div>
                <div class="service-item">
                    <div class="service-icon">
                        <i class="icon-camera"></i>
                    </div>
                    <h3>{service3_title}</h3>
                    <p>{service3_description}</p>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="about-section">
        <div class="container">
            <div class="about-content">
                <div class="about-text">
                    <h2>About {creator_name}</h2>
                    <p>{about_description}</p>
                    <div class="experience-stats">
                        <div class="stat-item">
                            <span class="stat-number">{years_experience}</span>
                            <span class="stat-label">Years Experience</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-number">{projects_completed}</span>
                            <span class="stat-label">Projects Completed</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-number">{happy_clients}</span>
                            <span class="stat-label">Happy Clients</span>
                        </div>
                    </div>
                </div>
                <div class="about-image">
                    <img src="{creator_photo}" alt="{creator_name}" />
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials -->
    <section class="testimonials-section">
        <div class="container">
            <h2>What Clients Say</h2>
            <div class="testimonials-grid">
                <div class="testimonial-card">
                    <div class="testimonial-content">
                        <p>"{testimonial1_text}"</p>
                    </div>
                    <div class="testimonial-author">
                        <img src="{testimonial1_avatar}" alt="{testimonial1_name}" />
                        <div class="author-info">
                            <h4>{testimonial1_name}</h4>
                            <p>{testimonial1_title}</p>
                            <p>{testimonial1_company}</p>
                        </div>
                    </div>
                </div>
                <div class="testimonial-card">
                    <div class="testimonial-content">
                        <p>"{testimonial2_text}"</p>
                    </div>
                    <div class="testimonial-author">
                        <img src="{testimonial2_avatar}" alt="{testimonial2_name}" />
                        <div class="author-info">
                            <h4>{testimonial2_name}</h4>
                            <p>{testimonial2_title}</p>
                            <p>{testimonial2_company}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact CTA -->
    <section class="contact-cta">
        <div class="container">
            <div class="cta-content">
                <h2>Ready to Work Together?</h2>
                <p>{contact_description}</p>
                <a href="{contact_link}" class="btn-contact-large">{contact_button_text}</a>
                <div class="contact-info">
                    <p><strong>Email:</strong> {email}</p>
                    <p><strong>Phone:</strong> {phone}</p>
                </div>
            </div>
        </div>
    </section>
</div>
        ''',
        css_styles='''
.portfolio-showcase { font-family: 'Arial', sans-serif; }
.portfolio-hero { background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%); color: white; padding: 100px 0; }
.container { max-width: 1200px; margin: 0 auto; padding: 0 20px; display: flex; align-items: center; gap: 60px; }
.hero-content { flex: 1; }
.portfolio-title { font-size: 3.5rem; margin-bottom: 1rem; font-weight: bold; }
.portfolio-subtitle { font-size: 1.5rem; margin-bottom: 1.5rem; color: #3498db; }
.portfolio-description { font-size: 1.1rem; margin-bottom: 2rem; opacity: 0.9; line-height: 1.6; }
.hero-cta { display: flex; gap: 15px; }
.btn-contact { background: #e74c3c; color: white; padding: 15px 30px; text-decoration: none; border-radius: 5px; font-weight: bold; }
.btn-portfolio { background: transparent; color: white; padding: 15px 30px; text-decoration: none; border: 2px solid white; border-radius: 5px; font-weight: bold; }
.hero-visual { flex: 1; }
.hero-visual img { width: 100%; border-radius: 15px; }
.featured-work { padding: 100px 0; }
.featured-work .container { display: block; }
.featured-work h2 { text-align: center; font-size: 2.5rem; margin-bottom: 60px; color: #2c3e50; }
.projects-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
.project-card { background: white; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1); transition: transform 0.3s; }
.project-card:hover { transform: translateY(-10px); }
.project-card.featured { grid-column: span 2; }
.project-image { position: relative; overflow: hidden; }
.project-image img { width: 100%; height: 250px; object-fit: cover; transition: transform 0.3s; }
.project-card:hover .project-image img { transform: scale(1.1); }
.project-overlay { position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.8); color: white; display: flex; flex-direction: column; justify-content: center; align-items: center; opacity: 0; transition: opacity 0.3s; }
.project-card:hover .project-overlay { opacity: 1; }
.view-project { background: #3498db; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin-top: 15px; }
.project-info { padding: 25px; }
.project-category { color: #3498db; font-weight: bold; margin-bottom: 10px; }
.services-section { background: #f8f9fa; padding: 80px 0; }
.services-section .container { display: block; }
.services-section h2 { text-align: center; font-size: 2.5rem; margin-bottom: 60px; color: #2c3e50; }
.services-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 40px; }
.service-item { text-align: center; }
.service-icon { background: #3498db; color: white; width: 80px; height: 80px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 20px; font-size: 2rem; }
.about-section { padding: 100px 0; }
.about-content { display: flex; align-items: center; gap: 60px; }
.about-text { flex: 1; }
.about-text h2 { font-size: 2.5rem; margin-bottom: 30px; color: #2c3e50; }
.experience-stats { display: flex; gap: 40px; margin-top: 40px; }
.stat-item { text-align: center; }
.stat-number { display: block; font-size: 2.5rem; font-weight: bold; color: #3498db; }
.stat-label { color: #7f8c8d; }
.about-image { flex: 0 0 300px; }
.about-image img { width: 100%; border-radius: 15px; }
.testimonials-section { background: #f8f9fa; padding: 80px 0; }
.testimonials-section .container { display: block; }
.testimonials-section h2 { text-align: center; font-size: 2.5rem; margin-bottom: 60px; color: #2c3e50; }
.testimonials-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(400px, 1fr)); gap: 30px; }
.testimonial-card { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
.testimonial-content p { font-style: italic; margin-bottom: 30px; color: #7f8c8d; line-height: 1.6; }
.testimonial-author { display: flex; align-items: center; gap: 15px; }
.testimonial-author img { width: 60px; height: 60px; border-radius: 50%; }
.author-info h4 { color: #2c3e50; margin-bottom: 5px; }
.author-info p { color: #7f8c8d; margin: 0; }
.contact-cta { background: linear-gradient(135deg, #3498db 0%, #2980b9 100%); color: white; padding: 100px 0; text-align: center; }
.contact-cta .container { display: block; }
.cta-content h2 { font-size: 2.5rem; margin-bottom: 20px; }
.cta-content p { font-size: 1.2rem; margin-bottom: 40px; opacity: 0.9; }
.btn-contact-large { background: #e74c3c; color: white; padding: 20px 40px; text-decoration: none; border-radius: 8px; font-size: 1.2rem; font-weight: bold; display: inline-block; margin-bottom: 30px; }
.contact-info p { margin: 5px 0; opacity: 0.8; }
        ''',
        fields=['portfolio_title', 'subtitle', 'description', 'contact_link', 'contact_button_text', 'portfolio_link', 'portfolio_button_text', 'hero_image', 'project1_title', 'project1_category', 'project1_description', 'project1_image', 'project1_link', 'project2_title', 'project2_category', 'project2_description', 'project2_image', 'project2_link', 'project3_title', 'project3_category', 'project3_description', 'project3_image', 'project3_link', 'project4_title', 'project4_category', 'project4_description', 'project4_image', 'project4_link', 'service1_title', 'service1_description', 'service2_title', 'service2_description', 'service3_title', 'service3_description', 'creator_name', 'about_description', 'years_experience', 'projects_completed', 'happy_clients', 'creator_photo', 'testimonial1_text', 'testimonial1_name', 'testimonial1_title', 'testimonial1_company', 'testimonial1_avatar', 'testimonial2_text', 'testimonial2_name', 'testimonial2_title', 'testimonial2_company', 'testimonial2_avatar', 'contact_description', 'email', 'phone'],
        tags=['portfolio', 'creative', 'showcase', 'professional'],
        industry='Creative Services'
    )
]

# Template registry for easy access
CONTENT_TEMPLATE_REGISTRY = {template.id: template for template in CONTENT_TEMPLATES}

def get_content_template_by_id(template_id):
    """Get content template by ID"""
    return CONTENT_TEMPLATE_REGISTRY.get(template_id)

def get_all_content_templates():
    """Get all available content templates"""
    return CONTENT_TEMPLATES

def get_content_templates_by_category(category):
    """Get content templates by category"""
    return [template for template in CONTENT_TEMPLATES if template.category == category]

def get_content_template_categories():
    """Get all unique content template categories"""
    return list(set(template.category for template in CONTENT_TEMPLATES))

def get_content_templates_by_industry(industry):
    """Get content templates by industry"""
    return [template for template in CONTENT_TEMPLATES if template.industry == industry]

def search_content_templates(query):
    """Search content templates by name, description, or tags"""
    query = query.lower()
    results = []
    
    for template in CONTENT_TEMPLATES:
        if (query in template.name.lower() or 
            query in template.description.lower() or 
            query in template.purpose.lower() or
            any(query in tag.lower() for tag in template.tags)):
            results.append(template)
    
    return results