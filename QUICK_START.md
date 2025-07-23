# 🚀 Quick Start Guide

**Get your AI Generator running in 2 minutes!**

## 🎯 Method 1: One-Click Start (Recommended)

### Linux/Mac:
```bash
./start.sh
```

### Windows:
```batch
start.bat
```

## 🎯 Method 2: Manual Start

### With Node.js (Full Features):
```bash
npm install
npm start
```
Open: http://localhost:3000

### With Python (Frontend Only):
```bash
python3 -m http.server 8000
```
Open: http://localhost:8000

## 🔑 Get Free API Keys (5 minutes)

### 1. Groq - FASTEST & FREE
1. Go to: https://console.groq.com/
2. Sign up with Google/GitHub
3. Copy API key
4. In browser console: `setApiKey('groq', 'gsk_your_key')`

### 2. HuggingFace - FREE
1. Go to: https://huggingface.co/settings/tokens
2. Create new token
3. In browser console: `setApiKey('huggingface', 'hf_your_token')`

## ✅ Test Your Setup

1. Open the AI Generator
2. Type: "Write a short poem about AI"
3. Click "Generate AI Response"
4. 🎉 You're ready!

## 🆘 Need Help?

- **API Key Error?** Check browser console for instructions
- **CORS Error?** Use Node.js server (Method 1)
- **Port Busy?** Kill process: `lsof -ti:3000 | xargs kill -9`

## 🎨 Features to Try

- ✨ Use prompt templates
- 🎛️ Adjust temperature/tokens
- 📚 Check your history
- 📋 Copy responses
- 🔄 Switch between AI models

---

**🎉 That's it! You're now an AI power user!**