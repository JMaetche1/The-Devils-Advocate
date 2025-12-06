# 📖 The Devil's Advocate - Usage Guide

A comprehensive guide to getting the most out of your red team business analysis.

---

## 🎯 Quick Start

### First Time Setup

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Set Up API Key**

Choose ONE of these methods:

**Option A: Environment File (Recommended)**
```bash
# Create .env file
echo "OPENAI_API_KEY=sk-..." > .env
```

**Option B: Direct Environment Variable**
```bash
# Windows PowerShell
$env:OPENAI_API_KEY="sk-..."

# Mac/Linux
export OPENAI_API_KEY="sk-..."
```

**Option C: Enter in Settings**
- Run the app
- Go to Settings page
- Enter API key (session only)

3. **Launch**
```bash
streamlit run main.py
```

---

## 📝 How to Write Effective Business Descriptions

### ✅ GOOD Example

```
Business Name: QuickClean AI

Description:
An AI-powered mobile app that connects busy professionals with vetted 
cleaning services in under 2 hours. Users book through the app, cleaners 
arrive within 120 minutes, and payment is automatic.

Target Market:
Urban professionals aged 25-45, earning $75k+, who work 50+ hour weeks 
and live in apartments or condos in top 20 US metro areas.

Revenue Model:
- 25% commission on each booking
- Average booking: $80
- Premium subscription: $19.99/month for priority booking

Key Assumptions:
- 15% of target market needs last-minute cleaning monthly
- Can recruit 500 cleaners in first 6 months
- Customer acquisition cost: $25
- Average customer lifetime value: $400

Competitive Landscape:
- Handy: focuses on scheduled cleaning, not same-day
- Taskrabbit: generalist platform, not specialized
- Our advantage: Speed + specialization
```

### ❌ BAD Example

```
We're building an app for cleaning. It's like Uber for cleaners.
We think people will like it. There's a big market.
```

**Why it's bad:**
- No specifics
- No numbers
- Vague market description
- No unique value proposition

---

## 🎮 Three Input Modes Explained

### 1. Structured Form

**When to use:**
- You have a detailed business plan
- You want the most thorough analysis
- You've done market research

