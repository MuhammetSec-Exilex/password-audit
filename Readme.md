# 🔐 Password Audit Tool

Comprehensive password auditing tool for assessing strength through entropy analysis, pattern detection, and crack time estimation.

**⚠️ Educational Use Only**

---

## 🚀 Quick Start

```bash
python3 cli.py                               # Interactive mode (secure, masked input)
python3 cli.py -p "MyPassword123!"           # Analyze password via argument
python3 cli.py -p "MyPassword123!" -w Wordlists/100k-most-used-passwords-NCSC.txt  # Custom wordlist
python3 cli.py -f passwords.txt              # Batch analysis
python3 cli.py -p "Pass123!" --json          # JSON output
python3 cli.py -p "Pass123" -g 1e12          # GPU simulation
```

---

## 🔑 Secure Password Input (v1.1)

### Hybrid Input Approach

The tool now supports **two ways** to provide passwords for analysis:

#### 1️⃣ Interactive Mode (Recommended)
Simply run the tool without the `-p` flag:
```bash
python3 cli.py
```
You'll be securely prompted to enter your password. The input is:
- ✅ **Masked** (hidden on screen for privacy)
- ✅ **Bypasses shell interpretation** (no issues with special characters like `!`, `$`, `&`, `*`)
- ✅ **No quoting needed** - enter passwords exactly as they are

#### 2️⃣ Command-Line Argument
Provide password directly via the `-p` flag:
```bash
python3 cli.py -p 'MyP@ss$123!'
```
**Note:** You must quote passwords with special characters to prevent shell interpretation errors.

### Why Interactive Mode?

**Problem:** Shell special characters (`!`, `$`, `&`, etc.) cause issues when passed as arguments.

**Examples of issues:**
```bash
python3 cli.py -p MyPass!123      # ❌ Shell interprets ! as history expansion
python3 cli.py -p Pass$word       # ❌ Shell interprets $ as variable
python3 cli.py -p "Pass!123"      # ✅ Works but requires quoting
python3 cli.py                     # ✅✅ Best: Interactive mode (no shell issues)
```

**Solution:** Interactive mode using `getpass` library reads input directly, completely bypassing shell interpretation.

---

## � New Features in v1.1

### 🔍 Spatial Keyboard Pattern Detection

The tool now detects **keyboard layout patterns** - common weak password patterns where users type adjacent keys.

#### What It Detects:

**QWERTY Keyboard Patterns:**
- Number row: `1234567890`
- Symbol row: `!@#$%^&*()`
- Letter rows: `qwerty`, `asdfgh`, `zxcvbn`
- Both forward (`qwe`) and reverse (`ewq`) sequences

**Numeric Keypad Patterns:**
- Rows: `789`, `456`, `123`
- Columns: `741`, `852`, `963`
- Diagonals: `753`, `159`

#### Examples:

```bash
# Passwords WITH spatial patterns (weak):
qwerty          # QWERTY top row
asdfgh          # QWERTY home row
!@#$            # Shifted number row
789456          # Numpad rows
ewq             # Reverse of 'qwe'

# Passwords WITHOUT spatial patterns (better):
MyP@ssword!     # Random arrangement
SecureR@nd0m    # No keyboard sequence
```

#### How It Works:

- **Case-insensitive:** Detects both `QWERTY` and `qwerty`
- **Minimum length:** 3+ consecutive keyboard characters
- **Bidirectional:** Catches forward and reverse patterns
- **Comprehensive:** Checks all QWERTY rows and numpad layouts

---

## �🎯 Security Levels

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
  -w, --wordlist TEXT    Path to password wordlist (default: Wordlists/100k-most-used-passwords-NCSC.txt)
  --json                 JSON output
  -h, --help             Help message
```

**Input security limit:**
- Maximum password length is **512 characters**.
- If exceeded, the program exits gracefully with:  
  `Error: Input exceeds the maximum allowed length of 512 characters.`
- Leading and trailing whitespace is automatically stripped from input (spaces, tabs, newlines), while internal spaces are preserved for passphrases.
- Input is also blocked if it contains **illegal control characters** (e.g., null byte, escape/control sequences).
- If detected, the program exits with:  
  `Error: Illegal control characters detected in input.`

---

## 📚 Common Password Wordlist

The tool now loads **common passwords dynamically** from a wordlist file.

**Default file:**
```
Wordlists/100k-most-used-passwords-NCSC.txt
```

**What happens at runtime:**
- The wordlist is read line by line
- Each entry is lowercased and stored in a Python `set` for fast $O(1)$ lookups
- In `audit.py` module mode, a short status message prints the file path and count

**Custom wordlist:**
```bash
python3 cli.py -p "MyPassword123!" -w Wordlists/your-list.txt
```

**Tests:**
- A lightweight test wordlist is stored at:
  `Wordlists/wordlist_for_test_audit.txt`
- It contains the **first 10 lines** of the main list to verify loading works

---

## 🧪 Running Tests

### Terminal (Recommended)

```bash
# Run all tests
./venv/bin/python -m pytest test_audit.py -q

# Run with verbose output
./venv/bin/python -m pytest test_audit.py -v

