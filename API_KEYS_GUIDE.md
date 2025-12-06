# 🔑 API Keys Setup Guide

A complete guide to getting API keys for all supported AI providers.

---

## Why Do I Need API Keys?

The Devil's Advocate uses AI models from major providers (OpenAI, Anthropic, Google) to analyze your business ideas. These providers require API keys to authenticate and bill for usage.

**You only need ONE provider to get started**, but having multiple allows you to compare results.

---

## 🟢 OpenAI (GPT-4)

### Best For
- Balanced, creative analysis
- Most widely used and documented
- Good for beginners

### Cost
- ~$0.50-1.00 per analysis
- Pay-as-you-go, charged to credit card
- No monthly minimums

### How to Get Key

1. **Sign up**
   - Go to [platform.openai.com](https://platform.openai.com)
   - Click "Sign up" or "Log in"
   - Verify your email

2. **Add payment method**
   - Go to Billing → Payment methods
   - Add a credit card
   - (Required even for small usage)

3. **Create API key**
   - Go to API keys section
   - Click "Create new secret key"
   - Name it (e.g., "DevilsAdvocate")
   - **Copy the key immediately** (starts with `sk-proj-...` or `sk-...`)
   - Store it safely (you can't see it again)

4. **Set usage limits** (Recommended)
   - Go to Billing → Usage limits
   - Set monthly limit (e.g., $10)
   - Prevents unexpected charges

### Key Format
```
sk-proj-abc123...xyz789
```
or
```
sk-abc123...xyz789
```

### Pricing Details
- GPT-4o: $2.50 per 1M input tokens, $10 per 1M output tokens
- Typical analysis: ~3,000 input + 2,000 output tokens
- Cost per analysis: ~$0.03-0.05 (model) + overhead

### Troubleshooting

**"Invalid API key"**
- Make sure you copied the entire key
- Check for extra spaces
- Regenerate if lost

**"Quota exceeded"**
- Add payment method
- Increase billing limit
- Check usage dashboard

---

## 🔵 Anthropic (Claude)

### Best For
- Deep, logical business analysis
- Understanding complex business models
- Detailed critique

### Cost
- ~$0.30-0.80 per analysis
- Pay-as-you-go
- Generally cheaper than OpenAI for same quality

### How to Get Key

1. **Sign up**
   - Go to [console.anthropic.com](https://console.anthropic.com)
   - Click "Sign up"
   - Verify your email

2. **Add payment**
   - Go to Settings → Billing
   - Add credit card

3. **Create API key**
   - Go to API Keys
   - Click "Create Key"
   - Name it
   - **Copy immediately** (starts with `sk-ant-...`)

4. **Set budget** (Recommended)
   - Go to Settings → Usage
   - Set spending limit

### Key Format
```
sk-ant-api03-abc123...xyz789
```

### Pricing Details
- Claude 3.5 Sonnet: $3 per 1M input tokens, $15 per 1M output tokens
- Typical analysis: ~3,000 input + 2,000 output tokens
- Cost per analysis: ~$0.04-0.06

### Troubleshooting

**"Authentication failed"**
- Verify key copied correctly
- Check billing is set up
- Regenerate key if needed

**"Rate limit exceeded"**
- Wait 60 seconds
- Upgrade tier if needed
- Contact support for higher limits

---

## 🟡 Google (Gemini)

### Best For
- Fast analysis
- Budget-conscious users
- Long documents (larger context window)

### Cost
- ~$0.20-0.50 per analysis
- Often has free tier
- Cheapest option

### How to Get Key

1. **Sign up**
   - Go to [ai.google.dev](https://ai.google.dev)
   - Click "Get API key in Google AI Studio"
   - Sign in with Google account

2. **Create API key**
   - Click "Create API Key"
   - Select or create a Google Cloud project
   - **Copy the key**

3. **Enable billing** (Optional)
   - Free tier available
   - For higher usage, link to Google Cloud billing

### Key Format
```
AIzaSyAbc123...Xyz789
```

### Pricing Details
- Gemini 1.5 Pro: Free tier available
- Paid: $1.25 per 1M input tokens, $5 per 1M output tokens
- Typical analysis: ~3,000 input + 2,000 output tokens
- Cost per analysis: ~$0.01-0.02 (or free!)

### Troubleshooting

**"API not enabled"**
- Go to Google Cloud Console
- Enable Generative Language API
- Wait 2-3 minutes

**"Quota exceeded"**
- Check free tier limits
- Enable billing if needed
- Wait for quota reset (daily)

---

## 💰 Cost Comparison

| Provider | Cost per Analysis | Free Tier | Best For |
|----------|-------------------|-----------|----------|
| **OpenAI** | $0.50-1.00 | No | Creative scenarios |
| **Anthropic** | $0.30-0.80 | No | Logical analysis |
| **Google** | $0.20-0.50 | Yes | Budget/Speed |

### Monthly Cost Estimates

**Light usage** (10 analyses/month):
- OpenAI: ~$5-10/month
- Anthropic: ~$3-8/month
- Google: Free - $5/month

**Medium usage** (50 analyses/month):
- OpenAI: ~$25-50/month
- Anthropic: ~$15-40/month
- Google: ~$10-25/month

**Heavy usage** (200 analyses/month):
- OpenAI: ~$100-200/month
- Anthropic: ~$60-160/month
- Google: ~$40-100/month

---

## 🔒 Security Best Practices

### ✅ DO

- Store keys in `.env` file
- Add `.env` to `.gitignore`
- Use environment variables
- Set usage limits
- Rotate keys periodically
- Keep keys private

### ❌ DON'T

- Commit keys to GitHub
- Share keys in screenshots
- Hardcode keys in files
- Use keys in public demos
- Share keys with others
- Store keys in browser

---

## 🛠️ Setting Up Keys

### Method 1: Environment File (Recommended)

Create `.env` file in project root:

```env
OPENAI_API_KEY=sk-proj-abc123...
ANTHROPIC_API_KEY=sk-ant-api03-xyz789...
GOOGLE_API_KEY=AIzaSyAbc123...
```

The app will load these automatically.

### Method 2: Environment Variables

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="sk-proj-abc123..."
```

**Mac/Linux (Terminal):**
```bash
export OPENAI_API_KEY="sk-proj-abc123..."
```

**Permanent (add to profile):**
- Windows: Edit system environment variables
- Mac/Linux: Add to `~/.bashrc` or `~/.zshrc`

### Method 3: Settings Page

1. Run the app
2. Go to Settings page
3. Enter keys in form
4. ⚠️ Keys only saved for current session

---

## 🔄 Which Provider Should I Choose?

### Start with ONE of these:

**Choose OpenAI if:**
- You want the most popular/documented option
- You value creative failure scenarios
- You're willing to pay a bit more

**Choose Anthropic if:**
- You want deep, logical analysis
- You prioritize business reasoning
- You want good value for money

**Choose Google if:**
- You're on a tight budget
- You want to try for free first
- Speed is your priority

### Pro Move: Use All Three

1. Get all three API keys
2. Run same idea through each
3. Compare what they find
4. The overlapping issues are likely real problems
5. The unique insights give different perspectives

**Cost for comparing all three:** ~$1-2 per idea

**Value:** 3x the stress-testing for < 2x the cost

---

## 🆘 Troubleshooting

### "Invalid API Key"

1. Copy key again (no spaces)
2. Check key format matches provider
3. Verify billing is set up
4. Try regenerating key

### "Quota Exceeded"

1. Check usage dashboard
2. Increase billing limit
3. Add payment method
4. Wait for quota reset (if on free tier)

### "Rate Limited"

1. Wait 60 seconds
2. Reduce analysis frequency
3. Upgrade to higher tier
4. Spread requests across providers

### Key Not Working

1. Restart app after setting key
2. Check `.env` file location (project root)
3. Verify no typos in environment variable name
4. Try Method 3 (Settings page) to test

---

## 📞 Getting Help

**OpenAI Support:**
- [help.openai.com](https://help.openai.com)
- Documentation: [platform.openai.com/docs](https://platform.openai.com/docs)

**Anthropic Support:**
- [support.anthropic.com](https://support.anthropic.com)
- Documentation: [docs.anthropic.com](https://docs.anthropic.com)

**Google Support:**
- [support.google.com](https://support.google.com)
- Documentation: [ai.google.dev/docs](https://ai.google.dev/docs)

---

## ✅ Quick Checklist

Before running your first analysis:

- [ ] Have at least ONE API key
- [ ] Key is stored in `.env` file or environment variable
- [ ] Billing is set up (if required)
- [ ] Usage limits are configured
- [ ] `.env` is in `.gitignore`
- [ ] You've tested the key (run the app)

---

**You're ready!** Run your first analysis and start stress-testing ideas. 🚀


