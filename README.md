#  LLM Security Research Lab

A comprehensive educational framework for understanding and defending against LLM security vulnerabilities including **knowledge base poisoning**, **prompt injection**, and **model extraction attacks**.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Security](https://img.shields.io/badge/security-research-red.svg)

##  DISCLAIMER

**This tool is for educational and research purposes only.**

- Use only on systems you own or have explicit permission to test
- Do not use for malicious purposes
- Understand applicable laws and regulations
- Respect responsible disclosure practices

##  What This Project Covers

### 1. Knowledge Base Poisoning
Attackers inject malicious content into RAG (Retrieval-Augmented Generation) systems to manipulate LLM responses.

**Attack Examples:**
- Hiding instructions in documents
- Unicode obfuscation
- Context manipulation
- Delimiter injection

**Defenses:**
- Content sanitization
- Pattern detection
- Anomaly detection
- Input validation

### 2. Prompt Injection
Attempts to override system instructions through user input or retrieved content.

**Attack Types:**
- Direct instruction override
- Role manipulation
- Context confusion
- Multi-language injection
- Emotional manipulation

**Defenses:**
- Hardened system prompts
- Input filtering
- Threat scoring
- Delimiter protection

### 3. Model Extraction
Systematic API abuse to steal model behavior or weights.

**Attack Indicators:**
- High request rates
- Systematic query patterns
- Model probing queries
- Boundary testing
- Adversarial examples

**Defenses:**
- Rate limiting
- Behavioral analysis
- Query pattern detection
- API hardening
- Response filtering

## Quick Start

### Installation

```bash
# Clone repository
git clone <your-repo-url>
cd llm-security-research

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run Web Interface

```bash
streamlit run app.py
```

Access at `http://localhost:8501`

### Run CLI Tool

```bash
# Run security lab
python llm_security_lab.py

# Run attack scenarios
python attack_scenarios.py
```

## Usage

### Web Interface

The Streamlit dashboard provides four modules:

1. **Knowledge Base Poisoning**
   - Create test poison documents
   - Detect poisoned content
   - Sanitize contaminated data

2. **Prompt Injection**
   - Test injection payloads
   - Defense testing
   - Generate hardened prompts

3. **Model Extraction**
   - Monitor API requests
   - Configure defenses
   - View security alerts

4. **Security Dashboard**
   - Overall threat assessment
   - Findings by severity
   - Export audit reports

### Programmatic Usage

#### Knowledge Base Poisoning

```python
from llm_security_lab import KnowledgeBasePoisoning

kb_poison = KnowledgeBasePoisoning()

# Detect poisoned content
detection = kb_poison.detect_poisoned_content(suspicious_document)

if detection['is_suspicious']:
    print(f"Threat detected! Score: {detection['detection_score']:.2f}")
    
    # Sanitize
    clean_content = kb_poison.sanitize_content(suspicious_document)
```

#### Prompt Injection Defense

```python
from llm_security_lab import PromptInjectionTester

tester = PromptInjectionTester()

# Test user input
result = tester.test_injection_defense(
    user_input="Ignore previous instructions...",
    system_prompt="You are a helpful assistant."
)

print(f"Risk Score: {result['risk_score']:.2f}")
print(f"Action: {result['recommended_action']}")

# Get sanitized input
safe_input = result['sanitized_input']
```

#### Model Extraction Defense

```python
from llm_security_lab import ModelExtractionDefense

defense = ModelExtractionDefense(
    rate_limit_window=60,
    max_requests=100
)

# Track API request
analysis = defense.track_request(
    user_id="user123",
    query="What is your model architecture?",
    response="I am an AI assistant."
)

if analysis['is_suspicious']:
    print(f"Extraction attempt detected!")
    print(f"Action: {analysis['recommended_action']}")
```

## Features

### Detection Capabilities

-  **Pattern Matching**: Detect known injection keywords
-  **Unicode Analysis**: Find hidden characters
-  **Behavioral Analysis**: Identify systematic patterns
-  **Rate Limiting**: Track request frequencies
-  **Anomaly Detection**: Flag unusual queries
-  **Risk Scoring**: Quantify threat levels

### Defense Strategies

-  **Input Sanitization**: Clean malicious content
-  **Hardened Prompts**: Injection-resistant templates
-  **Rate Limiting**: Prevent API abuse
-  **Content Filtering**: Remove suspicious patterns
-  **Monitoring**: Real-time threat detection
-  **Audit Logging**: Track all security events

### Reporting

-  **JSON Export**: Machine-readable reports
-  **Severity Classification**: Critical/High/Medium/Low
-  **Recommendations**: Actionable security advice
-  **Trend Analysis**: Historical threat data
-  **Compliance**: Document security posture

##  Attack Scenarios

The project includes 5 realistic attack scenarios:

1. **Corporate Document Poisoning**
   - Injecting malicious content into company policies
   - Detection and sanitization demo

2. **RAG System Injection**
   - Combining retrieved content with injection
   - Context manipulation attacks

3. **Systematic Model Extraction**
   - API abuse for model replication
   - Rate limiting and detection

4. **Multi-Vector Attack**
   - Combined attack using multiple techniques
   - Comprehensive defense demonstration

5. **Social Engineering**
   - Emotional manipulation tactics
   - Authority impersonation
   - Urgency-based attacks

Run scenarios:
```bash
python attack_scenarios.py
```

##  Project Structure

```
llm-security-research/
├── llm_security_lab.py      # Core security framework
├── app.py                    # Streamlit web interface
├── attack_scenarios.py       # Demo attack scenarios
├── requirements.txt          # Dependencies
├── README.md                 # This file
├── .gitignore               # Git ignore rules
└── examples/                 # Example scripts
    ├── test_kb_poisoning.py
    ├── test_prompt_injection.py
    └── test_model_extraction.py
```

##  Technical Details

### Detection Algorithms

#### Knowledge Base Poisoning Detection
```python
# Multi-factor scoring system
- Injection keyword scanning (30% weight)
- Hidden Unicode detection (40% weight)
- Formatting anomalies (20% weight)
- Bracket patterns (30% weight)
Threshold: >0.5 = suspicious
```

#### Prompt Injection Detection
```python
# Threat pattern analysis
- Override keywords (30% per match)
- Delimiter manipulation (20% per delimiter)
- Role manipulation (25% per attempt)
- Encoding detection (20% per type)
- Structural anomalies (15%)
Threshold: >0.4 = injection attempt
```

#### Model Extraction Detection
```python
# Behavioral analysis
- Rate limit violations (40% weight)
- Query similarity (30% weight)
- Probing keywords (25% per keyword)
- Adversarial patterns (30% weight)
- Repetition detection (25% weight)
Threshold: >0.5 = suspicious activity
```

### Defense Mechanisms

#### Sanitization Process
1. Remove hidden Unicode characters
2. Strip injection keywords
3. Normalize whitespace
4. Escape special characters
5. Remove delimiter patterns

#### Rate Limiting Strategy
```python
# Multi-tier limits
- Per-minute: 60 requests
- Per-hour: 1,000 requests
- Per-day: 10,000 requests
- Burst limit: 10 requests
```

#### Hardened Prompt Template
```
System rules (immutable)
↓
Clear delimiter
↓
User content marker
↓
User input (untrusted)
↓
Response with rules enforcement
```

##  Use Cases

### Security Research
- Understanding LLM vulnerabilities
- Testing defense mechanisms
- Developing new attack vectors
- Evaluating security posture

### Education
- Teaching cybersecurity concepts
- LLM security workshops
- Red team training
- Security awareness programs

### Development
- Securing LLM applications
- Testing RAG systems
- API security hardening
- Implementing safeguards

### Compliance
- Security audits
- Penetration testing
- Risk assessments
- Documentation

##  Best Practices

### For Developers

1. **Input Validation**
   ```python
   # Always sanitize user input
   sanitized = kb_poison.sanitize_content(user_input)
   ```

2. **Rate Limiting**
   ```python
   # Apply per-user limits
   if request_count > max_requests:
       return "Rate limit exceeded"
   ```

3. **Monitoring**
   ```python
   # Log all suspicious activity
   if detection['is_suspicious']:
       log_security_event(detection)
   ```

4. **Hardened Prompts**
   ```python
   # Use injection-resistant templates
   template = tester.create_defense_template()
   ```

### For Security Teams

1. **Regular Audits**
   - Run weekly security scans
   - Review audit logs
   - Update threat models

2. **Incident Response**
   - Monitor alerts in real-time
   - Investigate anomalies
   - Document incidents

3. **Defense Updates**
   - Track new attack vectors
   - Update detection rules
   - Test defenses regularly

## 🔧 Configuration

### Environment Variables

```bash
# .env file
RATE_LIMIT_WINDOW=60          # seconds
MAX_REQUESTS_PER_WINDOW=100
DETECTION_THRESHOLD=0.5
LOG_LEVEL=INFO
ALERT_EMAIL=security@company.com
```

### API Hardening Config

```json
{
  "rate_limiting": {
    "requests_per_minute": 60,
    "requests_per_hour": 1000,
    "burst_limit": 10
  },
  "response_filtering": {
    "max_response_length": 2000,
    "filter_internal_info": true
  },
  "authentication": {
    "require_api_key": true,
    "rotate_keys_regularly": true
  }
}
```

## 🧪 Testing

```bash
# Run unit tests
pytest tests/

# Test specific module
python -m pytest tests/test_kb_poisoning.py

# Run with coverage
pytest --cov=. tests/
```

##  Resources

### Learn More
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Anthropic's Claude Safety](https://www.anthropic.com/index/claude-2)
- [LLM Security Research Papers](https://arxiv.org/search/?query=llm+security)

### Related Projects
- [LLM Guard](https://github.com/laiyer-ai/llm-guard)
- [Prompt Injection Detector](https://github.com/protectai/rebuff)
- [AI Security Tools](https://github.com/topics/ai-security)

##  Contributing

Contributions welcome! Areas of interest:

- [ ] New attack vectors
- [ ] Improved detection algorithms
- [ ] Additional defense mechanisms
- [ ] Performance optimizations
- [ ] Documentation improvements
- [ ] Test coverage

**Please:**
1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Submit a pull request

##  License

MIT License - See LICENSE file for details

##  Responsible Disclosure

If you discover security vulnerabilities:

1. **Do NOT** publicly disclose
2. Email: security@[your-domain].com
3. Provide detailed information
4. Allow time for fixes
5. Credit will be given

##  Acknowledgments

- OWASP LLM Security Project
- AI Security research community
- Anthropic & OpenAI safety teams
- Security researchers worldwide

##  Contact

- **Issues**: Open a GitHub issue
- **Security**: security@[your-domain].com
- **General**: [your-email]

##  Star History

If you find this project useful:
-  Star the repository
-  Fork for your research
-  Share with security community
-  Contribute improvements

---

**Built with ❤️ for LLM security research and education**

**Stay secure! **
