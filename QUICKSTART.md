# ⚡ Quick Start Guide

Get The Devil's Advocate running in 5 minutes.

---

## 1️⃣ Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Expected time:** 2-3 minutes

---

## 2️⃣ Get an API Key

You need AT LEAST ONE of these:

### Option A: OpenAI (Recommended for First-Timers)

1. Go to [platform.openai.com](https://platform.openai.com)
2. Sign up / Log in
3. Go to API Keys
4. Create new key
5. Copy it (starts with `sk-...`)

**Cost:** ~$0.50-1.00 per analysis

### Option B: Anthropic Claude

1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Sign up / Log in  
3. Get API key
4. Copy it (starts with `sk-ant-...`)

**Cost:** ~$0.30-0.80 per analysis

### Option C: Google Gemini

1. Go to [ai.google.dev](https://ai.google.dev)
2. Get API key
3. Copy it

**Cost:** ~$0.20-0.50 per analysis (often free tier available)

---

## 3️⃣ Set Your API Key

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your_key_here"
```

**Mac/Linux (Terminal):**
```bash
export OPENAI_API_KEY="your_key_here"
```

**Or create a `.env` file:**
```env
OPENAI_API_KEY=your_key_here
```

---

## 4️⃣ Launch the App

```bash
streamlit run main.py
```

Your browser should open automatically to `http://localhost:8501`

---

## 5️⃣ Run Your First Analysis

### Try This Example:

**Mode:** Quick Analysis

**Paste this:**
```
A mobile app that uses AI to generate personalized workout plans based on 
your fitness level, available equipment, and goals. Users pay $9.99/month 
for unlimited plans and progress tracking. Target market is people who 
can't afford personal trainers ($50-100/session) but want better results 
than free YouTube videos. Competition includes apps like Nike Training Club 
(free) and Future ($150/month with human coaches). Our advantage is AI 
personalization at an affordable price point.
```

**Click:** ⚔️ ANALYZE

**Wait:** 30-60 seconds

**Result:** You'll see a ruthless analysis with verdict, kill shot, scenarios, and path forward.

---

## ✅ You're Done!

Now try with your own business idea.

---

## 🆘 Troubleshooting

### "API key not configured"
- Make sure you set the environment variable
- Or enter it in Settings page
- Restart terminal after setting

### "Module not found"
- Run `pip install -r requirements.txt` again
- Make sure you're in the project directory

### "Port 8501 already in use"
- Another Streamlit app is running
- Kill it or use: `streamlit run main.py --server.port 8502`

### Still stuck?
- Check full README.md
- Check USAGE_GUIDE.md
- Verify Python version: `python --version` (need 3.8+)

---

## 🎯 Next Steps

1. **Read the Examples**: Check `EXAMPLES.md` for real analyses
2. **Learn Best Practices**: See `USAGE_GUIDE.md`
3. **Try All Providers**: Compare OpenAI vs Claude vs Gemini
4. **Enable Intel**: Turn on "Include Competitor Intel" for deeper analysis
5. **Save History**: Build up a library of analyses

---

**Pro Tip:** Run the same idea through all three AI providers and compare results. They'll catch different issues!


