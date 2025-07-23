function aiGenerator() {
    return {
        // State
        selectedModel: 'groq-llama',
        prompt: '',
        response: '',
        isLoading: false,
        showToast: false,
        toastMessage: '',
        history: JSON.parse(localStorage.getItem('aiHistory') || '[]'),
        
        // Settings
        settings: {
            temperature: 0.7,
            maxTokens: 500,
            topP: 0.9
        },

        // AI Models with free tiers
        models: [
            {
                id: 'groq-llama',
                name: 'Llama 3.1 70B',
                description: 'Fast inference with Groq',
                provider: 'Groq',
                type: 'Chat Completion',
                limit: 'Free tier available',
                icon: 'fas fa-rocket',
                color: 'bg-orange-500',
                endpoint: 'https://api.groq.com/openai/v1/chat/completions',
                model: 'llama-3.1-70b-versatile'
            },
            {
                id: 'huggingface',
                name: 'HuggingFace Inference',
                description: 'Various models via HF',
                provider: 'HuggingFace',
                type: 'Text Generation',
                limit: 'Rate limited free',
                icon: 'fas fa-brain',
                color: 'bg-yellow-500',
                endpoint: 'https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium',
                model: 'microsoft/DialoGPT-medium'
            },
            {
                id: 'cohere',
                name: 'Cohere Command',
                description: 'Command model by Cohere',
                provider: 'Cohere',
                type: 'Chat',
                limit: 'Free trial available',
                icon: 'fas fa-comments',
                color: 'bg-blue-500',
                endpoint: 'https://api.cohere.ai/v1/generate',
                model: 'command'
            },
            {
                id: 'together',
                name: 'Together AI',
                description: 'Open source models',
                provider: 'Together',
                type: 'Completion',
                limit: 'Free credits',
                icon: 'fas fa-users',
                color: 'bg-green-500',
                endpoint: 'https://api.together.xyz/inference',
                model: 'togethercomputer/llama-2-7b-chat'
            }
        ],

        // Prompt templates
        promptTemplates: [
            {
                id: 'creative',
                name: 'Creative Writing',
                prompt: 'Write a creative story about a mysterious discovery in an ancient library. Make it engaging and imaginative.'
            },
            {
                id: 'explain',
                name: 'Explain Concept',
                prompt: 'Explain the concept of artificial intelligence in simple terms that a 10-year-old could understand.'
            },
            {
                id: 'code',
                name: 'Code Helper',
                prompt: 'Write a Python function that calculates the factorial of a number. Include comments and error handling.'
            },
            {
                id: 'business',
                name: 'Business Ideas',
                prompt: 'Generate 5 innovative business ideas for the year 2024. Focus on sustainability and technology.'
            },
            {
                id: 'translate',
                name: 'Translation',
                prompt: 'Translate the following text to Indonesian: "Artificial intelligence is revolutionizing the way we work and live."'
            }
        ],

        // Initialize
        init() {
            // Load saved settings
            const savedSettings = localStorage.getItem('aiSettings');
            if (savedSettings) {
                this.settings = { ...this.settings, ...JSON.parse(savedSettings) };
            }
            
            // Load selected model
            const savedModel = localStorage.getItem('selectedModel');
            if (savedModel) {
                this.selectedModel = savedModel;
            }
        },

        // Generate AI response
        async generateResponse() {
            if (!this.prompt.trim()) return;

            this.isLoading = true;
            this.response = '';

            try {
                const currentModel = this.models.find(m => m.id === this.selectedModel);
                let response;

                switch (this.selectedModel) {
                    case 'groq-llama':
                        response = await this.callGroq(currentModel);
                        break;
                    case 'huggingface':
                        response = await this.callHuggingFace(currentModel);
                        break;
                    case 'cohere':
                        response = await this.callCohere(currentModel);
                        break;
                    case 'together':
                        response = await this.callTogether(currentModel);
                        break;
                    default:
                        response = await this.simulateResponse();
                }

                this.response = response;
                this.addToHistory(currentModel.name, this.prompt, response);
                this.showToastMessage('Response generated successfully!');

            } catch (error) {
                console.error('Error generating response:', error);
                this.response = `Error: ${error.message}. Please check your API keys and try again.`;
                this.showToastMessage('Error generating response');
            } finally {
                this.isLoading = false;
            }
        },

        // Groq API call
        async callGroq(model) {
            const apiKey = localStorage.getItem('groq_api_key');
            if (!apiKey) {
                throw new Error('Groq API key not found. Please add it in browser console: localStorage.setItem("groq_api_key", "your_key")');
            }

            const response = await fetch(model.endpoint, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${apiKey}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    model: model.model,
                    messages: [
                        {
                            role: 'user',
                            content: this.prompt
                        }
                    ],
                    temperature: parseFloat(this.settings.temperature),
                    max_tokens: parseInt(this.settings.maxTokens),
                    top_p: parseFloat(this.settings.topP)
                })
            });

            if (!response.ok) {
                throw new Error(`Groq API error: ${response.status}`);
            }

            const data = await response.json();
            return data.choices[0].message.content;
        },

        // HuggingFace API call
        async callHuggingFace(model) {
            const apiKey = localStorage.getItem('huggingface_api_key');
            if (!apiKey) {
                throw new Error('HuggingFace API key not found. Please add it in browser console: localStorage.setItem("huggingface_api_key", "your_key")');
            }

            const response = await fetch(model.endpoint, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${apiKey}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    inputs: this.prompt,
                    parameters: {
                        temperature: parseFloat(this.settings.temperature),
                        max_new_tokens: parseInt(this.settings.maxTokens),
                        top_p: parseFloat(this.settings.topP)
                    }
                })
            });

            if (!response.ok) {
                throw new Error(`HuggingFace API error: ${response.status}`);
            }

            const data = await response.json();
            return Array.isArray(data) ? data[0].generated_text : data.generated_text;
        },

        // Cohere API call
        async callCohere(model) {
            const apiKey = localStorage.getItem('cohere_api_key');
            if (!apiKey) {
                throw new Error('Cohere API key not found. Please add it in browser console: localStorage.setItem("cohere_api_key", "your_key")');
            }

            const response = await fetch(model.endpoint, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${apiKey}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    model: model.model,
                    prompt: this.prompt,
                    temperature: parseFloat(this.settings.temperature),
                    max_tokens: parseInt(this.settings.maxTokens),
                    p: parseFloat(this.settings.topP)
                })
            });

            if (!response.ok) {
                throw new Error(`Cohere API error: ${response.status}`);
            }

            const data = await response.json();
            return data.generations[0].text;
        },

        // Together AI API call
        async callTogether(model) {
            const apiKey = localStorage.getItem('together_api_key');
            if (!apiKey) {
                throw new Error('Together API key not found. Please add it in browser console: localStorage.setItem("together_api_key", "your_key")');
            }

            const response = await fetch(model.endpoint, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${apiKey}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    model: model.model,
                    prompt: this.prompt,
                    temperature: parseFloat(this.settings.temperature),
                    max_tokens: parseInt(this.settings.maxTokens),
                    top_p: parseFloat(this.settings.topP)
                })
            });

            if (!response.ok) {
                throw new Error(`Together API error: ${response.status}`);
            }

            const data = await response.json();
            return data.output.choices[0].text;
        },

        // Simulate response (fallback)
        async simulateResponse() {
            // Simulate API delay
            await new Promise(resolve => setTimeout(resolve, 2000));
            
            const responses = [
                "I'm a demo response! To use real AI models, please configure your API keys in the browser console.\n\nFor example:\n- localStorage.setItem('groq_api_key', 'your_groq_key')\n- localStorage.setItem('huggingface_api_key', 'your_hf_key')\n\nThen refresh and try again!",
                "This is a simulated AI response. The interface is fully functional, but you'll need to add your API keys to connect to real AI models.\n\nCheck the browser console for instructions on how to add API keys.",
                "Demo mode active! Your prompt was: '" + this.prompt.substring(0, 50) + "...'\n\nTo enable real AI responses, add your API keys using localStorage in the browser console."
            ];
            
            return responses[Math.floor(Math.random() * responses.length)];
        },

        // Copy to clipboard
        async copyToClipboard(text) {
            try {
                await navigator.clipboard.writeText(text);
                this.showToastMessage('Copied to clipboard!');
            } catch (err) {
                console.error('Failed to copy:', err);
                // Fallback for older browsers
                const textArea = document.createElement('textarea');
                textArea.value = text;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
                this.showToastMessage('Copied to clipboard!');
            }
        },

        // Show toast message
        showToastMessage(message) {
            this.toastMessage = message;
            this.showToast = true;
            setTimeout(() => {
                this.showToast = false;
            }, 3000);
        },

        // Add to history
        addToHistory(model, prompt, response) {
            const historyItem = {
                model,
                prompt,
                response,
                timestamp: new Date().toLocaleString()
            };
            
            this.history.unshift(historyItem);
            
            // Keep only last 20 items
            if (this.history.length > 20) {
                this.history = this.history.slice(0, 20);
            }
            
            localStorage.setItem('aiHistory', JSON.stringify(this.history));
        },

        // Load from history
        loadFromHistory(item) {
            this.prompt = item.prompt;
            this.response = item.response;
            this.showToastMessage('Loaded from history');
        },

        // Watch for changes
        $watch: {
            selectedModel(value) {
                localStorage.setItem('selectedModel', value);
            },
            settings: {
                handler(value) {
                    localStorage.setItem('aiSettings', JSON.stringify(value));
                },
                deep: true
            }
        }
    }
}

