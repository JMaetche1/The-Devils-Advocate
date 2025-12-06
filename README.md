# ⚔️ The Devil's Advocate

**Ruthless Red Team Business Analysis**

A powerful AI-powered application that stress-tests business ideas using a Pre-Mortem framework. The Devil's Advocate acts as a strategic adversary to identify fatal flaws, market blind spots, and logistical bottlenecks before you invest time and money.

---

## 🎯 The Problem

Project managers and startup founders suffer from "optimism bias." They plan for success but rarely rigorously plan for failure. Hiring a consultant to stress-test a business plan costs $5,000+.

## 💡 The Solution

An AI consultant specifically prompted to be a "Red Team" adversary. Upload your project plan, marketing strategy, or feature list, and the AI ruthlessly tears it apart following the Pre-Mortem framework.

---

## ✨ Features

- **🤖 Multi-AI Provider Support**: OpenAI, Anthropic Claude, Google Gemini
- **🎯 Latest AI Models**: Claude Opus 4.5, Gemini 2.0 Flash, and 20+ model options
- **📊 Pre-Mortem Analysis Framework**: Assumes your project fails in 12 months and works backward to find why
- **🔍 Competitor Intelligence**: Optional web scraping to gather real competitor data, pricing, and market trends
- **📚 Analysis History**: Save and search through past analyses
- **📈 Statistics Dashboard**: Track viable vs. risky vs. dead-on-arrival ideas
- **💰 API Usage & Cost Tracking**: Monitor your AI API usage and costs in CAD with per-model estimates
- **📥 Export Options**: Download analyses as Markdown or text files
- **🎨 Modern UI**: Clean, professional interface with color-coded verdicts

---

## 🔒 Security & Privacy

**This app is designed for personal use.** Your API keys and data stay on your computer.

### Quick Security Facts

- ✅ **API keys stored in `.env`** (never committed to git)
- ✅ **Data stored locally** in SQLite (not sent anywhere)
- ✅ **No telemetry or external analytics**
- ✅ **Your business data only goes to AI provider APIs** (OpenAI/Anthropic/Google)
- ✅ **Open source** - inspect the code yourself

### For Collaborators

- Each person needs their own API keys
- Don't share your `.env` file
- See [SETUP.md](SETUP.md) for installation instructions
- See [SECURITY.md](SECURITY.md) for full security guidelines

### ⚠️ Important

**DO NOT deploy to public server without additional security measures!**

This application is designed for personal/local use. If you want to host as a multi-user service, you'll need to implement:
- User authentication
- Per-user API key management  
- Rate limiting and usage quotas
- HTTPS/TLS encryption
- Additional security controls

---

## 🏗️ Analysis Framework

Every analysis follows "The Auditor" persona and provides:

### 1. **THE VERDICT**
One of three outcomes: `VIABLE`, `RISKY`, or `DEAD ON ARRIVAL`

### 2. **THE "KILL SHOT"** 
The single weakest link—the one factor that, if it breaks, destroys the entire project

### 3. **SCENARIO SIMULATION** (The Wargame)
- **Scenario A (The Market)**: Customers don't care or pay too little
- **Scenario B (The Operations)**: Logistics break or costs explode  
- **Scenario C (The Black Swan)**: A competitor or regulation kills the model

### 4. **THE "STEEL MAN" ARGUMENT**
The exact narrow path you must take to prove The Auditor wrong

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- At least one AI provider API key (OpenAI, Anthropic, or Google)
- Git (for cloning the repository)

### Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd Idea1
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up your API keys**

Copy the environment template:
```bash
# Windows
copy .env.example .env

# Mac/Linux
cp .env.example .env
```

Then edit `.env` and add your API keys:
```env
OPENAI_API_KEY=sk-proj-your_actual_key_here
ANTHROPIC_API_KEY=
GOOGLE_API_KEY=
SERPER_API_KEY=
```

**Need help getting API keys?** See [SETUP.md](SETUP.md) for detailed instructions.

4. **Run the app**
```bash
# Windows
run.bat

# Mac/Linux
./run.sh

# Or manually
streamlit run main.py
```

The app will open in your browser at http://localhost:8501

---

## 🎮 Usage

### Start the Application

```bash
streamlit run main.py
```

The application will open in your browser at `http://localhost:8501`

### Three Input Modes

1. **Structured Form**: Provide detailed information about your business
   - Business name/concept
   - Target market
   - Revenue model
   - Key assumptions
   - Competitive landscape

2. **Quick Analysis**: Just paste your elevator pitch and get instant feedback

3. **Upload Document**: Upload PDF, DOCX, or TXT files containing your business plan

### Run Analysis

