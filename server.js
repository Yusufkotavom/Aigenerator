const express = require('express');
const cors = require('cors');
const path = require('path');
const axios = require('axios');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('.'));

// Serve static files
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

// Proxy endpoint for Groq API
app.post('/api/groq', async (req, res) => {
    try {
        const { apiKey, ...requestData } = req.body;
        
        const response = await axios.post(
            'https://api.groq.com/openai/v1/chat/completions',
            requestData,
            {
                headers: {
                    'Authorization': `Bearer ${apiKey}`,
                    'Content-Type': 'application/json'
                }
            }
        );
        
        res.json(response.data);
    } catch (error) {
        console.error('Groq API Error:', error.response?.data || error.message);
        res.status(error.response?.status || 500).json({
            error: error.response?.data || { message: 'Internal server error' }
        });
    }
});

// Proxy endpoint for HuggingFace API
app.post('/api/huggingface', async (req, res) => {
    try {
        const { apiKey, model, ...requestData } = req.body;
        
        const response = await axios.post(
            `https://api-inference.huggingface.co/models/${model}`,
            requestData,
            {
                headers: {
                    'Authorization': `Bearer ${apiKey}`,
                    'Content-Type': 'application/json'
                }
            }
        );
        
        res.json(response.data);
    } catch (error) {
        console.error('HuggingFace API Error:', error.response?.data || error.message);
        res.status(error.response?.status || 500).json({
            error: error.response?.data || { message: 'Internal server error' }
        });
    }
});

// Proxy endpoint for Cohere API
app.post('/api/cohere', async (req, res) => {
    try {
        const { apiKey, ...requestData } = req.body;
        
        const response = await axios.post(
            'https://api.cohere.ai/v1/generate',
            requestData,
            {
                headers: {
                    'Authorization': `Bearer ${apiKey}`,
                    'Content-Type': 'application/json'
                }
            }
        );
        
        res.json(response.data);
    } catch (error) {
        console.error('Cohere API Error:', error.response?.data || error.message);
        res.status(error.response?.status || 500).json({
            error: error.response?.data || { message: 'Internal server error' }
        });
    }
});

// Proxy endpoint for Together AI
app.post('/api/together', async (req, res) => {
    try {
        const { apiKey, ...requestData } = req.body;
        
        const response = await axios.post(
            'https://api.together.xyz/inference',
            requestData,
            {
                headers: {
                    'Authorization': `Bearer ${apiKey}`,
                    'Content-Type': 'application/json'
                }
            }
        );
        
        res.json(response.data);
    } catch (error) {
        console.error('Together AI Error:', error.response?.data || error.message);
        res.status(error.response?.status || 500).json({
            error: error.response?.data || { message: 'Internal server error' }
        });
    }
});

// Health check endpoint
app.get('/api/health', (req, res) => {
    res.json({ 
        status: 'OK', 
        timestamp: new Date().toISOString(),
        uptime: process.uptime()
    });
});

// Error handling middleware
app.use((error, req, res, next) => {
    console.error('Server Error:', error);
    res.status(500).json({ 
        error: 'Internal server error',
        message: error.message 
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`
🚀 AI Generator Server is running!
==================================

Server: http://localhost:${PORT}
Health: http://localhost:${PORT}/api/health

Available API endpoints:
- POST /api/groq      - Groq Llama models
- POST /api/huggingface - HuggingFace models  
- POST /api/cohere    - Cohere models
- POST /api/together  - Together AI models

Note: Add your API keys in the browser console using:
- setApiKey('groq', 'your_key')
- setApiKey('huggingface', 'your_key')
- setApiKey('cohere', 'your_key')
- setApiKey('together', 'your_key')
    `);
});