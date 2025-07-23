# AI Generator - Multi Model Platform

🤖 **AI Generator modern dengan beragam model AI gratis** menggunakan HTML, Tailwind CSS, dan Alpine.js.

![AI Generator Screenshot](https://via.placeholder.com/800x400/8b5cf6/ffffff?text=AI+Generator+Interface)

## ✨ Fitur Utama

- 🎯 **Multi-Model Support**: Groq, HuggingFace, Cohere, Together AI
- 🆓 **Free Tier Focus**: Semua model mendukung tier gratis
- 🎨 **Modern UI**: Glassmorphism dengan Tailwind CSS
- 📱 **Responsive Design**: Optimal di desktop dan mobile
- 💾 **Local Storage**: History dan settings tersimpan
- 🔧 **Customizable**: Temperature, tokens, dan parameter lainnya
- 📋 **Template Prompts**: Prompt siap pakai untuk berbagai kebutuhan
- 📊 **Real-time Response**: Interface yang responsif dan interaktif

## 🚀 Model AI yang Didukung

| Provider | Model | Type | Free Tier |
|----------|-------|------|-----------|
| **Groq** | Llama 3.1 70B | Chat Completion | ✅ Fast inference |
| **HuggingFace** | Various Models | Text Generation | ✅ Rate limited |
| **Cohere** | Command | Chat | ✅ Free trial |
| **Together AI** | Llama 2 7B | Completion | ✅ Free credits |

## 📋 Prerequisites

### Opsi 1: Menggunakan Node.js (Recommended)
```bash
node --version  # v14.0.0 atau lebih baru
npm --version   # v6.0.0 atau lebih baru
```

### Opsi 2: Python (Simple Server)
```bash
python3 --version  # v3.6 atau lebih baru
```

### Opsi 3: PHP (Alternative)
```bash
php --version  # v7.0 atau lebih baru
```

## 🛠️ Instalasi

### Metode 1: Node.js Server (Full Features)

1. **Clone repository:**
```bash
git clone https://github.com/your-username/ai-generator.git
cd ai-generator
```

2. **Install dependencies:**
```bash
npm install
```

3. **Jalankan server:**
```bash
npm start
# atau untuk development:
npm run dev
```

4. **Buka browser:** `http://localhost:3000`

### Metode 2: Python Server (Frontend Only)

1. **Download dan extract files**
2. **Jalankan server:**
```bash
python3 -m http.server 8000
```
3. **Buka browser:** `http://localhost:8000`

### Metode 3: PHP Server (Alternative)

1. **Download dan extract files**
2. **Jalankan server:**
```bash
php -S localhost:8000
```
3. **Buka browser:** `http://localhost:8000`

## 🔑 Setup API Keys

### 1. Groq (Llama 3.1 70B) - GRATIS
- Daftar di: https://console.groq.com/
- Dapatkan API key gratis
- Masukkan di browser console:
```javascript
setApiKey('groq', 'gsk_your_groq_api_key_here')
```

### 2. HuggingFace - GRATIS
- Daftar di: https://huggingface.co/
- Buat token di: https://huggingface.co/settings/tokens
- Masukkan di browser console:
```javascript
setApiKey('huggingface', 'hf_your_token_here')
```

### 3. Cohere - FREE TRIAL
- Daftar di: https://dashboard.cohere.ai/
- Dapatkan API key trial gratis
- Masukkan di browser console:
```javascript
setApiKey('cohere', 'your_cohere_key_here')
```

### 4. Together AI - FREE CREDITS
- Daftar di: https://api.together.xyz/
- Dapatkan $5 credit gratis
- Masukkan di browser console:
```javascript
setApiKey('together', 'your_together_key_here')
```

## 💡 Cara Penggunaan

1. **Pilih Model AI** dari card yang tersedia
2. **Masukkan Prompt** atau gunakan template yang disediakan
3. **Atur Parameter** (temperature, max tokens, top-p)
4. **Klik Generate** untuk mendapatkan response AI
5. **Copy/Save** hasil sesuai kebutuhan

### Template Prompts

- **Creative Writing**: Menulis cerita kreatif
- **Explain Concept**: Menjelaskan konsep kompleks
- **Code Helper**: Bantuan coding dan programming
- **Business Ideas**: Generasi ide bisnis
- **Translation**: Terjemahan bahasa

## 🎨 Kustomisasi UI

### Mengubah Theme Colors
Edit `tailwind.config` di `index.html`:
```javascript
tailwind.config = {
  theme: {
    extend: {
      colors: {
        primary: '#your-color',
        secondary: '#your-color'
      }
    }
  }
}
```

### Menambah CSS Custom
Edit file `css/style.css` untuk styling tambahan.

## 📱 Fitur Mobile

- ✅ Responsive design
- ✅ Touch-friendly interface
- ✅ Optimized untuk smartphone
- ✅ PWA ready (bisa diinstall)

## 🔧 Advanced Configuration

### Environment Variables (Node.js)
Buat file `.env`:
```env
PORT=3000
NODE_ENV=production
```

### Proxy Settings
Jika ada CORS issues, gunakan server Node.js yang sudah include proxy.

### Rate Limiting
Beberapa API memiliki rate limit:
- Groq: ~30 requests/minute (free)
- HuggingFace: ~1000 requests/month (free)
- Cohere: Berdasarkan trial limit
- Together: Berdasarkan credit

## 🛡️ Security Notes

- ✅ API keys disimpan di localStorage (client-side only)
- ✅ Tidak ada data yang dikirim ke server eksternal
- ✅ CORS protection untuk API calls
- ⚠️ Gunakan HTTPS di production
- ⚠️ Jangan share API keys di public

## 🚨 Troubleshooting

### Error: "API key not found"
```javascript
// Check if key exists:
getApiKey('groq')
// Set key if missing:
setApiKey('groq', 'your_key_here')
```

### Error: "CORS blocked"
- Gunakan Node.js server (npm start)
- Atau install browser extension untuk disable CORS

### Error: "Rate limit exceeded"
- Tunggu beberapa menit
- Atau ganti ke provider lain

### Performance Issues
- Kurangi max_tokens setting
- Gunakan model yang lebih kecil
- Check internet connection

## 🤝 Contributing

1. Fork repository
2. Buat feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push branch: `git push origin feature/amazing-feature`
5. Open Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) - Fast inference
- [HuggingFace](https://huggingface.co/) - Model hosting
- [Cohere](https://cohere.ai/) - Language models
- [Together AI](https://together.ai/) - Open source models
- [Tailwind CSS](https://tailwindcss.com/) - Styling
- [Alpine.js](https://alpinejs.dev/) - Reactivity

## 📞 Support

- 🐛 Bug reports: [Issues](https://github.com/your-username/ai-generator/issues)
- 💬 Discussions: [Discussions](https://github.com/your-username/ai-generator/discussions)
- 📧 Email: support@your-domain.com

---

**Made with ❤️ in Indonesia**

⭐ Jika project ini membantu, jangan lupa kasih star ya!