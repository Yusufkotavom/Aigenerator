# 🚀 Quick Start Guide - AI Bulk Content Generator

Panduan cepat untuk memulai generate ratusan halaman konten WordPress dalam hitungan menit!

## 📋 Prerequisites

- Python 3.8+ installed
- Basic knowledge of CSV files
- WordPress site (opsional untuk testing)

## ⚡ 5-Minute Setup

### 1. Install & Run
```bash
# Clone & setup
git clone <repository-url>
cd ai-bulk-generator
pip install -r requirements.txt

# Run aplikasi
python run.py
```

### 2. Access Application
```
http://localhost:5000
```

### 3. Pilih "Bulk Generator" dari menu

## 🎯 Generate Content Pertama

### Step 1: Download Template CSV
1. Pilih template **"Business Landing Page"**
2. Klik **"Download CSV Template"**
3. Edit file CSV dengan data bisnis Anda

### Step 2: Upload CSV
1. Drag & drop file CSV ke upload area
2. Pastikan validasi sukses (hijau ✅)
3. Preview data terlihat benar

### Step 3: Configure
- **AI Model**: Pilih "Gemini 1.5 Flash" (recommended)
- **Output Format**: "WordPress" untuk blog
- **AI Enhancement**: Enable untuk kualitas lebih baik
- **API Key**: Kosongkan untuk demo mode

### Step 4: Generate!
1. Klik **"Start Generation"**
2. Tunggu proses selesai
3. **Download ZIP** berisi semua file

## 📁 Apa yang Anda Dapatkan?

```
bulk_content_20241201_143022.zip
├── tech_innovators.txt          # WordPress content
├── green_earth_cafe.txt         # WordPress content  
├── digital_marketing_pro.txt    # WordPress content
├── _SUMMARY.txt                 # Generation report
└── _csv_template.txt           # Template untuk next time
```

## 🔧 WordPress Integration

### Method 1: Copy-Paste (Mudah)
1. Buka WordPress admin → Posts → Add New
2. Switch ke "Text" or "Code" editor
3. Copy-paste isi file .txt
4. Publish!

### Method 2: Bulk Import (Advanced)
1. Install plugin "WP All Import"
2. Create CSV dengan post_title, post_content
3. Import all posts sekaligus

## 📊 Template yang Tersedia

| Template | Use Case | Fields Required | Best For |
|----------|----------|-----------------|----------|
| **Business Landing** | Company pages | 21 | Service businesses |
| **Product Showcase** | E-commerce | 24 | Online stores |
| **Blog Article** | Content marketing | 42 | Blogs & media |
| **Restaurant Menu** | Food business | 31 | Restaurants |
| **Real Estate** | Property listings | 35 | Real estate |
| **Event Landing** | Event promotion | 57 | Events & conferences |
| **Portfolio** | Creative showcase | 45 | Designers & agencies |

## 💡 Pro Tips

### 1. Optimize Images
- Gunakan Unsplash URLs dalam CSV
- Format: `https://images.unsplash.com/photo-ID?w=800`
- Atau upload ke WordPress Media Library dulu

### 2. AI Enhancement
- Enable untuk content yang lebih engaging
- Butuh API key untuk hasil terbaik
- Demo mode tetap menghasilkan hasil bagus

### 3. Bulk Processing
- Start dengan 5-10 rows untuk testing
- Scale up ke 100-500 rows untuk production
- Monitor rate limits jika pakai API key

### 4. Field Mapping
```csv
# Gunakan field names yang exact
business_name,tagline,description  # ✅ Correct
BusinessName,tag_line,desc         # ❌ Wrong
```

## 🚨 Common Issues & Solutions

### "CSV validation fails"
**Problem**: Missing required fields
**Solution**: Download CSV template dan pastikan header exact match

### "Generation returns demo response"
**Problem**: No API key configured  
**Solution**: Add API key di environment atau form (opsional untuk demo)

### "ZIP file empty"
**Problem**: Generation failed
**Solution**: Check error logs, coba dengan data lebih simple

### "WordPress import error"
**Problem**: Format tidak sesuai
**Solution**: Gunakan "Text" editor, bukan Visual editor

## 🔑 API Keys (Optional)

### Get Free API Keys:
- **Gemini**: [Google AI Studio](https://makersuite.google.com/app/apikey) - Free 1500 requests/day
- **Groq**: [Groq Console](https://console.groq.com/) - Free 30 req/min  
- **OpenAI**: [OpenAI Platform](https://platform.openai.com/api-keys) - $5 trial credit

### Set API Keys:
```bash
# Method 1: Environment file
echo "GEMINI_API_KEY=your_key_here" >> .env

# Method 2: Web interface
# Click "Show API Settings" di Step 3
```

## 📈 Scaling Up

### For 100+ Pages:
1. Split CSV into batches of 50
2. Generate in multiple sessions
3. Use API keys untuk best results
4. Monitor generation success rate

### For Different Industries:
1. Use appropriate templates per business type
2. Customize CSV fields untuk specific needs  
3. Mix templates untuk diverse content

## 🎉 Next Steps

1. **Test dengan sample data** - Generate 3-5 pages pertama
2. **Customize templates** - Edit HTML/CSS sesuai brand
3. **Scale production** - Generate hundreds of pages
4. **WordPress automation** - Setup bulk import workflow

## 📞 Need Help?

- 📧 **Email**: support@your-domain.com
- 💬 **GitHub Issues**: [Report bugs](https://github.com/your-username/ai-bulk-generator/issues)
- 📖 **Full Documentation**: [README.md](README.md)

---

**🚀 Ready to generate? Start dengan Business Landing template dan 5 sample businesses!**

*Happy bulk generating! 🎯*