# Run only input validation tests (length + control characters)
./venv/bin/python -m pytest test_audit.py::TestInputValidation -q
```

### If terminal is not available (VS Code UI)

1. Open **Testing** panel in VS Code (beaker icon).
2. Click **Configure Python Tests** (choose **pytest**).
3. Select `test_audit.py` or a specific test class.
4. Click **Run** from the Testing panel.

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

### 9 Patterns Detected (Updated in v1.1)

1. **Common Password** - Dictionary match against known breached passwords
2. **Low Variation** - ≤2 unique characters (weak entropy)
3. **Repeated Chars** - 3+ identical characters in a row
4. **Sequential** - Ascending/descending sequences (abc, 123, xyz)
5. **Spatial Pattern** - Keyboard layouts (qwerty, asdf, 789, !@#) ⭐ NEW
6. **Year-like** - Year patterns (1900-2025 or 00-99)
7. **Missing Uppercase** - Has letters but no uppercase (e.g., "password!") ⭐ IMPROVED
8. **Missing Lowercase** - Has letters but no lowercase (e.g., "PASSWORD123") ⭐ IMPROVED
9. **All Digits** - Only numeric digits

**Note:** The case detection logic was improved to be more accurate. Passwords with symbols like `abc!@#` will now correctly show `missing-uppercase` instead of the misleading `single-case` flag.

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
from audit import analyze_password, entropy_bits, shannon_entropy, _check_spatial_patterns

pw = "MyPassword123!"
print(f"Pool Entropy: {entropy_bits(pw):.2f} bits")
print(f"Shannon Entropy: {shannon_entropy(pw):.2f} bits")

# Check for spatial patterns
has_spatial = _check_spatial_patterns(pw)
print(f"Has spatial pattern: {has_spatial}")  # False

# GPU simulation
result = analyze_password(pw, guesses_per_second=1e12)
print(result["estimated_crack_human"])

# Check spatial patterns in different passwords
print(_check_spatial_patterns("qwerty"))      # True
print(_check_spatial_patterns("asdfgh"))      # True
print(_check_spatial_patterns("SecureKey!"))  # False
```

---

## 📊 Example Output

### Example 1: Weak Password with Spatial Pattern

```bash
python3 cli.py -p "qwerty123"
```

```
╔════════════════════════════════════════╗
║ 🟠 Password Analysis - WEAK            ║
╚════════════════════════════════════════╝

Basic Information:
  Password: qwerty123
  Length: 9

Entropy Analysis:
  Pool Entropy: 46.53 bits
  Shannon Entropy: 28.52 bits

Security Level:
  🟠 WEAK - Add length, mix character types

Crack Time (Brute Force):
  Standard CPU: 235.53 days (max)
  Single GPU: 2.06 minutes (max)
  Large Botnet: 7.43 seconds (max)

With Hash Protection:
  bcrypt: 47.11 days
  Argon2: 235.53 days

⚠️  Issues Found:
  • common-password
  • sequential-chars
  • missing-uppercase
  • spatial-pattern ⭐ NEW
  • year-like
```

### Example 2: Strong Password (No Issues)

```bash
python3 cli.py -p "MySecureP@ss!"
```

```
╔════════════════════════════════════════╗
║ 🟢 Password Analysis - GOOD            ║
╚════════════════════════════════════════╝

Basic Information:
  Password: MySecureP@ss!
  Length: 13

Entropy Analysis:
  Pool Entropy: 83.10 bits
  Shannon Entropy: 45.26 bits

Security Level:
  🟢 GOOD - Strong password - well done!

Crack Time (Brute Force):
  Standard CPU: >= 1.32 years (max)
  Single GPU: 4.83 days (max)
  Large Botnet: 2.12 hours (max)

With Hash Protection:
  bcrypt: >= 262.94 years
  Argon2: >= 1314.70 years

✅ No issues detected!
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
- [x] **Keyboard Pattern Detection** - Detect QWERTY, DVORAK patterns ✅ (v1.1)
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

## 📝 Changelog

### Version 1.1.4 (March 2, 2026)
- ✅ Added second defensive input-validation layer for illegal control characters (`\x00`, escape/control sequences)
- ✅ Validation is executed before analysis/regex operations and exits with code `1` on violation
- ✅ Expanded `TestInputValidation` coverage for both `cli.py` and `audit.py` entry points

### Version 1.1.3 (March 2, 2026)
- ✅ Added defensive input-length validation (max **512** chars) to prevent ReDoS risk at entry points
- ✅ Validation runs before analysis/regex processing and exits with code `1` on violation
- ✅ Added tests in `test_audit.py` for both `cli.py` and `audit.py` main entry points
- ✅ Added README instructions for running tests (terminal + VS Code Testing panel)

### Version 1.1.2 (February 19, 2026)
- ✅ Replaced hardcoded common-password set with **dynamic wordlist loading**
- ✅ Added `-w/--wordlist` option for custom lists
- ✅ Added test wordlist file for reliable loading verification

### Version 1.1.1 (February 17, 2026)
- ✅ **Improved Case Detection Logic** - Replaced generic `single-case` with granular `missing-uppercase` and `missing-lowercase` flags
- ✅ Fixed misleading case detection for passwords with symbols (e.g., `abc!@#` now correctly shows `missing-uppercase`)
- ✅ Case checks now only apply when password contains letters
- ✅ Enhanced pattern detection from 8 to 9 patterns
- ✅ Added 2 new comprehensive test cases for case detection

### Version 1.1 (February 16, 2026)
- ✅ Added **Spatial Keyboard Pattern Detection** - Detects QWERTY and numpad patterns
- ✅ Added **Hybrid Input Approach** - Interactive mode with `getpass` for secure password entry
- ✅ Enhanced pattern detection from 7 to 8 patterns
- ✅ Added comprehensive test suite for spatial patterns (16 new tests)
- ✅ Improved security by bypassing shell interpretation issues

### Version 1.0 (November 28, 2025)
- Initial comprehensive release

---

Last Updated: March 2, 2026 | Version 1.1.4
