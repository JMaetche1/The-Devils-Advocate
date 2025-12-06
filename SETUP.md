# 🚀 Setup Guide

Complete setup instructions for The Devil's Advocate.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (for cloning the repository)

## Quick Start

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Idea1
```

### 2. Create Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Keys

**Step 1:** Copy the environment template

```bash
# Windows
copy .env.example .env

# Mac/Linux
cp .env.example .env
```

**Step 2:** Get your API keys

You need **at least ONE** of these:

#### OpenAI (Recommended for beginners)

1. Go to https://platform.openai.com/api-keys
2. Sign up / Log in
3. Add payment method (required)
4. Click "Create new secret key"
5. Name it (e.g., "DevilsAdvocate")
6. Copy the key (starts with `sk-proj-` or `sk-`)
7. **Save it immediately** (you can't see it again!)

**Cost:** ~$0.03-0.05 per analysis

#### Anthropic Claude

1. Go to https://console.anthropic.com/settings/keys
2. Create account / Log in
3. Add payment method
4. Create API key
5. Copy the key (starts with `sk-ant-`)

**Cost:** ~$0.02-0.04 per analysis

#### Google Gemini

1. Go to https://aistudio.google.com/app/apikey
2. Sign in with Google account
3. Click "Get API key"
4. Create new project or select existing
5. Copy the key

**Cost:** ~$0.01-0.03 per analysis (often free tier)

#### Serper (Optional - for competitor intelligence)

1. Go to https://serper.dev
2. Sign up (FREE - 2,500 searches/month)
3. Get API key from dashboard
4. Copy the key

**Cost:** FREE (2,500 searches/month)

**Step 3:** Edit your `.env` file

Open `.env` in any text editor (Notepad, VS Code, etc.) and paste your API keys:

```env
OPENAI_API_KEY=sk-proj-your_actual_key_here
ANTHROPIC_API_KEY=
GOOGLE_API_KEY=
SERPER_API_KEY=your_serper_key_here
```

**Important:**
- Remove the placeholder text
- Don't use quotes around the keys
- No spaces around the = sign
- Leave blank the providers you're not using

### 5. Run the App

**Windows:**
```bash
run.bat
```

**Mac/Linux:**
```bash
chmod +x run.sh
./run.sh
```

**Or manually:**
```bash
streamlit run main.py
```

The app will open in your browser at: **http://localhost:8501**

## Troubleshooting

### "ModuleNotFoundError: No module named 'streamlit'"

Make sure you installed dependencies and your virtual environment is activated:

```bash
# Activate virtual environment first
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Then install
pip install -r requirements.txt
```

### "Invalid API Key" or "Authentication Error"

1. Check for extra spaces in `.env`
2. Make sure you copied the entire key (they're very long!)
3. Verify the key is active in the provider's dashboard
4. Check you added payment method (OpenAI, Anthropic require this)
5. **Restart the app** after adding keys

### "streamlit: command not found"

Make sure your virtual environment is activated:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### App won't start / crashes immediately

1. Verify Python version: `python --version` (should be 3.8+)
2. Check for error messages in terminal
3. Try deleting `data/history.db` and restarting
4. Make sure you're in the correct directory
5. Reinstall dependencies: `pip install -r requirements.txt --force-reinstall`

### Can't see .env file in File Explorer

Windows hides dot files by default:

**Option 1:** Use Notepad
```bash
notepad .env
```

**Option 2:** Show hidden files
1. Open File Explorer
2. Click View tab
3. Check "Hidden items" or "File name extensions"

**Option 3:** Use VS Code / Cursor
- Just open the file - IDEs show dot files by default

### "Quota exceeded" or "Insufficient credits"

1. Add payment method to your AI provider account
2. Check your usage dashboard
3. Increase billing limits if set too low
4. For Google Gemini, you might be over free tier limits

### Competitor Intelligence not working

This feature requires a SERPER_API_KEY:

1. Sign up at https://serper.dev (FREE)
2. Get your API key
3. Add to `.env`: `SERPER_API_KEY=your_key_here`
4. Restart the app

Without this key, you'll see: "SERPER_API_KEY not configured" when you enable competitor intel.

## Updating

To get the latest version from GitHub:

```bash
# Pull latest changes
git pull origin main

# Update dependencies (in case new ones were added)
pip install -r requirements.txt --upgrade

# Restart the app
streamlit run main.py
```

## Cost Management

### Typical Analysis Costs

**Per analysis (without competitor intel):**
- GPT-4o: $0.03-0.05
- GPT-5 models: $0.10-0.30
- Claude Sonnet: $0.02-0.04
- Gemini Pro: $0.01-0.03 (often FREE)

**With Competitor Intel:**
- Add $0.01-0.02 per analysis

### Preventing Surprise Bills

1. **Set usage limits** in each provider's dashboard:
   - OpenAI: Settings → Billing → Usage limits
   - Anthropic: Console → Settings → Usage limits
   - Google: Usually has generous free tier

2. **Start with Gemini** if you're cost-conscious (often free)

3. **Monitor usage** in the app:
   - Go to "Usage & Costs" page
   - See real-time cost tracking

4. **Test with small inputs** first

### Recommended Starting Limits

- OpenAI: $10/month
- Anthropic: $10/month  
- Google: Usually no limit needed (free tier)

## Features Overview

### New Analysis
- **Structured Form:** Guided input for comprehensive analysis
- **Quick Analysis:** Paste your idea and get instant feedback
- **Upload Document:** Analyze from PDF, DOCX, or TXT

### Include Competitor Intel
- Requires SERPER_API_KEY
- Searches web for competitor and market data
- Adds ~$0.01-0.02 to analysis cost
- Results appear in analysis output

### History
- View all past analyses
- Search by name or description
- Filter by verdict (Viable, Risky, Dead on Arrival)
- Delete old analyses

### Usage & Costs
- Track API usage and costs
- See breakdown by provider and model
- Monitor spending over time
- Real-time cost estimates

## Advanced Usage

### Running on Different Port

```bash
streamlit run main.py --server.port 8502
```

### Running on Network (so others can access)

```bash
streamlit run main.py --server.address 0.0.0.0
```

**Warning:** Anyone on your network can use your API keys! Better to have them run their own instance.

### Customizing Configuration

Edit `config.py` to change:
- Default AI provider
- Temperature settings
- Max tokens per analysis
- Scraping timeout
- Cache duration

## Security Reminders

- ✅ **Never commit** your `.env` file to git
- ✅ **Never share** your `.env` file with anyone
- ✅ **Set billing limits** in provider dashboards
- ✅ Each user should use **their own API keys**
- ✅ See [SECURITY.md](SECURITY.md) for full security guidelines

## Need Help?

1. Check this SETUP.md file
2. Read [SECURITY.md](SECURITY.md) for security questions
3. See [API_KEYS_GUIDE.md](API_KEYS_GUIDE.md) for detailed API setup
4. Read [USAGE_GUIDE.md](USAGE_GUIDE.md) for how to use features
5. Check [CHANGELOG.md](CHANGELOG.md) for recent updates
6. Open a GitHub issue for bugs or questions

## Getting Started Checklist

- [ ] Python 3.8+ installed
- [ ] Repository cloned
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created from `.env.example`
- [ ] At least one AI provider API key added to `.env`
- [ ] App runs successfully (`streamlit run main.py`)
- [ ] Tested with a sample analysis

---

**Ready to analyze!** ⚔️

Run `streamlit run main.py` and open http://localhost:8501 in your browser.


