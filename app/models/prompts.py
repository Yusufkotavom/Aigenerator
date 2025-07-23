"""Prompt templates and management"""

class PromptTemplate:
    """Prompt template data structure"""
    
    def __init__(self, template_id, name, description, prompt, category, tags=None):
        self.id = template_id
        self.name = name
        self.description = description
        self.prompt = prompt
        self.category = category
        self.tags = tags or []
    
    def to_dict(self):
        """Convert template to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'prompt': self.prompt,
            'category': self.category,
            'tags': self.tags
        }

# Predefined prompt templates
PROMPT_TEMPLATES = [
    PromptTemplate(
        template_id='creative-story',
        name='Cerita Kreatif',
        description='Template untuk menulis cerita pendek yang menarik',
        prompt='Tulis sebuah cerita pendek yang menarik tentang seorang anak yang menemukan benda ajaib di loteng rumah neneknya. Cerita harus memiliki awal yang menarik, konflik yang jelas, dan akhir yang memuaskan. Panjang sekitar 300-500 kata.',
        category='Creative Writing',
        tags=['cerita', 'fiksi', 'kreatif', 'naratif']
    ),
    PromptTemplate(
        template_id='explain-concept',
        name='Penjelasan Konsep',
        description='Template untuk menjelaskan konsep kompleks dengan sederhana',
        prompt='Jelaskan konsep {konsep} dengan bahasa yang mudah dipahami oleh anak berusia 12 tahun. Gunakan analogi dan contoh konkret. Struktur penjelasan: 1) Definisi sederhana, 2) Analogi yang mudah dipahami, 3) Contoh dalam kehidupan sehari-hari, 4) Mengapa konsep ini penting.',
        category='Education',
        tags=['penjelasan', 'edukasi', 'konsep', 'pembelajaran']
    ),
    PromptTemplate(
        template_id='code-helper',
        name='Bantuan Coding',
        description='Template untuk meminta bantuan pemrograman',
        prompt='Buatkan kode Python untuk {fungsi_yang_diinginkan}. Persyaratan:\n1. Kode harus bersih dan mudah dibaca\n2. Sertakan komentar yang jelas\n3. Tambahkan error handling\n4. Berikan contoh penggunaan\n5. Jelaskan cara kerja algoritma yang digunakan',
        category='Programming',
        tags=['coding', 'python', 'programming', 'bantuan']
    ),
    PromptTemplate(
        template_id='business-analysis',
        name='Analisis Bisnis',
        description='Template untuk analisis ide bisnis',
        prompt='Lakukan analisis mendalam terhadap ide bisnis berikut: {ide_bisnis}. Analisis harus mencakup:\n1. Target market dan segmentasi\n2. Analisis kompetitor\n3. Model revenue yang potensial\n4. Risiko dan tantangan utama\n5. Strategi marketing awal\n6. Estimasi modal yang diperlukan\n7. Timeline implementasi\n\nBerikan rekomendasi apakah ide ini layak untuk dilanjutkan.',
        category='Business',
        tags=['bisnis', 'analisis', 'market', 'strategi']
    ),
    PromptTemplate(
        template_id='translate-improve',
        name='Terjemahan & Perbaikan',
        description='Template untuk terjemahan dan perbaikan teks',
        prompt='Lakukan tugas berikut untuk teks yang diberikan:\n1. Terjemahkan dari {bahasa_asal} ke {bahasa_tujuan}\n2. Perbaiki tata bahasa dan struktur kalimat\n3. Sesuaikan dengan konteks budaya\n4. Pastikan tone dan gaya bahasa konsisten\n5. Berikan alternatif terjemahan untuk frasa yang ambigu\n\nTeks: {teks_yang_akan_diterjemahkan}',
        category='Translation',
        tags=['terjemahan', 'bahasa', 'perbaikan', 'editing']
    ),
    PromptTemplate(
        template_id='content-creator',
        name='Content Creator',
        description='Template untuk membuat konten media sosial',
        prompt='Buatkan konten untuk {platform_media_sosial} dengan tema {tema_konten}. Konten harus:\n1. Menarik perhatian dalam 3 detik pertama\n2. Memberikan value atau hiburan\n3. Sesuai dengan algoritma platform\n4. Include call-to-action yang natural\n5. Menggunakan hashtag yang relevan\n6. Panjang sesuai dengan best practice platform\n\nTarget audience: {target_audience}\nTone: {tone_konten}',
        category='Content Marketing',
        tags=['content', 'sosmed', 'marketing', 'viral']
    ),
    PromptTemplate(
        template_id='problem-solver',
        name='Problem Solving',
        description='Template untuk memecahkan masalah secara sistematis',
        prompt='Bantu saya memecahkan masalah berikut: {deskripsi_masalah}\n\nGunakan framework problem solving berikut:\n1. Identifikasi dan definisi masalah dengan jelas\n2. Analisis akar penyebab (root cause analysis)\n3. Brainstorming minimal 5 solusi alternatif\n4. Evaluasi pro dan kontra setiap solusi\n5. Rekomendasi solusi terbaik dengan alasan\n6. Langkah implementasi konkret\n7. Metrik untuk mengukur keberhasilan\n\nBerikan jawaban yang terstruktur dan actionable.',
        category='Problem Solving',
        tags=['masalah', 'solusi', 'analisis', 'sistematis']
    )
]

# Template registry
TEMPLATE_REGISTRY = {template.id: template for template in PROMPT_TEMPLATES}

def get_template_by_id(template_id):
    """Get template by ID"""
    return TEMPLATE_REGISTRY.get(template_id)

def get_all_templates():
    """Get all available templates"""
    return PROMPT_TEMPLATES

def get_templates_by_category(category):
    """Get templates by category"""
    return [template for template in PROMPT_TEMPLATES if template.category == category]

def get_template_categories():
    """Get all unique categories"""
    return list(set(template.category for template in PROMPT_TEMPLATES))

def search_templates(query):
    """Search templates by name, description, or tags"""
    query = query.lower()
    results = []
    
    for template in PROMPT_TEMPLATES:
        if (query in template.name.lower() or 
            query in template.description.lower() or 
            any(query in tag.lower() for tag in template.tags)):
            results.append(template)
    
    return results