# 🔐 Security Guidelines

## Overview

The Devil's Advocate is designed for **personal use** or **small team use** where each user sets up their own environment with their own API keys.

## ⚠️ Important Security Notes

### DO NOT Deploy As-Is to Public Server

This application is **NOT designed** for multi-user hosted deployment without significant modifications. If you want to host this as a public web service, you need to implement:

- User authentication
- Per-user API key management
- Rate limiting
- Usage quotas
- HTTPS/TLS
- Additional security controls

### Safe Usage Patterns

✅ **SAFE:**
- Running locally on your computer
- Sharing code via GitHub (API keys stay in your .env)
- Running on a private network
- Each user has their own .env file

❌ **NOT SAFE:**
- Deploying to public server with your API keys in .env
- Sharing your .env file with others
- Running without HTTPS on public internet
- Multiple users sharing the same API keys

## 🔑 API Key Security

### Setup

1. **Copy the template:**
   ```bash
   # Windows
   copy .env.example .env
   
   # Mac/Linux
   cp .env.example .env
   ```

2. **Add your API keys to `.env`:**
   - Only add keys for providers you want to use
   - At minimum, you need ONE AI provider (OpenAI, Anthropic, or Google)
   - SERPER_API_KEY is optional (only for competitor intelligence)

3. **Verify .env is in .gitignore:**
   ```bash
   git check-ignore .env
   # Should output: .env
   ```

### Protecting Your Keys

**DO:**
- ✅ Keep `.env` in `.gitignore`
- ✅ Use different API keys for different projects
- ✅ Set billing limits in provider dashboards
- ✅ Revoke and regenerate keys if exposed
- ✅ Use environment-specific keys (dev vs prod)

**DON'T:**
- ❌ Commit `.env` to git
- ❌ Share `.env` in emails, chats, screenshots
- ❌ Hardcode API keys in source code
- ❌ Use production keys for testing
- ❌ Share keys between users

### If You Accidentally Expose a Key

1. **Immediately revoke the key:**
   - OpenAI: https://platform.openai.com/api-keys
   - Anthropic: https://console.anthropic.com/settings/keys
   - Google: https://aistudio.google.com/app/apikey
   - Serper: https://serper.dev

2. **Generate a new key**

3. **Update your `.env` file**

4. **Check your usage dashboard** for unexpected charges

5. **If committed to git:** Use tools like `git-secrets` or BFG Repo-Cleaner to remove from history

## 📊 Data Privacy

### What Gets Stored Locally

The app stores the following in a local SQLite database (`data/history.db`):

- Business analyses you run
- Analysis results (verdict, critique, scenarios)
- API usage statistics (tokens, costs)
- Competitor intelligence data (if gathered)

### What Does NOT Get Stored

- ❌ API keys (only in .env file)
- ❌ Your prompts or business data is not sent anywhere except the AI provider APIs
- ❌ No telemetry or analytics sent to external servers

### Database Security

- Database is stored locally in `data/history.db`
- Included in `.gitignore` - won't be shared via git
- If sharing the project folder directly (zip, etc.), **delete the `data/` folder first**
- Contains potentially sensitive business information

## 🌐 Network Security

### Running Locally

When running locally (`streamlit run main.py`):
- Default: http://localhost:8501
- Only accessible from your computer
- No external access unless you explicitly allow it

### Running on Network

If you want others on your network to access:

```bash
streamlit run main.py --server.address 0.0.0.0
```

**Warning:** Anyone on your network can access the app and use your API keys!

**Better approach:** Each person runs their own instance with their own keys.

## 🛡️ Built-in Security Features

### Already Implemented

- ✅ API keys in environment variables (not hardcoded)
- ✅ `.env` in `.gitignore`
- ✅ Database in `.gitignore`
- ✅ No logging of sensitive data
- ✅ Retry logic with exponential backoff (prevents rate limit abuse)
- ✅ Direct API key management removed from UI (keys only from .env)

### Not Implemented (Not Needed for Personal Use)

- ❌ User authentication (everyone shares the app)
- ❌ Rate limiting (you control your own usage)
- ❌ Input validation (you trust your own input)
- ❌ HTTPS (local use only)
- ❌ Audit logging (single user)

## 📋 Pre-Deployment Checklist

Before sharing this project via GitHub:

- [ ] Verify `.env` is in `.gitignore`
- [ ] Verify `data/` is in `.gitignore`
- [ ] `.env.example` exists with placeholder values
- [ ] No test API keys in code
- [ ] README updated with setup instructions
- [ ] SECURITY.md file created
- [ ] Test `git status` - should NOT show .env or data/ files
- [ ] Review `git diff` before committing

## 🔍 Verifying Security Before Push

Run these commands before pushing to GitHub:

```bash
# Check what will be committed
git status

# Verify .env is ignored
git check-ignore .env
# Should output: .env

# Verify data folder is ignored
git check-ignore data/
# Should output: data/

# Check for any accidental API keys in code
git diff | grep -i "api.*key"
# Should be empty or only show comments

# List what will be committed
git ls-files
# Should NOT include .env or data/
```

## 🚨 Reporting Security Issues

If you find a security vulnerability in this project:

1. **DO NOT** open a public GitHub issue
2. Contact the maintainer directly
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

## 📚 Additional Resources

- [OpenAI API Best Practices](https://platform.openai.com/docs/guides/production-best-practices)
- [Anthropic Safety Best Practices](https://docs.anthropic.com/claude/docs/safety-best-practices)
- [Google AI API Key Security](https://ai.google.dev/docs/api_key)
- [OWASP API Security](https://owasp.org/www-project-api-security/)

---

**Last Updated:** December 2025  
**Version:** 1.1.0


