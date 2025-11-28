# 🔐 Password Audit Tool# 🔐 Password Audit Tool# Password Audit (lightweight)



A comprehensive, lightweight password auditing tool for assessing password strength through entropy analysis, pattern detection, and realistic crack time estimation.



**⚠️ Educational Use Only** - Designed for learning and assessment, not for performing attacks.A comprehensive, lightweight password auditing tool for assessing password strength through entropy analysis, pattern detection, and realistic crack time estimation.Simple Python CLI to evaluate how strong a password looks based on entropy



---estimates, common-password matches, and some naive pattern detections.



## ✨ Features**⚠️ Educational Use Only** - Designed for learning and assessment, not for performing attacks.



- **Entropy Calculation**: Pool-based and Shannon entropy analysisUsage:

- **Pattern Detection**: 7 different weakness patterns

- **Multiple Crack Scenarios**: CPU, GPU, and botnet simulations---

- **Security Levels**: 6-tier classification (CRITICAL to MASTER)

- **Hash Protection Simulation**: bcrypt and Argon2 penaltiesRun a single password:

- **Output Formats**: Human-readable colored output + JSON export

## ✨ Features

---

```bash

## 🚀 Quick Start

- **Entropy Calculation**: Pool-based and Shannon entropy analysispython cli.py -p "Tr0ub4dor&3"

```bash- **Pattern Detection**: 7 different weakness patterns

# Single password analysis- **Multiple Crack Scenarios**: CPU, GPU, and botnet simulations

python3 cli.py -p "MyPassword123!"- **Security Levels**: 6-tier classification (CRITICAL to MASTER)

- **Hash Protection Simulation**: bcrypt and Argon2 penalties

# Batch analysis from file- **Output Formats**: Human-readable colored output + JSON export

python3 cli.py -f passwords.txt

---

# JSON output for automation

python3 cli.py -p "Test123!" --json## 🚀 Quick Start



# Simulate GPU farm attack (1 trillion guesses/sec)```bash

python3 cli.py -p "Pass123" -g 1e12# Single password analysis

```python3 cli.py -p "MyPassword123!"



---# Batch analysis from file

python3 cli.py -f passwords.txt

## 🎯 Security Levels

# JSON output for automation

```python3 cli.py -p "Test123!" --json

🔴 CRITICAL (0-30 bits)        → Change immediately

🟠 WEAK (30-50 bits)           → Add length, mix types# Simulate GPU farm attack (1 trillion guesses/sec)

🟡 FAIR (50-70 bits)           → Acceptable, could improvepython3 cli.py -p "Pass123" -g 1e12

🟢 GOOD (70-90 bits)           → Strong password```

🟢 EXCELLENT (90-120 bits)     → Very strong

💎 MASTER (120+ bits)          → Exceptional strength---

```

## 🎯 Security Levels

---

```

## 📖 Usage🔴 CRITICAL (0-30 bits)

   → Instantly crackable

### Command Line Options   → Change immediately



```🟠 WEAK (30-50 bits)

python3 cli.py [OPTIONS]   → Cracklе in hours

   → Add length, mix character types

OPTIONS:

  -p, --password TEXT       Single password to analyze🟡 FAIR (50-70 bits)

  -f, --file TEXT          File with one password per line   → Cracks in days

  -g, --guesses FLOAT      Guesses per second (default: 1e9)   → Acceptable, but could be stronger

  --json                   Output in JSON format

  -h, --help               Show help message🟢 GOOD (70-90 bits)

```   → Cracks in years

   → Strong password - well done!

### Examples

🟢 EXCELLENT (90-120 bits)

```bash   → Cracks in centuries

# Analyze weak password   → Very strong password - excellent!

python3 cli.py -p "password"

💎 MASTER (120+ bits)

# Analyze strong password   → Cracks in millions of years

python3 cli.py -p "X9@mK2pLqR!zT4vW#5sUa"   → Exceptional strength - top tier!

```

# Batch process passwords from file

python3 cli.py -f my_passwords.txt---



# Export analysis to JSON## 📊 Example Output

python3 cli.py -p "Test123!" --json > result.json

```

# Simulate GPU (1 trillion guesses/sec)╔════════════════════════════════════════╗

python3 cli.py -p "Pass123" -g 1e12║ 🟡 Password Analysis - FAIR            ║