**What to provide:**
- Business name and concept
- Target market (be specific: demographics, geography, behavior)
- Revenue model (with numbers and pricing)
- Key assumptions (the things that MUST be true)
- Competitive landscape (who else does this, what's different)

**Time:** 5-10 minutes to fill out

### 2. Quick Analysis

**When to use:**
- You just had an idea and want quick feedback
- You're in early brainstorming
- You want to test multiple variations

**What to provide:**
- A paragraph describing the core concept
- Include: problem, solution, who pays, why now

**Time:** 1-2 minutes

**Example:**
```
A subscription box for pet owners that delivers customized toys and treats 
based on their pet's breed, age, and preferences. $29.99/month. Different 
from BarkBox because we use AI to personalize each box. Target market is 
millennial pet owners who spend $100+/month on their pets already.
```

### 3. Upload Document

**When to use:**
- You have an existing business plan
- You have a pitch deck with notes
- You've written detailed documentation

**Supported formats:**
- PDF
- Word documents (.docx)
- Plain text (.txt)

**Tips:**
- Ensure text is selectable (not scanned images)
- Documents under 50 pages work best
- Can edit extracted text before analysis

---

## 🤖 Choosing an AI Provider

### OpenAI (GPT-4o) 🟢

**Best for:** Balanced analysis with creative failure scenarios

**Strengths:**
- Creative "what if" scenarios
- Good at identifying non-obvious risks
- Fast response times

**Weaknesses:**
- Can sometimes be too creative
- May miss technical details

**Cost:** ~$0.50-1.00 per analysis

### Anthropic (Claude 3.5 Sonnet) 🔵

**Best for:** Deep, nuanced business analysis

**Strengths:**
- Excellent at logical reasoning
- Very thorough with business models
- Understands complex financial structures

**Weaknesses:**
- Can be overly conservative
- Slightly slower

**Cost:** ~$0.30-0.80 per analysis

### Google (Gemini 1.5 Pro) 🟡

**Best for:** Fast analysis with good context

**Strengths:**
- Fast response times
- Good at market trends
- Handles long documents well

**Weaknesses:**
- Sometimes less detailed
- Can miss subtle flaws

**Cost:** ~$0.20-0.50 per analysis

### 💡 Pro Tip

Run the SAME business idea through all three providers and compare results. Often they'll catch different issues.

---

## 🔍 Using Competitor Intelligence

### When to Enable

✅ Enable when:
- You have direct competitors
- You're entering an established market
- You want real pricing data
- You need recent news/trends

❌ Skip when:
- You're in a completely new category
- You're testing multiple quick ideas
- API rate limits are a concern
- You want faster results

### What It Does

1. **Google Search**: Finds competitors, news, trends
2. **Pricing Data**: Attempts to extract competitor pricing
3. **Recent News**: Looks for regulatory changes, funding rounds
4. **Market Sentiment**: Checks social media discussions

### Limitations

- Requires Serper API key for best results
- Adds 30-60 seconds to analysis time
- May not find data for very niche markets
- Rate limited to avoid IP bans

### Example Output

```
COMPETITOR INTELLIGENCE:

1. **TaskRabbit raises $50M Series D**
   Query: cleaning services competitors
   TaskRabbit, the on-demand service platform, raised $50M to expand 
   into new categories including cleaning...
   Source: techcrunch.com

2. **Handy Cleaning Service Reviews**
   Query: home cleaning app pricing
   Average Handy cleaning session costs $65-120 depending on home size.
   Customers report 4.2/5 satisfaction...
   Source: trustpilot.com
```

---

## 📊 Understanding Your Analysis

### The Verdict

**VIABLE** 🟢
- The idea could work with execution
- Risks are manageable
- Market opportunity exists
- Still shows weaknesses to address

**RISKY** 🟡
- Significant challenges ahead
- Multiple assumptions need validation
- Market is uncertain or competitive
- Could succeed but odds are tough

**DEAD ON ARRIVAL** 🔴
- Fatal flaws in the concept
- Market doesn't exist or won't pay
- Competitors have insurmountable advantages
- Economics don't work

**Important:** Even "VIABLE" doesn't mean "guaranteed success." Even "DOA" might work with pivots.

### The Kill Shot

This is the ONE thing that will most likely destroy your business.

**Common Kill Shots:**
- "Customer acquisition cost exceeds lifetime value"
- "No defensible moat against well-funded competitors"
- "Chicken-and-egg problem with no clear first step"
- "Unit economics require unrealistic scale"

**What to do:**
1. Accept this is your #1 risk
2. Develop specific mitigation strategy
3. Test this assumption FIRST
4. If you can't solve it, pivot or quit

### The Scenarios

These are specific failure narratives:

**Scenario A (Market):**
- Focus: Will customers actually pay?
- Common issues: Willingness to pay, market size, adoption rate

**Scenario B (Operations):**
- Focus: Can you actually deliver?
- Common issues: Supply chain, hiring, scale, margins

**Scenario C (Black Swan):**
- Focus: What external force kills you?
- Common issues: Regulation, competitor, technology shift

### The Steel Man

This is your roadmap IF you want to proceed.

It will include:
- Specific tests to run
- Metrics to validate
- Milestones to hit
- Pivot points to consider

**Treat this as your real action plan.**

---

## 💾 Managing History

### Saving Analyses

After each analysis:
1. Click "💾 Save to History"
2. Add tags or notes (optional)
3. Access anytime from History page

### Searching History

**By Name:**
```
Search: "cleaning app"
```

**By Verdict:**
- Filter dropdown: "VIABLE", "RISKY", or "DEAD ON ARRIVAL"

**By Date:**
- Most recent appears first
- Can filter by date range

### Comparing Analyses

Use history to:
- Track how an idea evolved
- Compare different approaches to same problem
- See patterns in why ideas fail
- Learn from past mistakes

### Exporting

**Markdown:**
- Full formatted report
- Include in documentation
- Share with team

**Text:**
- Plain text version
- Easy to paste in emails
- Works anywhere

---

## 🎯 Best Practices

### Before You Analyze

1. **Do Basic Research**: Know your market size, competitors, pricing
2. **Have Numbers**: Revenue assumptions, cost estimates, user counts
3. **Be Honest**: Hiding flaws from the AI means hiding them from yourself
4. **Be Specific**: "Young people" vs "Women aged 25-34 living in urban areas"

### During Analysis

1. **Use Structured Form**: For serious ideas
2. **Enable Intelligence**: For competitive markets
3. **Read Everything**: Don't just look at the verdict
4. **Take Notes**: Write down specific concerns to research

### After Analysis

1. **Don't Get Defensive**: The AI is trying to help
2. **Test Kill Shots**: Validate or invalidate the biggest risk
3. **Follow Steel Man**: If proceeding, use as roadmap
4. **Iterate**: Revise and re-analyze

### Advanced Techniques

**Stress Test Variations:**
```
Analyze the same idea with:
- 10x higher customer acquisition cost
- 50% of assumed market size
- 2 years later market entry
```

**Component Testing:**
```
Instead of full business, analyze:
- Just the revenue model
- Just the go-to-market strategy
- Just the competitive moat
```

---

## 🚨 Common Mistakes

### 1. Being Too Vague

❌ "An app for fitness"
✅ "A mobile app that uses computer vision to correct your form during home workouts, targeting women aged 25-40 who can't afford personal trainers."

### 2. Ignoring Bad Verdicts

If you get "DEAD ON ARRIVAL" on 3 different providers, that's not a bug—it's a feature. Listen to it.

### 3. Not Providing Numbers

❌ "People will pay for this"
✅ "Survey of 100 target customers showed 45% would pay $15/month"

### 4. Cherry-Picking Providers

Don't keep re-running until you get "VIABLE." If every provider says "RISKY," they might be right.

### 5. Skipping the Steel Man

The most valuable part is often the path forward, not the critique.

---

## 💡 Pro Tips

1. **Save Everything**: Even "bad" ideas teach you patterns

2. **Compare Providers**: Run through all three, see what overlaps

3. **Test Kill Shots First**: Before building anything, validate the fatal flaw doesn't exist

4. **Use for Features**: Analyze new features, not just full businesses

5. **Bring Real Data**: The more specific your input, the more useful the output

6. **Iterate Publicly**: Share analyses with advisors, get their input

7. **Set Triggers**: "If we don't hit 100 users in 30 days, pivot" (from Steel Man)

8. **Accept Reality**: If 3 different providers all say the same thing is your kill shot, believe them

---

## 🆘 Troubleshooting

### "API key not configured"

**Solution:** Check your .env file or enter key in Settings

### "Analysis incomplete"

**Solution:** 
- Check internet connection
- Verify API key is valid
- Try different provider
- Reduce input length

### "No competitor intelligence found"

**Solution:**
- Add Serper API key for better results
- Manually add competitor info in form
- Use more common search terms

### "Slow analysis"

**Solution:**
- Disable competitor intelligence
- Use Google Gemini (fastest)
- Reduce input length
- Check internet speed

---

## 📈 Measuring Success

### Good Signs

- You found a kill shot you hadn't considered
- The steel man path is clear and testable
- Different providers agree on main risks
- You have specific next steps

### Warning Signs

- You're arguing with the analysis
- You're shopping for a better verdict
- You're ignoring obvious points
- You can't articulate the kill shot to others

---

## 🎓 Learning Resources

### Recommended Reading

- "The Mom Test" by Rob Fitzpatrick
- "Zero to One" by Peter Thiel  
- "The Lean Startup" by Eric Ries
- "Obviously Awesome" by April Dunford

### Related Concepts

- Pre-Mortem Analysis
- Red Team Thinking
- Inversion (Charlie Munger)
- Jobs to Be Done
- Value Proposition Design

---

## 📞 Getting Help

If you're stuck:

1. Check this guide
2. Review example analyses
3. Try simpler input first
4. Check GitHub issues
5. Ask the community

---

**Remember: A harsh analysis today saves you from a failed business tomorrow.** 🛡️


