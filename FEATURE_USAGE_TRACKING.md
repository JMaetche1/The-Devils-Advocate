# 🎉 New Feature: API Usage & Cost Tracking

**Version 1.1.0** - Added December 6, 2024

---

## 📋 Overview

The Devil's Advocate now includes **comprehensive API usage and cost tracking** with all costs displayed in **Canadian Dollars (CAD)**.

This feature helps you:
- ✅ Monitor your AI API spending in real-time
- ✅ Understand which providers are most cost-effective
- ✅ Track token usage across all analyses
- ✅ Set and monitor budget limits
- ✅ Optimize costs by choosing cheaper providers

---

## 🎯 What's New

### 1. Usage Dashboard (New Page)

A dedicated "**Usage & Costs**" page showing:

```
📊 Total Metrics:
- Total API Calls: 25
- Total Tokens: 125,450
- Cost (USD): $9.23
- Cost (CAD): $12.55

📈 By Provider:
🟢 OpenAI: 15 calls, $8.50 CAD
🔵 Anthropic: 7 calls, $3.20 CAD
🟡 Google: 3 calls, $0.85 CAD

📝 Recent API Calls:
[Table showing last 20 calls with timestamps, models, tokens, costs]

💵 Cost Estimator:
Plan 50 analyses with Anthropic = $27.50 CAD estimated
```

### 2. Sidebar Quick Stats

Your sidebar now shows:
```
💰 Session Costs
$12.55 CAD
25 API calls
⚠️ Check Usage & Costs page
```

### 3. Per-Analysis Metrics

After each analysis, you'll see:
```
Tokens Used: 4,523
Input Tokens: 2,845
Output Tokens: 1,678
Cost (CAD): $0.52
```

### 4. Automatic Tracking

Every API call is automatically tracked:
- ✅ Token counts from provider
- ✅ Real-time cost calculation
- ✅ Saved to local database
- ✅ No configuration needed

### 5. Cost Alerts

Smart warnings when you exceed thresholds:
- **$5 CAD**: Warning in sidebar
- **$10 CAD**: Alert on Usage page with cost-saving tips

---

## 💰 Pricing Information

All costs are calculated using current provider pricing and converted to CAD at 1.36 exchange rate.

### OpenAI GPT-4o
- **$2.50 USD** per 1M input tokens
- **$10.00 USD** per 1M output tokens
- **~$0.50-1.00 CAD** per analysis

### Anthropic Claude 3.5 Sonnet
- **$3.00 USD** per 1M input tokens
- **$15.00 USD** per 1M output tokens  
- **~$0.30-0.80 CAD** per analysis

### Google Gemini 1.5 Pro
- **$1.25 USD** per 1M input tokens
- **$5.00 USD** per 1M output tokens
- **~$0.20-0.50 CAD** per analysis
- Often has **free tier** available

---

## 🚀 How to Use

### View Your Usage

**Option 1: Sidebar**
1. Look at sidebar while using the app
2. See total cost (CAD) and call count
3. Get warnings if usage is high

**Option 2: Usage & Costs Page**
1. Click "Usage & Costs" in navigation
2. Select time period (All Time, Last 7 Days, etc.)
3. View detailed breakdown

**Option 3: Per-Analysis**
- After each analysis, see token usage and cost
- Displayed right above the analysis results

### Estimate Costs

Before running multiple analyses:

1. Go to Usage & Costs page
2. Scroll to "Cost Estimator"
3. Enter number of analyses
4. Select provider
5. See estimated total cost

**Example:**
```
20 analyses with Google Gemini
= 20 × $0.35 CAD
= $7.00 CAD total
```

### Compare Providers

See which provider is cheapest for your use case:

1. Run same idea through all 3 providers
2. Check Usage & Costs breakdown
3. See actual cost per provider
4. Choose best value for future analyses

---

## 📊 Cost Comparison Example

**Scenario:** 50 analyses per month

| Provider | Cost per Analysis | Monthly Total | Annual Total |
|----------|------------------|---------------|--------------|
| **Google** | $0.35 CAD | $17.50 CAD | $210 CAD |
| **Anthropic** | $0.55 CAD | $27.50 CAD | $330 CAD |
| **OpenAI** | $0.75 CAD | $37.50 CAD | $450 CAD |

**Savings by using Google instead of OpenAI:** 
- $20/month = **$240/year** 💰

---

## 🎓 Cost Optimization Tips

### 1. Choose the Right Provider

- **Testing ideas quickly?** → Google Gemini (cheapest)
- **Need deep analysis?** → Anthropic Claude (best value)
- **Want creative scenarios?** → OpenAI GPT-4 (premium)

### 2. Use Quick Analysis Mode

- Shorter inputs = fewer tokens = lower cost
- Save 30-50% vs uploading full documents

### 3. Disable Intelligence When Not Needed

- Competitor Intelligence adds ~1,500 input tokens
- Adds ~$0.15-0.30 to each analysis
- Only enable when you need market data

### 4. Batch Your Analyses

- Run multiple ideas in one session
- Compare all variations at once
- More efficient than one-at-a-time