```╚════════════════════════════════════════╝

Basic Information:

---  Password: MyPass123

  Length: 9

## 🔬 How It Works

Entropy Analysis:

### Entropy Calculation  Pool Entropy: 53.59 bits

  Shannon Entropy: 26.53 bits

Pool-based entropy model:

Security Level:

```  🟡 FAIR - Fair

Entropy (bits) = log₂(pool_size) × length  Recommendation: Acceptable, but could be stronger

```

Crack Time (Brute Force):

**Character Types:**  Standard CPU: 156.68 hours (max)

- Lowercase (a-z): +26  Single GPU: 3.76 minutes (max)

- Uppercase (A-Z): +26  Large Botnet: 13.54 seconds (max)

- Digits (0-9): +10

- Symbols: +32With Hash Protection:

- Unicode/Emoji: +128  bcrypt: 85.85 days

- Spaces: +1  Argon2: 429.26 days



### Pattern Detection⚠️  Issues Found:

  • sequential-chars

Detects 7 weaknesses:  • year-like

```

| Pattern | Example | Risk |

|---------|---------|------|---

| Common Password | "password" | 🔴 Critical |

| Low Variation | "aaaa" | 🔴 Critical |## 📖 Usage Guide

| Repeated Chars | "passsword" | 🟠 Weak |

| Sequential | "abc123" | 🟠 Weak |### Command Line Options

| Year-like | "Pass1990" | 🟡 Fair |

| Single Case | "PASSWORD" | 🟡 Fair |```

| All Digits | "123456" | 🔴 Critical |python3 cli.py [OPTIONS]



### Attack ScenariosOPTIONS:

  -p, --password TEXT       Single password to analyze

- **CPU Single**: 1M guesses/sec  -f, --file TEXT          File with one password per line

- **CPU Multi**: 1B guesses/sec  -g, --guesses FLOAT      Guesses per second (default: 1e9)

- **GPU Single**: 1T guesses/sec  --json                   Output in JSON format

- **GPU Farm**: 10T guesses/sec  -h, --help               Show help message

- **Botnet**: 1000T guesses/sec```



### Hash Function Penalties### Usage Examples



- plaintext: 1x```bash

- MD5: 1x# Analyze weak password

- SHA256: 1xpython3 cli.py -p "password"

- **bcrypt: 200x** ✅

- **Argon2: 1000x** ✅# Analyze strong password

python3 cli.py -p "X9@mK2pLqR!zT4vW#5sUa"

---

# Batch process passwords from file

## 💡 Best Practicespython3 cli.py -f my_passwords.txt



### Strong Passwords ✅# Export analysis to JSON

python3 cli.py -p "Test123!" --json > result.json

```

DO:# Simulate modern multi-core CPU (1 billion guesses/sec)

✅ Use 12+ characters (16+ better)python3 cli.py -p "Pass123" -g 1e9

✅ Mix all character types

✅ Use random characters# Simulate single GPU (1 trillion guesses/sec)

✅ Use unique per accountpython3 cli.py -p "Pass123" -g 1e12

✅ Use passphrases: "Correct-Horse-Battery-Staple"

# Simulate GPU farm (10 trillion guesses/sec)

DON'T:python3 cli.py -p "Pass123" -g 1e13

❌ Dictionary words```

❌ Sequential patterns (abc, 123)

❌ Repeated characters (aaa)---

❌ Personal information

❌ Same password everywhere## 🔬 How It Works

```

### Entropy Calculation

### Examples

The tool uses **pool-based entropy**:

**Strong:**

``````

✅ X9@mK2pLqR!zT4vW#5sUa      (Master - 137 bits)Entropy (bits) = log₂(pool_size) × length

✅ BluePanda#Rocket42!7x       (Excellent - 104 bits)```

✅ Cr0wn$Jewel&Phoenix9        (Good - 76 bits)

```**Character Pool Sizes:**

- Lowercase letters (a-z): +26

**Weak:**- Uppercase letters (A-Z): +26

```- Digits (0-9): +10

❌ password              (37 bits)- ASCII symbols: +32

❌ 123456               (20 bits)- Unicode/Emoji: +128

❌ Pass123              (42 bits)- Spaces: +1

```

**Example:**

---```

Password: "Pass123!"

## 🔌 Python APIPool = 26 + 26 + 10 + 32 = 94 characters

Entropy = log₂(94) × 8 = 6.55 × 8 = 52.4 bits

```python```

from audit import analyze_password

### Shannon Entropy

# Analyze password

result = analyze_password("MyPassword123!")Measures statistical randomness based on character frequency:



# Get security level```

