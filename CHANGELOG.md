# Changelog

All notable changes to The Devil's Advocate will be documented in this file.

## [1.2.0] - 2025-12-06

### Added - Security & GitHub Readiness
- 🔒 **`.env.example` template file** - Safe template for users to copy
- 📄 **SECURITY.md** - Comprehensive security guidelines and best practices
- 📚 **SETUP.md** - Detailed setup guide for new users
- 🔐 Enhanced `.gitignore` with additional protections for sensitive files
- 🛡️ Security section added to README.md
- ✅ Pre-commit verification instructions

### Changed
- 🎨 **Settings page redesigned** - Removed non-functional API key inputs from UI
- 🔑 API keys now **only** configured via `.env` file (more secure)
- 📖 Updated README.md with security warnings and improved quick start
- 📝 Updated installation instructions to use `.env.example` template
- 🔒 Settings page now shows API key configuration status (not input fields)

### Security Improvements
- ✅ Removed password-type inputs from Settings page (they didn't work and gave false sense of security)
- ✅ All API keys must now be in `.env` file (proper security model)
- ✅ Added `.env.example` to git (safe template)
- ✅ Enhanced `.gitignore` to prevent accidental exposure of:
  - All `.env` variants (`*.env`, `.env.local`, etc.)
  - Credential files (`credentials.json`, `service-account.json`)
  - Certificate files (`*.key`, `*.pem`, `*.cert`)
  - Backup files that might contain sensitive data
  - Private documentation files
- ✅ Database journal files now ignored
- ✅ Backup files (`.bak`, `.backup`, `.old`) now ignored

### Documentation
- 📄 New SECURITY.md with complete security guidelines
- 📚 New SETUP.md with step-by-step installation
- 📖 README.md updated with security section
- 🔐 Clear warnings about not deploying to public servers
- 📝 Instructions for safe GitHub collaboration

### Fixed
- 🐛 **GPT-5 model formatting bug** - Dollar signs no longer cause weird character spacing
- 🐛 **Competitor intelligence error handling** - Clear error messages when SERPER_API_KEY missing
- 🔍 Better error messages for API key configuration issues

### For Developers
- ✅ Project is now **GitHub-ready** - safe to push without exposing secrets
- ✅ Clear separation between template (`.env.example`) and actual keys (`.env`)
- ✅ Each user sets up their own environment with their own keys
- ✅ No shared credentials or multi-user security concerns

### Breaking Changes
- ⚠️ **Settings page API key inputs removed** - Must use `.env` file
- ⚠️ **First-time users** must copy `.env.example` to `.env` and add keys

### Migration Guide
If upgrading from v1.1.0:
1. Your existing `.env` file will continue to work
2. Settings page no longer has API key inputs (by design)
3. No action needed unless you were trying to use Settings page inputs

## [1.1.0] - 2024-12-06

### Added
- 💰 **API Usage & Cost Tracking System**
  - Real-time tracking of all API calls
  - Token usage monitoring (input/output)
  - Cost calculation in USD and CAD
  - Historical usage data storage
  - Usage dashboard with statistics
  - Breakdown by AI provider
  - Recent API calls table
  - Cost estimator tool
  - Budget alerts for high usage
  - Session cost display in sidebar
  - Per-analysis cost metrics
- 📊 New "Usage & Costs" page in navigation
- 📝 Complete usage tracking documentation (USAGE_TRACKING.md)
- 🔢 Canadian Dollar (CAD) cost calculations (1.36 exchange rate)
- ⚠️ Automatic cost threshold warnings ($5 and $10 CAD)

### Changed
- Updated all AI provider interfaces to return usage metadata
- Modified Auditor class to track and save usage data
- Enhanced analysis results to include cost information
- Updated sidebar to show session usage stats
- Improved Settings page version number

### Technical
- New module: `core/usage_tracker.py` - Usage tracking logic
- New module: `database/usage_models.py` - Usage database models
- New module: `ui/usage_components.py` - Usage UI components
- Enhanced AI provider response format to include token counts
- Database schema extended with `api_usage` table

## [1.0.0] - 2024-12-06

### Initial Release

#### Features
- 🤖 Multi-AI Provider Support (OpenAI, Anthropic Claude, Google Gemini)
- 📊 Pre-Mortem Analysis Framework implementation
- 🔍 Optional competitor intelligence gathering via web scraping
- 📚 Full analysis history with SQLite database
- 🔎 Search and filter analysis history
- 📥 Export analyses to Markdown format
- 🎨 Modern, responsive UI with custom styling
- ⚙️ Settings page for API key management

#### Input Modes
- Structured Form (detailed business plan input)
- Quick Analysis (rapid feedback on ideas)
- Document Upload (PDF, DOCX, TXT support)

#### Analysis Components
- Verdict (VIABLE / RISKY / DEAD ON ARRIVAL)
- Kill Shot (fatal flaw identification)
- Scenario Simulation (Market, Operations, Black Swan)
- Steel Man Argument (path to success)

#### Technical
- Python 3.8+ support
- Streamlit-based web interface
- SQLAlchemy ORM for database
- BeautifulSoup4 for web scraping
- Tenacity for API retry logic
- PyPDF2 and python-docx for document parsing

#### Documentation
- Comprehensive README with installation guide
- Detailed USAGE_GUIDE with best practices
- EXAMPLES.md with real-world analysis samples
- QUICKSTART.md for rapid setup
- Launch scripts for Windows/Mac/Linux

---

## [Unreleased]

### Planned Features

#### Short-term (v1.1.0)
- [ ] Batch analysis mode (analyze multiple ideas at once)
- [ ] Comparison view (side-by-side analysis comparison)
- [ ] Custom analysis templates
- [ ] PDF export functionality
- [ ] More detailed statistics dashboard
- [ ] Analysis sharing (generate shareable links)

#### Medium-term (v1.2.0)
- [ ] Collaborative features (team workspaces)
- [ ] API endpoint for programmatic access
- [ ] Integration with project management tools
- [ ] Advanced web scraping with Playwright
- [ ] Social media sentiment analysis
- [ ] Regulatory database integration

#### Long-term (v2.0.0)
- [ ] AI-powered follow-up questions
- [ ] Automated competitive analysis reports
- [ ] Market size estimation tools
- [ ] Financial modeling integration
- [ ] Custom AI fine-tuning
- [ ] Mobile app version

### Potential Improvements
- Performance optimization for large documents
- Enhanced caching for web scraping
- Better error handling and recovery
- Accessibility improvements
- Internationalization (i18n) support
- Dark/light theme toggle
- Keyboard shortcuts
- Analysis templates for specific industries

---

## Version History Notes

### Version Numbering
- **Major (X.0.0)**: Breaking changes, major new features
- **Minor (0.X.0)**: New features, backward compatible
- **Patch (0.0.X)**: Bug fixes, minor improvements

### Release Schedule
- Patch releases: As needed for bug fixes
- Minor releases: Monthly for new features
- Major releases: Quarterly for significant changes

---

## Contributing

See issues on GitHub for planned features and known bugs. Pull requests welcome!

---

## Support

For bug reports and feature requests, please open an issue on GitHub.

