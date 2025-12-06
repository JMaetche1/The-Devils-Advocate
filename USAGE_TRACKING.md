# 💰 API Usage & Cost Tracking Guide

The Devil's Advocate now includes comprehensive API usage tracking with costs displayed in Canadian Dollars (CAD).

---

## Features

### 🎯 What's Tracked

- **API Calls**: Total number of analyses performed
- **Token Usage**: Input and output tokens for each call
- **Costs**: Calculated in both USD and CAD
- **Provider Breakdown**: See usage by OpenAI, Anthropic, or Google
- **Historical Data**: Track usage over time periods

### 📊 Dashboard Views

1. **Sidebar Quick Stats**
   - Current session total cost (CAD)
   - Number of API calls
   - Warning alerts for high usage

2. **Usage & Costs Page**
   - Detailed usage dashboard
   - Breakdown by provider
   - Recent API calls table
   - Cost estimator tool

3. **Per-Analysis Metrics**
   - Tokens used for each analysis
   - Exact cost in CAD
   - Input/output token breakdown

---

## How It Works

### Automatic Tracking

Every time you run an analysis:

1. **Token count** is retrieved from the AI provider
2. **Cost is calculated** using current provider pricing
3. **USD to CAD conversion** applied (rate: 1.36)
4. **Data is saved** to local database
5. **Statistics update** in real-time

### Cost Calculation

```
Input Cost = (Input Tokens / 1,000,000) × Provider Input Rate
Output Cost = (Output Tokens / 1,000,000) × Provider Output Rate
Total USD = Input Cost + Output Cost
Total CAD = Total USD × 1.36
```

---

## Current Pricing (December 2024)

### OpenAI GPT-4o
- **Input**: $2.50 USD per 1M tokens
- **Output**: $10.00 USD per 1M tokens
- **Average analysis**: $0.50-1.00 CAD

### Anthropic Claude 3.5 Sonnet
- **Input**: $3.00 USD per 1M tokens
- **Output**: $15.00 USD per 1M tokens
- **Average analysis**: $0.30-0.80 CAD

### Google Gemini 1.5 Pro
- **Input**: $1.25 USD per 1M tokens
- **Output**: $5.00 USD per 1M tokens
- **Average analysis**: $0.20-0.50 CAD
- **Note**: Often has free tier available

---

## Using the Usage Tracker

### View Current Usage

**In Sidebar:**
- Quick glance at total cost (CAD)
- Number of API calls this session
- Warning if costs exceed $5 CAD

**In Usage & Costs Page:**
1. Click "Usage & Costs" in navigation
2. Select time period (All Time, Last 7 Days, Last 30 Days, Today)
3. View detailed breakdown

### Understanding the Dashboard

**Total Metrics:**
- Total API Calls
- Total Tokens (input + output)
- Cost in USD
- Cost in CAD

**By Provider:**
- Calls per provider
- Tokens per provider
- Cost per provider

**Recent Usage Table:**
- Last 20 API calls
- Timestamp, provider, model, tokens, cost
- Helps identify which analyses cost most

### Cost Estimator

Before running multiple analyses:

1. Go to "Usage & Costs" page
2. Scroll to "Cost Estimator"
3. Enter number of planned analyses
4. Select AI provider
5. See estimated total cost

**Example:**
```
10 analyses with OpenAI GPT-4o
= 10 × $0.75 CAD
= $7.50 CAD estimated
```

---

## Cost Optimization Tips

### 💡 Save Money

1. **Choose Cheaper Providers**
   - Google Gemini: ~$0.35/analysis (cheapest)
   - Anthropic Claude: ~$0.55/analysis (good value)
   - OpenAI GPT-4: ~$0.75/analysis (most expensive)

2. **Use Quick Analysis Mode**
   - Shorter inputs = fewer tokens
   - Avoid uploading entire documents when possible

3. **Disable Competitor Intelligence**
   - When not needed for your analysis
   - Reduces input token count

4. **Batch Similar Ideas**
   - Run multiple variations through same provider
   - Compare all at once rather than one at a time

### 📊 Monitor Usage

Set personal budgets:
- **Daily limit**: e.g., 5 analyses = ~$3.75 CAD
- **Weekly limit**: e.g., 20 analyses = ~$15 CAD
- **Monthly limit**: e.g., 100 analyses = ~$75 CAD

**The app will show warnings** when you exceed $5 and $10 CAD thresholds.

---

## Data Privacy