print(result["security_level"]["level"])H = -Σ(p_i × log₂(p_i))



# Get crack timeWhere p_i = probability of character i

print(result["estimated_crack_human"])```



# Check for issues**Key Insight:** Detects repetitive characters that score high in pool entropy but are actually weak.

print(result["issues"])

### Pattern Detection

# Custom attack speed (GPU)

result = analyze_password("Pass123", guesses_per_second=1e12)Identifies 7 common password weaknesses:

```

| Pattern | Detection | Example | Risk |

---|---------|-----------|---------|------|

| Common Password | Dictionary match | "password" | 🔴 Critical |

## 📊 Example Output| Low Variation | ≤2 unique chars | "aaaa" | 🔴 Critical |

| Repeated Chars | 3+ same in row | "passsword" | 🟠 Weak |

```| Sequential | Ascending/descending | "abc123" | 🟠 Weak |

╔════════════════════════════════════════╗| Year-like | 1900-2025 or 00-99 | "Pass1990" | 🟡 Fair |

║ 🟡 Password Analysis - FAIR            ║| Single Case | All upper or lower | "PASSWORD" | 🟡 Fair |

╚════════════════════════════════════════╝| All Digits | Only numbers | "123456" | 🔴 Critical |

Basic Information:

  Password: MyPass123### Crack Time Estimation

  Length: 9

Simulates different attack scenarios:

Entropy Analysis:

  Pool Entropy: 53.59 bits```

  Shannon Entropy: 26.53 bitsCrack Time = 2^entropy / guesses_per_second

```

Security Level:

  🟡 FAIR - Fair**Attack Scenarios:**

  Recommendation: Acceptable, but could be stronger

| Scenario | Speed | Device |

Crack Time (Brute Force):|----------|-------|--------|

  Standard CPU: 156.68 hours (max)| CPU Single | 1M/sec | Single core processor |

  Single GPU: 3.76 minutes (max)| CPU Multi | 1B/sec | Modern multi-core CPU |

  Large Botnet: 13.54 seconds (max)| GPU Single | 1T/sec | Single graphics card |

| GPU Farm | 10T/sec | 10 GPUs combined |

With Hash Protection:| Botnet | 1000T/sec | Large distributed network |

  bcrypt: 85.85 days

  Argon2: 429.26 days### Hash Function Penalties



⚠️  Issues Found:Real systems use hash functions that deliberately slow down cracking:

  • sequential-chars

  • year-like| Function | Speed Penalty | Use Case |

```|----------|--------------|----------|

| Plaintext | 1x | Dangerous (no hashing) |

---| MD5 | 1x | Weak, fast (avoid) |

| SHA256 | 1x | Fast, not ideal for passwords |

## ⚖️ Disclaimer| bcrypt | 200x | ✅ Good default |

| Argon2 | 1000x | ✅ Excellent choice |

This tool estimates password strength based on:| scrypt | 1000x | ✅ Very good option |

- Brute-force attack assumptions

- Simplified hash function penalties---

- Statistical models

## 💡 Best Practices for Strong Passwords

**Real Security Requires:**

- Proper hash function implementation### DO ✅

- Strong salt usage

- Account lockout policies- Use **12+ characters** (16+ is better)

- Multi-factor authentication- Mix **all character types**:

  - Uppercase: A-Z

---  - Lowercase: a-z

  - Digits: 0-9

## 📚 References  - Symbols: !@#$%^&*

- Use **random characters** (not patterns)

- [NIST Password Guidelines](https://pages.nist.gov/800-63-3/)- Use **unique passwords** per account

- [Information Entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory))- Use **passphrase method**: "Correct-Horse-Battery-Staple"