---

## 🔒 Privacy & Data

### What's Stored

- Timestamp of each API call
- Provider and model name
- Token counts (input/output)
- Calculated costs (USD/CAD)

### Where It's Stored

- **Local SQLite database** only
- File: `data/history.db`
- Never sent to external servers
- You control the data

### Can I Delete It?

Yes! The data is yours:
- Delete specific records from database
- Clear old records (90+ days)
- Delete entire database file if desired

---

## 📈 Dashboard Features

### Main Metrics

- **Total API Calls**: Count of all analyses
- **Total Tokens**: Combined input + output
- **Cost (USD)**: For reference
- **Cost (CAD)**: Your actual spending

### Provider Breakdown

For each AI provider used:
- Number of calls made
- Total tokens consumed
- Total cost in CAD

### Recent Usage Table

Last 20 API calls showing:
- Exact timestamp
- Provider and model
- Token counts
- Cost per call

### Time Period Filters

- **All Time**: Complete history
- **Last 7 Days**: Recent week
- **Last 30 Days**: Current month
- **Today**: Current session

---

## 🛠️ Technical Details

### Files Added

```
core/usage_tracker.py          # Cost calculation logic
database/usage_models.py       # Usage database models
ui/usage_components.py         # Dashboard components
USAGE_TRACKING.md             # Complete documentation
```

### Files Modified

```
main.py                       # Added usage page and tracking
core/ai_providers.py          # Return token usage data
core/auditor.py              # Track and save usage
README.md                     # Updated features list
CHANGELOG.md                  # Version 1.1.0 notes
```

### Database Schema

New table: `api_usage`

```sql
CREATE TABLE api_usage (
    id INTEGER PRIMARY KEY,
    timestamp DATETIME,
    provider VARCHAR(50),
    model VARCHAR(100),
    input_tokens INTEGER,
    output_tokens INTEGER,
    total_tokens INTEGER,
    cost_usd FLOAT,
    cost_cad FLOAT,
    analysis_id INTEGER
);
```

---

## 🎯 Use Cases

### For Budget-Conscious Users

Track spending to stay within monthly budget:
- Set personal limit (e.g., $20 CAD/month)
- Monitor daily/weekly
- Get alerts when approaching limit
- Switch to cheaper providers if needed

### For Heavy Users

Optimize costs at scale:
- Identify most expensive analyses
- Choose best provider for each use case
- Forecast monthly spending
- Justify costs with usage data

### For Comparison Shopping

Evaluate providers objectively:
- Run same idea through all 3 providers
- Compare quality vs. cost
- Make data-driven provider choices
- Save money without sacrificing quality

### For Reporting

Track business expenses:
- Export usage data to JSON
- Import to Excel/Google Sheets
- Generate expense reports
- Track ROI on AI tools

---

## ⚠️ Important Notes

### Exchange Rate

- Currently fixed at **1.36 USD to CAD**
- Update periodically for accuracy
- Edit `core/usage_tracker.py` to change rate

### Pricing Updates

Provider pricing may change. Update in `core/usage_tracker.py`:

```python
PRICING = {
    "openai": {
        "gpt-4o": {"input": 2.50, "output": 10.00},
        # Update these values as needed
    },
}
```

### Accuracy

- Token counts are exact from provider APIs
- Costs calculated using official pricing
- CAD conversion may vary slightly
- Actual bills from providers may differ due to taxes, rounding

---

## 📚 Documentation

Complete guides available:

- **USAGE_TRACKING.md** - Full usage tracking documentation
- **README.md** - Updated with usage tracking features
- **CHANGELOG.md** - Version 1.1.0 release notes

---

## 🎉 Benefits Summary

### Save Money
- Identify cheapest providers
- Monitor spending in real-time
- Optimize usage patterns
- **Potential savings: $20-40/month**

### Gain Insights
- Understand token usage
- See which analyses cost most
- Compare provider efficiency
- Make data-driven decisions

### Stay in Control
- Set personal budgets
- Get automatic alerts
- Track historical spending
- Plan future costs

### Complete Transparency
- See exact costs per analysis
- Breakdown by provider
- All data stored locally
- Export for reporting

---

## 🚀 Getting Started

**The feature is already active!** 

Just use the app normally and:

1. **Check sidebar** for quick cost summary
2. **Click "Usage & Costs"** for full dashboard
3. **Review costs** after each analysis
4. **Use estimator** before batch analyses
5. **Optimize** based on your usage patterns

---

## 💡 Pro Tips

1. **Baseline Test**: Run one analysis with each provider to see actual costs
2. **Monthly Budget**: Set a CAD limit and track weekly
3. **Provider Rotation**: Use cheapest for iterations, premium for final analysis
4. **Export Data**: Monthly export to track trends
5. **Cost Alerts**: Pay attention to warnings, they help prevent overspending

---

**Your AI usage, tracked. Your costs, controlled. All in Canadian Dollars.** 💰🇨🇦

For questions or issues with usage tracking, see `USAGE_TRACKING.md` or open a GitHub issue.


