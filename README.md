# E-Commerce Assistant Project

A comprehensive AI-powered e-commerce analytics and management system with voice assistant capabilities.

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (optional - works with fallback responses)

### Setup Instructions

1. **Navigate to the project directory**
   ```bash
   cd E_COM_Assistant
   ```

2. **Install required packages**
   ```bash
   pip install flask flask-cors beautifulsoup4 requests numpy pandas openai python-dotenv
   ```

3. **Start the demo (works without API key)**
   ```bash
   python start_demo.py
   ```

4. **Open the frontend**
   - Open `index2.html` in your web browser
   - Go to the "AI Assistant" tab
   - Try the quick query buttons or type your own questions

### With OpenAI API Key (Optional)

1. **Set your OpenAI API key for enhanced responses**
   ```bash
   # Windows
   set OPENAI_API_KEY=your_openai_api_key_here
   
   # Linux/Mac
   export OPENAI_API_KEY=your_openai_api_key_here
   ```

2. **Start the application**
   ```bash
   python Backend_api1.py
   ```

## 🔧 Manual Setup

1. **Install dependencies**
   ```bash
   pip install flask flask-cors beautifulsoup4 requests numpy pandas openai python-dotenv
   ```

2. **Generate mock data**
   ```bash
   python generate_mock_data.py
   ```

3. **Generate competitor data**
   ```bash
   python web_scraper.py
   ```

4. **Start backend**
   ```bash
   python Backend_api1.py
   ```

5. **Open frontend**
   - Open `index2.html` in your browser

## 🎯 Features

### Fixed Issues
- ✅ **Security**: Removed hardcoded API keys and credentials
- ✅ **Performance**: Fixed inefficient data loading and caching
- ✅ **Error Handling**: Added comprehensive error handling
- ✅ **API Migration**: Replaced Google Gemini with OpenAI API
- ✅ **Path Security**: Fixed path traversal vulnerabilities
- ✅ **Data Integrity**: Fixed division by zero and null pointer issues

### Core Functionality
- 🤖 **AI Voice Assistant**: OpenAI-powered query classification
- 📊 **Financial Analytics**: Revenue, profit, and expense tracking
- 📦 **Inventory Management**: Stock alerts and restock recommendations
- 🎁 **Loyalty Rewards**: Personalized customer reward system
- 🎨 **Store Design**: AI-generated design suggestions
- 🔍 **Website Monitoring**: Problem detection and fixes
- 🏪 **Competitor Analysis**: Market data scraping and analysis

## 🛠 API Endpoints

### Main Backend (Backend_api1.py - Port 5000)
- `GET /customers` - Get all customers
- `GET /inventory` - Get inventory status
- `GET /financials` - Get financial summary
- `POST /ai/query` - AI-powered query processing

### Voice Assistant (backend3.py - Port 5000)
- `POST /ai/query` - Voice query classification and response

### Data API (backend2_api.py - Port 5000)
- `GET /ai/rewards/<customer_id>` - Get loyalty rewards
- `GET /ai/inventory_alerts` - Get inventory alerts
- `GET /ai/website_health_alerts` - Get website health status

## 📁 Project Structure

```
E_COM_Assistant/
├── data/                    # Generated data files
├── zaphire_ledger/         # Blockchain-style transaction logs
├── ai_modules.py           # Core AI functionality
├── openai_assistant.py     # OpenAI API wrapper
├── zaphire_ledger.py       # Transaction ledger system
├── web_scraper.py          # Competitor data scraping
├── Backend_api1.py         # Main API server
├── backend2_api.py         # Data API server
├── backend3.py             # Voice assistant server
├── generate_mock_data.py   # Mock data generator
├── setup_project.py        # Automated setup script
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
└── README.md              # This file
```

## 🔐 Environment Variables

Create a `.env` file or set environment variables:

```bash
OPENAI_API_KEY=your_openai_api_key_here
FLASK_DEBUG=False
FLASK_ENV=production
```

## 🧪 Testing

Test the OpenAI integration:
```bash
python gemini_replacement.py
```

Test individual components:
```bash
python -c "from ai_modules import AIModules; print('AI Modules OK')"
python -c "from zaphire_ledger import ZaphireLedger; print('Ledger OK')"
```

## 🚨 Troubleshooting

### Common Issues

1. **AI Chatbot Not Working**
   - Make sure Backend_api1.py is running
   - Check console for error messages
   - The chatbot works with fallback responses even without OpenAI API key

2. **Import Errors**
   - Install required packages: `pip install flask flask-cors beautifulsoup4 requests numpy pandas openai python-dotenv`
   - Ensure you're using Python 3.8+

3. **Data Files Missing**
   - Run `python generate_mock_data.py`
   - Run `python web_scraper.py`
   - Or use `python start_demo.py` which generates them automatically

4. **Port Already in Use**
   - Kill existing processes using port 5000
   - Or change the port in Backend_api1.py

5. **Frontend Not Loading Data**
   - Ensure backend is running on http://127.0.0.1:5000
   - Check browser console for CORS errors
   - Try refreshing the page

### Getting Help

If you encounter issues:
1. Use the demo mode: `python start_demo.py`
2. Check the console output for error messages
3. Ensure all dependencies are installed
4. Verify backend is running on port 5000
5. For enhanced AI responses, set your OpenAI API key

## 📝 License

This project is for educational and hackathon purposes.

## 🤝 Contributing

This is a hackathon project. Feel free to fork and improve!