- [Password Cracking](https://en.wikipedia.org/wiki/Password_cracking)

- [Cryptographic Hash Functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function)### DON'T ❌



---- Dictionary words: "password", "baseball"

- Sequential patterns: "abc", "123", "qwerty"

**Made with ❤️ for password security education**- Repeated characters: "aaa", "111"

- Personal info: birth dates, names

Version: 2.0 (Professional Edition)- Common substitutions: "p@ssw0rd" (easily guessed)

Last Updated: November 26, 2025- Same password everywhere


### Example Passwords

**STRONG Passwords:**
```
✅ X9@mK2pLqR!zT4vW#5sUa      (Master Level - 137 bits)
✅ BluePanda#Rocket42!7x       (Excellent - 104 bits)
✅ Cr0wn$Jewel&Phoenix9        (Good - 76 bits)
✅ J@zz#Trumpet$Music*1988     (Fair - 68 bits)
```

**WEAK Passwords:**
```
❌ password                (Common, single case - 37 bits)
❌ 123456                 (Sequential, all digits - 20 bits)
❌ Pass123                (Sequential, year-like - 42 bits)
❌ aaaaaaa                (Repetitive, no variation - 0 bits)
❌ john1990               (Name + year - 35 bits)
```

---

## 🔌 Python API

### Installation

```bash
# Optional: Install termcolor for colored output
pip install termcolor
```

### Basic Usage

```python
from audit import analyze_password
import json

# Analyze a password
result = analyze_password("MyPassword123!")

# Print security level
print(result["security_level"]["level"])  # Output: FAIR
print(result["security_level"]["emoji"])  # Output: 🟡

# Print crack time
print(result["estimated_crack_human"])     # Output: 70.55 hours

# Print issues
if result["issues"]:
    print("Issues:", result["issues"])
else:
    print("No issues found!")

# Export to JSON
with open("analysis.json", "w") as f:
    json.dump(result, f, indent=2)
```

### Advanced Usage

```python
from audit import analyze_password, entropy_bits, shannon_entropy

# Get just entropy values
pw = "MyPassword123!"
pool_entropy = entropy_bits(pw)
shannon = shannon_entropy(pw)
print(f"Pool Entropy: {pool_entropy:.2f} bits")
print(f"Shannon Entropy: {shannon:.2f} bits")

# Simulate different attack scenarios
result = analyze_password(pw, guesses_per_second=1e12)  # GPU
print(result["estimated_crack_human"])  # Time with GPU

# Batch processing
passwords = ["password", "Pass123", "X9@mK2pL"]
for pw in passwords:
    result = analyze_password(pw)
    print(f"{pw}: {result['security_level']['level']}")
```

---

## 📚 Output Formats

### Human-Readable (Default)

```bash
python3 cli.py -p "Test123!"
```

Colorful, organized display with:
- Basic information
- Entropy analysis
- Security level & recommendations
- Crack time for different scenarios
- Hash protection impact
- Pattern warnings

### JSON Format

```bash
python3 cli.py -p "Test123!" --json
```

Machine-readable output with all metrics:
```json
{
  "password": "Test123!",
  "length": 8,
  "entropy_bits": 52.44,
  "shannon_bits": 24.0,
  "security_level": {
    "level": "FAIR",
    "emoji": "🟡",
    "description": "Fair",
    "recommendation": "Acceptable, but could be stronger"
  },
  "crack_scenarios": {
    "cpu_single": {...},
    "cpu_multi": {...},
    "gpu_single": {...},
    "gpu_farm": {...},
    "distributed": {...}
  },
  "with_hash_protection": {
    "bcrypt": {...},
    "argon2": {...}
  },
  "issues": ["sequential-chars"]
}
```

---

## ⚖️ Important Disclaimers

### What This Tool Does ✅
- Estimates password entropy based on character analysis
- Detects common weak password patterns
- Simulates brute-force attack scenarios
- Provides security recommendations

### What This Tool Does NOT ✅
- Replace proper authentication systems
- Account for phishing or social engineering
- Test against specific hash implementations
- Guarantee actual security (use proper security practices)

### Real Security Requires ✅
- Proper hash function implementation
- Strong salt usage
- Account lockout policies
- Multi-factor authentication
- Regular security updates

---

## 🤝 Contributing

Found an issue or have suggestions? Contributions welcome!

### Potential Improvements
- Support for language-specific dictionaries
- Keyboard walk pattern detection
- Configuration file support
- Progress bars for batch processing
- Performance optimizations

---

## 📚 References

- [NIST Password Guidelines](https://pages.nist.gov/800-63-3/)
- [Information Entropy - Wikipedia](https://en.wikipedia.org/wiki/Entropy_(information_theory))
- [Password Cracking - Wikipedia](https://en.wikipedia.org/wiki/Password_cracking)
- [Cryptographic Hash Functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function)
- [Passphrase Security](https://xkcd.com/936/)

---

## 🔗 Related Tools

- **[zxcvbn](https://github.com/dropbox/zxcvbn)** - JavaScript password strength estimator
- **[hashcat](https://hashcat.net/)** - Password cracking tool
- **[John the Ripper](https://www.openwall.com/john/)** - Password auditing software

---

**Made with ❤️ for password security education**

Last Updated: November 26, 2025
Version: 2.0 (Professional Edition)