// Helper functions for API key management
window.setApiKey = function(provider, key) {
    localStorage.setItem(`${provider}_api_key`, key);
    console.log(`${provider} API key saved!`);
};

window.getApiKey = function(provider) {
    return localStorage.getItem(`${provider}_api_key`);
};

window.clearApiKeys = function() {
    const keys = ['groq_api_key', 'huggingface_api_key', 'cohere_api_key', 'together_api_key'];
    keys.forEach(key => localStorage.removeItem(key));
    console.log('All API keys cleared!');
};

// Console instructions
console.log(`
🤖 AI Generator - API Key Setup Instructions
============================================

To use real AI models, set your API keys:

1. Groq (Llama 3.1 70B - Free tier):
   setApiKey('groq', 'your_groq_api_key_here')
   Get free key: https://console.groq.com/

2. HuggingFace (Free tier):
   setApiKey('huggingface', 'your_hf_token_here')
   Get free key: https://huggingface.co/settings/tokens

3. Cohere (Free trial):
   setApiKey('cohere', 'your_cohere_key_here')
   Get free key: https://dashboard.cohere.ai/

4. Together AI (Free credits):
   setApiKey('together', 'your_together_key_here')
   Get free key: https://api.together.xyz/

Other commands:
- getApiKey('provider') - Check if key exists
- clearApiKeys() - Remove all keys

⚠️  Note: Keys are stored in localStorage (client-side only)
`);