### What's Stored

- Timestamp of each API call
- Provider and model used
- Token counts (input/output)
- Calculated costs (USD/CAD)
- Link to analysis (optional)

### Where It's Stored

- **Local SQLite database** (`data/history.db`)
- **Never sent to external services**
- **You control the data**

### Data Retention

- Data is kept indefinitely by default
- Can be manually cleared from database
- Only visible to you on your machine

---

## Understanding Your Costs

### Why Do Costs Vary?

**Factors affecting cost:**

1. **Input Length**
   - Longer business descriptions = more input tokens
   - Uploading documents = significantly more tokens
   - Competitor intelligence = additional input

2. **Output Length**
   - More detailed analyses = more output tokens
   - Longer Kill Shot explanations
   - Extensive Steel Man arguments

3. **Provider**
   - Different pricing per provider
   - Different token counting methods
   - Some include free tiers

### Typical Cost Examples

**Quick Analysis** (short description):
- Input: ~1,000 tokens
- Output: ~1,500 tokens
- Cost: $0.20-0.40 CAD

**Structured Analysis** (detailed form):
- Input: ~2,500 tokens
- Output: ~2,000 tokens
- Cost: $0.40-0.80 CAD

**Document Upload** (10-page business plan):
- Input: ~6,000 tokens
- Output: ~2,500 tokens
- Cost: $1.00-2.00 CAD

**With Competitor Intelligence**:
- Add ~1,000-2,000 input tokens
- Add ~$0.10-0.30 CAD to cost

---

## Alerts & Warnings

### Cost Threshold Alerts

**$5 CAD:**
- Warning appears in sidebar
- Suggestion to check Usage page

**$10 CAD:**
- Alert on Usage & Costs page
- Recommendations to reduce costs

**Custom Thresholds:**
- Can be configured in code
- Edit `ui/usage_components.py`

---

## Frequently Asked Questions

### Is usage tracking required?

No, but it's automatic. All API calls are tracked to help you:
- Monitor spending
- Understand which providers are cheapest
- Budget for future analyses

### Can I disable tracking?

Tracking is built-in and cannot be disabled, but:
- Data stays on your machine
- No data is sent externally
- You can delete the database file

### How accurate are the costs?

Very accurate for:
- OpenAI (exact token counts provided)
- Anthropic (exact token counts provided)
- Google (exact token counts provided)

The USD to CAD exchange rate is fixed at 1.36 and should be updated periodically for accuracy.

### What if pricing changes?

Update the pricing in `core/usage_tracker.py`:

```python
PRICING = {
    "openai": {
        "gpt-4o": {"input": 2.50, "output": 10.00},
        # Update these values
    },
    # ...
}
```

### Can I export usage data?

Yes! On the Usage & Costs page:
- Click "Export Usage Data"
- Download as JSON
- Import into Excel/Google Sheets for analysis

---

## Comparison Shopping

### Provider Cost Comparison

For 50 analyses per month:

| Provider | Avg per Analysis | Total per Month |
|----------|-----------------|-----------------|
| **Google Gemini** | $0.35 CAD | $17.50 CAD |
| **Anthropic Claude** | $0.55 CAD | $27.50 CAD |
| **OpenAI GPT-4o** | $0.75 CAD | $37.50 CAD |

**Savings:** Using Google instead of OpenAI = **$20/month saved**

### Quality vs. Cost

**Best Value:**
- Anthropic Claude 3.5 Sonnet
- High quality, moderate cost
- Excellent business analysis

**Cheapest:**
- Google Gemini 1.5 Pro
- Good quality, lowest cost
- Often has free tier

**Premium:**
- OpenAI GPT-4o
- Creative scenarios
- Higher cost

**Recommendation:** Try all three and compare results for your specific use case.

---

## Future Enhancements

Planned features for usage tracking:

- [ ] Custom budget alerts
- [ ] Monthly cost reports
- [ ] Export to CSV/Excel
- [ ] Cost trend charts
- [ ] Budget forecasting
- [ ] Multi-currency support
- [ ] Real-time exchange rates

---

## Support

If you notice incorrect cost calculations:

1. Check pricing in `core/usage_tracker.py`
2. Verify exchange rate (currently 1.36 USD to CAD)
3. Compare with provider's official pricing
4. Update pricing constants if needed

---

**Bottom Line:** The usage tracker helps you understand and control your AI API costs, all displayed in Canadian Dollars for easy budgeting. 💰


