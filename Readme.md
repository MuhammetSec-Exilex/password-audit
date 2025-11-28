# 🔐 Password Audit Tool

Comprehensive password auditing tool for assessing strength through entropy analysis, pattern detection, and crack time estimation.

**⚠️ Educational Use Only**

---

## 🚀 Quick Start

```bash
python3 cli.py -p "MyPassword123!"           # Analyze password
python3 cli.py -f passwords.txt              # Batch analysis
python3 cli.py -p "Pass123!" --json          # JSON output
python3 cli.py -p "Pass123" -g 1e12          # GPU simulation
```

---

## 🎯 Security Levels

| Level | Range | Status |
|-------|-------|--------|
| CRITICAL | 0-30 bits | 🔴 Instantly crackable |
| WEAK | 30-50 bits | 🟠 Hours to crack |
| FAIR | 50-70 bits | 🟡 Days to crack |
| GOOD | 70-90 bits | 🟢 Years to crack |
| EXCELLENT | 90-120 bits | 🟢 Centuries |
| MASTER | 120+ bits | 💎 Millions of years |

---

## 📖 Usage

```bash
python3 cli.py [OPTIONS]

OPTIONS:
  -p, --password TEXT    Single password
  -f, --file TEXT        File with passwords (one per line)
  -g, --guesses FLOAT    Guesses per second (default: 1e9)
  --json                 JSON output
  -h, --help             Help message
```

---

## 🔬 How It Works

### Entropy Calculation

```
Entropy (bits) = log₂(pool_size) × length
```

**Pool sizes:**
- Lowercase (a-z): 26
- Uppercase (A-Z): 26
- Digits (0-9): 10
- Symbols: 32
- Unicode: 128
- Spaces: 1

### 7 Patterns Detected

1. **Common Password** - Dictionary match
2. **Low Variation** - ≤2 unique characters
3. **Repeated Chars** - 3+ same character
4. **Sequential** - abc, 123, xyz
5. **Year-like** - 1900-2025 or 00-99
6. **Single Case** - All upper/lower
7. **All Digits** - Only numbers

### Attack Scenarios

| Scenario | Speed |
|----------|-------|
| CPU Single | 1M/sec |
| CPU Multi | 1B/sec |
| GPU Single | 1T/sec |
| GPU Farm | 10T/sec |
| Botnet | 1000T/sec |

### Hash Penalties

| Function | Penalty |
|----------|---------|
| Plaintext | 1x |
| MD5/SHA256 | 1x |
| bcrypt | 200x |
| Argon2 | 1000x |
| scrypt | 1000x |

---

## �� Best Practices

### ✅ DO
- 12+ characters (16+ better)
- Mix: Uppercase, Lowercase, Digits, Symbols
- Random characters (no patterns)
- Unique per account
- Passphrases: "Correct-Horse-Battery-Staple"

### ❌ DON'T
- Dictionary words
- Sequential patterns (abc, 123, qwerty)
- Repeated characters (aaa, 111)
- Personal info (birthdate, names)
- Same password everywhere

---

## 🔌 Python API

### Installation

```bash
pip install termcolor  # Optional for colors
```

### Basic Example

```python
from audit import analyze_password

result = analyze_password("MyPassword123!")

print(result["security_level"]["level"])      # FAIR
print(result["estimated_crack_human"])        # 70.55 hours
print(result["issues"])                       # List of issues
```

### Advanced Example

```python
from audit import analyze_password, entropy_bits, shannon_entropy

pw = "MyPassword123!"
print(f"Pool Entropy: {entropy_bits(pw):.2f} bits")
print(f"Shannon Entropy: {shannon_entropy(pw):.2f} bits")

# GPU simulation
result = analyze_password(pw, guesses_per_second=1e12)
print(result["estimated_crack_human"])
```

---

## 📊 Example Output

```
╔════════════════════════════════════════╗
║ 🟡 Password Analysis - FAIR            ║
╚════════════════════════════════════════╝

Basic Information:
  Password: MyPass123
  Length: 9

Entropy: 53.59 bits (Pool) | 26.53 bits (Shannon)

Security: 🟡 FAIR - Acceptable, could be stronger

Crack Time:
  CPU: 156.68 hours
  GPU: 3.76 minutes
  Botnet: 13.54 seconds

Hash Protection:
  bcrypt: 85.85 days
  Argon2: 429.26 days

Issues: sequential-chars, year-like
```

---

## 📚 Output Formats

### Human-Readable (Default)

```bash
python3 cli.py -p "Test123!"
```

### JSON Format

```bash
python3 cli.py -p "Test123!" --json
```

---

## ⚖️ Disclaimers

### ✅ What This Does
- Estimates entropy based on character analysis
- Detects weak patterns
- Simulates brute-force scenarios
- Provides recommendations

### ❌ What This Does NOT Do
- Replace authentication systems
- Account for phishing/social engineering
- Guarantee actual security
- Test specific hash implementations

### Real Security Requires
- Proper hash implementation (bcrypt, Argon2)
- Strong salt usage
- Account lockout policies
- Multi-factor authentication
- Regular security updates

---

## 📚 References

- [NIST Password Guidelines](https://pages.nist.gov/800-63-3/)
- [Information Entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory))
- [Password Cracking](https://en.wikipedia.org/wiki/Password_cracking)
- [Cryptographic Hashing](https://en.wikipedia.org/wiki/Cryptographic_hash_function)

---

## 🔗 Related Tools

- **[zxcvbn](https://github.com/dropbox/zxcvbn)** - JavaScript password estimator
- **[hashcat](https://hashcat.net/)** - Password cracking
- **[John the Ripper](https://www.openwall.com/john/)** - Auditing tool

---

## 🚧 Planned Features (Roadmap)

### Phase 2 - Advanced Analysis
- [ ] **Keyboard Pattern Detection** - Detect QWERTY, DVORAK patterns
- [ ] **Levenshtein Distance** - Find similarity to known passwords
- [ ] **Contextual Analysis** - Check against user's personal info
- [ ] **Dictionary Expansion** - Support custom word lists
- [ ] **Multi-language Support** - Turkish, German, French wordlists

### Phase 3 - Integration & APIs
- [ ] **REST API** - HTTP endpoint for password analysis
- [ ] **Docker Container** - Containerized deployment
- [ ] **Python Package** - PyPI distribution
- [ ] **Web Dashboard** - Interactive web interface
- [ ] **Database Logging** - Track analysis history

### Phase 4 - Advanced Features
- [ ] **Compromised Password Check** - HaveIBeenPwned API integration
- [ ] **Machine Learning Model** - Neural network for pattern recognition
- [ ] **Batch Processing Queue** - Large file processing optimization
- [ ] **Real-time Monitoring** - Password change detection
- [ ] **Custom Rules Engine** - User-defined validation rules

### Phase 5 - Enterprise Features
- [ ] **LDAP Integration** - Active Directory support
- [ ] **Audit Logging** - Compliance reporting (GDPR, SOC2)
- [ ] **Team Management** - Multi-user accounts
- [ ] **API Rate Limiting** - Enterprise tier support
- [ ] **Security Alerts** - Real-time breach notifications

### Performance Improvements
- [ ] GPU acceleration via CUDA/OpenCL
- [ ] Distributed processing support
- [ ] Caching mechanism for common passwords
- [ ] Parallel batch analysis

### Testing & Documentation
- [ ] Increase test coverage to 95%+
- [ ] Add integration tests
- [ ] Performance benchmarks
- [ ] Video tutorials
- [ ] API documentation (Swagger/OpenAPI)

---

**Made with ❤️ for password security education**

Last Updated: November 28, 2025 | Version 2.0