1. Fill in your business information
2. Select your preferred AI provider
3. Optionally enable competitor intelligence gathering
4. Click "⚔️ ANALYZE"
5. Review the ruthless critique
6. Save to history or export as needed

---

## 📁 Project Structure

```
devils-advocate/
├── main.py                      # Streamlit application entry point
├── config.py                    # Configuration management
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── data/
│   └── history.db              # SQLite database (auto-created)
├── core/
│   ├── auditor.py              # Main analysis engine
│   ├── ai_providers.py         # Multi-provider AI interface
│   └── prompts.py              # The Auditor system prompt
├── analysis/
│   ├── framework.py            # Pre-Mortem framework implementation
│   └── report_generator.py    # Report formatting
├── intelligence/
│   ├── web_scraper.py          # Competitor data scraping
│   ├── market_research.py      # Market intelligence
│   └── sources.py              # Data source configurations
├── database/
│   ├── models.py               # Database models
│   └── repository.py           # Database operations
└── ui/
    ├── components.py           # Reusable UI components
    └── styles.py               # Custom CSS styling
```

---

## 🔧 Configuration

### Environment Variables

All configuration is done via environment variables in `.env`:

- `OPENAI_API_KEY`: Your OpenAI API key
- `ANTHROPIC_API_KEY`: Your Anthropic API key  
- `GOOGLE_API_KEY`: Your Google AI API key
- `SERPER_API_KEY`: (Optional) Serper API for Google search

### Advanced Settings

Edit `config.py` to adjust:

- `DEFAULT_AI_PROVIDER`: Default provider to use
- `DEFAULT_TEMPERATURE`: AI creativity level (0.0-1.0)
- `DEFAULT_MAX_TOKENS`: Maximum response length
- `SCRAPING_ENABLED`: Enable/disable web scraping
- `SCRAPING_TIMEOUT`: Web request timeout in seconds
- `CACHE_DURATION`: How long to cache scraped data

---

## 💻 Technical Details

### AI Providers

**OpenAI**
- Models: GPT-4o, GPT-4 Turbo, GPT-4
- Best for: Balanced analysis with creative scenarios

**Anthropic Claude**
- Models: Claude 3.5 Sonnet, Claude 3 Opus
- Best for: Deep, nuanced business analysis

**Google Gemini**
- Models: Gemini 1.5 Pro, Gemini 1.5 Flash
- Best for: Fast analysis with good context understanding

### Database

- **SQLite**: Local database for history storage
- **Schema**: Stores full analysis, business data, and metadata
- **Location**: `data/history.db`

### Web Scraping

- **Basic Mode**: Uses Serper API for Google searches
- **Advanced Mode**: Can use Playwright for dynamic content
- **Rate Limiting**: Built-in delays to respect servers
- **Caching**: 24-hour cache to avoid repeated requests

---

## 🎨 UI/UX Features

- **Color-Coded Verdicts**: Green (Viable), Yellow (Risky), Red (Dead on Arrival)
- **Expandable Sections**: Clean, scannable analysis layout
- **Dark Theme**: Professional, modern interface
- **Responsive Design**: Works on desktop and tablet
- **Loading Animations**: Engaging feedback during analysis
- **Search & Filter**: Easy navigation through history

---

## 🔒 Security & Privacy

- **API Keys**: Stored in environment variables, never committed to code
- **Local Storage**: All data stored locally in SQLite
- **No Telemetry**: No data sent to external services except chosen AI provider
- **Session Keys**: Temporary API keys only exist for current session

---

## 🤝 Contributing

This is an open project. Contributions welcome for:

- Additional AI providers
- Enhanced web scraping sources
- New analysis frameworks
- UI/UX improvements
- Documentation

---

## 📝 License

This project is provided as-is for educational and commercial use.

---

## 🙏 Acknowledgments

Built with:
- [Streamlit](https://streamlit.io/) - UI framework
- [OpenAI](https://openai.com/) - GPT models
- [Anthropic](https://anthropic.com/) - Claude models
- [Google AI](https://ai.google/) - Gemini models
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database ORM
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - Web scraping

---

## 📞 Support

For issues, questions, or suggestions, please open an issue on GitHub.

**Additional Guides:**
- `USAGE_TRACKING.md` - Complete guide to API usage and cost tracking
- `USAGE_GUIDE.md` - Best practices and tips
- `API_KEYS_GUIDE.md` - How to get API keys
- `EXAMPLES.md` - Real-world analysis examples

---

## 🚨 Disclaimer

The Devil's Advocate provides analysis based on AI models. While designed to be thorough and critical, it should not replace professional business consulting, legal advice, or market research. Always conduct your own due diligence before making business decisions.

---

**Remember**: The goal is not to kill your dreams, but to make them bulletproof. 🛡️

