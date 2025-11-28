# 🔐 Password Audit Tool# 🔐 Password Audit Tool# 🔐 Password Audit Tool# Password Audit (lightweight)



A comprehensive, lightweight password auditing tool for assessing password strength through entropy analysis, pattern detection, and realistic crack time estimation.



**⚠️ Educational Use Only** - Designed for learning and assessment, not for performing attacks.A comprehensive, lightweight password auditing tool for assessing password strength through entropy analysis, pattern detection, and realistic crack time estimation.



---



## ✨ Features**⚠️ Educational Use Only** - Designed for learning and assessment, not for performing attacks.A comprehensive, lightweight password auditing tool for assessing password strength through entropy analysis, pattern detection, and realistic crack time estimation.Simple Python CLI to evaluate how strong a password looks based on entropy



- **Entropy Calculation**: Pool-based and Shannon entropy analysis

- **Pattern Detection**: 7 different weakness patterns

- **Multiple Crack Scenarios**: CPU, GPU, and botnet simulations---estimates, common-password matches, and some naive pattern detections.

- **Security Levels**: 6-tier classification (CRITICAL to MASTER)

- **Hash Protection Simulation**: bcrypt and Argon2 penalties

- **Output Formats**: Human-readable colored output + JSON export

## ✨ Features**⚠️ Educational Use Only** - Designed for learning and assessment, not for performing attacks.

---



## 🚀 Quick Start

- **Entropy Calculation**: Pool-based and Shannon entropy analysisUsage:

### Single Password Analysis

- **Pattern Detection**: 7 different weakness patterns

```bash

python3 cli.py -p "MyPassword123!"- **Multiple Crack Scenarios**: CPU, GPU, and botnet simulations---

```

- **Security Levels**: 6-tier classification (CRITICAL to MASTER)

### Batch Analysis from File

- **Hash Protection Simulation**: bcrypt and Argon2 penaltiesRun a single password:

```bash

python3 cli.py -f passwords.txt- **Output Formats**: Human-readable colored output + JSON export

```

## ✨ Features

### JSON Output for Automation

---

```bash

python3 cli.py -p "Test123!" --json```bash

```

## 🚀 Quick Start

### Simulate GPU Farm Attack (1 trillion guesses/sec)

- **Entropy Calculation**: Pool-based and Shannon entropy analysispython cli.py -p "Tr0ub4dor&3"

```bash

python3 cli.py -p "Pass123" -g 1e12```bash- **Pattern Detection**: 7 different weakness patterns

```

# Single password analysis- **Multiple Crack Scenarios**: CPU, GPU, and botnet simulations

---

python3 cli.py -p "MyPassword123!"- **Security Levels**: 6-tier classification (CRITICAL to MASTER)

## 🎯 Security Levels

- **Hash Protection Simulation**: bcrypt and Argon2 penalties

| Level | Range | Emoji | Meaning | Action |

|-------|-------|-------|---------|--------|# Batch analysis from file- **Output Formats**: Human-readable colored output + JSON export

| CRITICAL | 0-30 bits | 🔴 | Instantly crackable | Change immediately |

| WEAK | 30-50 bits | 🟠 | Cracks in hours | Add length, mix types |python3 cli.py -f passwords.txt

| FAIR | 50-70 bits | 🟡 | Cracks in days | Acceptable, could improve |

| GOOD | 70-90 bits | 🟢 | Cracks in years | Strong password |---

| EXCELLENT | 90-120 bits | 🟢 | Cracks in centuries | Very strong |

| MASTER | 120+ bits | 💎 | Millions of years | Exceptional |# JSON output for automation



---python3 cli.py -p "Test123!" --json## 🚀 Quick Start



## 📖 Usage Guide



### Command Line Options# Simulate GPU farm attack (1 trillion guesses/sec)```bash



```python3 cli.py -p "Pass123" -g 1e12# Single password analysis

python3 cli.py [OPTIONS]

```python3 cli.py -p "MyPassword123!"

OPTIONS:

  -p, --password TEXT       Single password to analyze

  -f, --file TEXT          File with one password per line

  -g, --guesses FLOAT      Guesses per second (default: 1e9)---# Batch analysis from file

  --json                   Output in JSON format

  -h, --help               Show help messagepython3 cli.py -f passwords.txt

```

## 🎯 Security Levels

### Usage Examples

# JSON output for automation

```bash

# Analyze weak password```python3 cli.py -p "Test123!" --json

python3 cli.py -p "password"

🔴 CRITICAL (0-30 bits)        → Change immediately

# Analyze strong password

python3 cli.py -p "X9@mK2pLqR!zT4vW#5sUa"🟠 WEAK (30-50 bits)           → Add length, mix types# Simulate GPU farm attack (1 trillion guesses/sec)



# Batch process passwords🟡 FAIR (50-70 bits)           → Acceptable, could improvepython3 cli.py -p "Pass123" -g 1e12

python3 cli.py -f my_passwords.txt

🟢 GOOD (70-90 bits)           → Strong password```

# Export to JSON

python3 cli.py -p "Test123!" --json > result.json🟢 EXCELLENT (90-120 bits)     → Very strong



# Simulate CPU (default, 1 billion guesses/sec)💎 MASTER (120+ bits)          → Exceptional strength---

python3 cli.py -p "Pass123" -g 1e9

```

# Simulate GPU (1 trillion guesses/sec)

python3 cli.py -p "Pass123" -g 1e12## 🎯 Security Levels



# Simulate GPU farm (10 trillion guesses/sec)---

python3 cli.py -p "Pass123" -g 1e13

``````



---## 📖 Usage🔴 CRITICAL (0-30 bits)



## 📊 Example Output   → Instantly crackable



```### Command Line Options   → Change immediately

╔════════════════════════════════════════╗

║ 🟡 Password Analysis - FAIR            ║

╚════════════════════════════════════════╝

```🟠 WEAK (30-50 bits)

Basic Information:

  Password: MyPass123python3 cli.py [OPTIONS]   → Cracklе in hours

  Length: 9

   → Add length, mix character types

Entropy Analysis:

  Pool Entropy: 53.59 bitsOPTIONS:

  Shannon Entropy: 26.53 bits

  -p, --password TEXT       Single password to analyze🟡 FAIR (50-70 bits)

Security Level:

  🟡 FAIR - Fair  -f, --file TEXT          File with one password per line   → Cracks in days

  Recommendation: Acceptable, but could be stronger

  -g, --guesses FLOAT      Guesses per second (default: 1e9)   → Acceptable, but could be stronger

Crack Time (Brute Force):

  Standard CPU: 156.68 hours (max)  --json                   Output in JSON format

  Single GPU: 3.76 minutes (max)

  Large Botnet: 13.54 seconds (max)  -h, --help               Show help message🟢 GOOD (70-90 bits)



With Hash Protection:```   → Cracks in years

  bcrypt: 85.85 days

  Argon2: 429.26 days   → Strong password - well done!



⚠️  Issues Found:### Examples

  • sequential-chars

  • year-like🟢 EXCELLENT (90-120 bits)

```

```bash   → Cracks in centuries

---

# Analyze weak password   → Very strong password - excellent!

## 🔬 How It Works

python3 cli.py -p "password"

### Entropy Calculation

💎 MASTER (120+ bits)

The tool uses **pool-based entropy**:

# Analyze strong password   → Cracks in millions of years

```

Entropy (bits) = log₂(pool_size) × lengthpython3 cli.py -p "X9@mK2pLqR!zT4vW#5sUa"   → Exceptional strength - top tier!

```

```

**Character Pool Sizes:**

- Lowercase letters (a-z): +26# Batch process passwords from file

- Uppercase letters (A-Z): +26

- Digits (0-9): +10python3 cli.py -f my_passwords.txt---

- ASCII symbols: +32

- Unicode/Emoji: +128

- Spaces: +1

# Export analysis to JSON## 📊 Example Output

**Example:**

```python3 cli.py -p "Test123!" --json > result.json

Password: "Pass123!"

Pool = 26 + 26 + 10 + 32 = 94 characters```

Entropy = log₂(94) × 8 = 6.55 × 8 = 52.4 bits

```# Simulate GPU (1 trillion guesses/sec)╔════════════════════════════════════════╗



### Shannon Entropypython3 cli.py -p "Pass123" -g 1e12║ 🟡 Password Analysis - FAIR            ║



Measures statistical randomness based on character frequency:```╚════════════════════════════════════════╝



```Basic Information:

H = -Σ(p_i × log₂(p_i))

```---  Password: MyPass123



Where p_i = probability of character i  Length: 9



**Key Insight:** Detects repetitive characters that score high in pool entropy but are actually weak.## 🔬 How It Works



### Pattern DetectionEntropy Analysis:



Identifies 7 common password weaknesses:### Entropy Calculation  Pool Entropy: 53.59 bits



| Pattern | Detection | Example | Risk |  Shannon Entropy: 26.53 bits

|---------|-----------|---------|------|

| Common Password | Dictionary match | "password" | 🔴 Critical |Pool-based entropy model:

| Low Variation | ≤2 unique chars | "aaaa" | 🔴 Critical |

| Repeated Chars | 3+ same in row | "passsword" | 🟠 Weak |Security Level:

| Sequential | Ascending/descending | "abc123" | 🟠 Weak |

| Year-like | 1900-2025 or 00-99 | "Pass1990" | 🟡 Fair |```  🟡 FAIR - Fair

| Single Case | All upper or lower | "PASSWORD" | 🟡 Fair |

| All Digits | Only numbers | "123456" | 🔴 Critical |Entropy (bits) = log₂(pool_size) × length  Recommendation: Acceptable, but could be stronger



### Crack Time Estimation```



Simulates different attack scenarios:Crack Time (Brute Force):



```**Character Types:**  Standard CPU: 156.68 hours (max)

Crack Time = 2^entropy / guesses_per_second

```- Lowercase (a-z): +26  Single GPU: 3.76 minutes (max)



**Attack Scenarios:**- Uppercase (A-Z): +26  Large Botnet: 13.54 seconds (max)



| Scenario | Speed | Device |- Digits (0-9): +10

|----------|-------|--------|

| CPU Single | 1M/sec | Single core processor |- Symbols: +32With Hash Protection:

| CPU Multi | 1B/sec | Modern multi-core CPU |

| GPU Single | 1T/sec | Single graphics card |- Unicode/Emoji: +128  bcrypt: 85.85 days

| GPU Farm | 10T/sec | 10 GPUs combined |

| Botnet | 1000T/sec | Large distributed network |- Spaces: +1  Argon2: 429.26 days



### Hash Function Penalties



Real systems use hash functions that deliberately slow down cracking:### Pattern Detection⚠️  Issues Found:



| Function | Speed Penalty | Use Case |  • sequential-chars

|----------|--------------|----------|

| Plaintext | 1x | Dangerous (no hashing) |Detects 7 weaknesses:  • year-like

| MD5 | 1x | Weak, fast (avoid) |

| SHA256 | 1x | Fast, not ideal for passwords |```

| bcrypt | 200x | ✅ Good default |

| Argon2 | 1000x | ✅ Excellent choice || Pattern | Example | Risk |

| scrypt | 1000x | ✅ Very good option |

|---------|---------|------|---

---

| Common Password | "password" | 🔴 Critical |

## 💡 Best Practices for Strong Passwords

| Low Variation | "aaaa" | 🔴 Critical |## 📖 Usage Guide

### DO ✅

| Repeated Chars | "passsword" | 🟠 Weak |

- Use **12+ characters** (16+ is better)

- Mix **all character types**:| Sequential | "abc123" | 🟠 Weak |### Command Line Options

  - Uppercase: A-Z

  - Lowercase: a-z| Year-like | "Pass1990" | 🟡 Fair |

  - Digits: 0-9

  - Symbols: !@#$%^&*| Single Case | "PASSWORD" | 🟡 Fair |```

- Use **random characters** (not patterns)

- Use **unique passwords** per account| All Digits | "123456" | 🔴 Critical |python3 cli.py [OPTIONS]

- Use **passphrase method**: "Correct-Horse-Battery-Staple"



### DON'T ❌

### Attack ScenariosOPTIONS:

- Dictionary words: "password", "baseball"

- Sequential patterns: "abc", "123", "qwerty"  -p, --password TEXT       Single password to analyze

- Repeated characters: "aaa", "111"

- Personal info: birth dates, names- **CPU Single**: 1M guesses/sec  -f, --file TEXT          File with one password per line

- Common substitutions: "p@ssw0rd" (easily guessed)

- Same password everywhere- **CPU Multi**: 1B guesses/sec  -g, --guesses FLOAT      Guesses per second (default: 1e9)



### Example Passwords- **GPU Single**: 1T guesses/sec  --json                   Output in JSON format



**STRONG Passwords:**- **GPU Farm**: 10T guesses/sec  -h, --help               Show help message

```

✅ X9@mK2pLqR!zT4vW#5sUa      (Master - 137 bits)- **Botnet**: 1000T guesses/sec```

✅ BluePanda#Rocket42!7x       (Excellent - 104 bits)

✅ Cr0wn$Jewel&Phoenix9        (Good - 76 bits)

✅ J@zz#Trumpet$Music*1988     (Fair - 68 bits)

```### Hash Function Penalties### Usage Examples



**WEAK Passwords:**

```

❌ password              (Common, single case - 37 bits)- plaintext: 1x```bash

❌ 123456               (Sequential, all digits - 20 bits)

❌ Pass123              (Sequential, year-like - 42 bits)- MD5: 1x# Analyze weak password

❌ aaaaaaa              (Repetitive, no variation - 0 bits)

❌ john1990             (Name + year - 35 bits)- SHA256: 1xpython3 cli.py -p "password"

```

- **bcrypt: 200x** ✅

---

- **Argon2: 1000x** ✅# Analyze strong password

## 🔌 Python API

python3 cli.py -p "X9@mK2pLqR!zT4vW#5sUa"

### Installation

---

```bash

# Optional: Install termcolor for colored output# Batch process passwords from file

pip install termcolor

```## 💡 Best Practicespython3 cli.py -f my_passwords.txt



### Basic Usage



```python### Strong Passwords ✅# Export analysis to JSON

from audit import analyze_password

import jsonpython3 cli.py -p "Test123!" --json > result.json



# Analyze a password```

result = analyze_password("MyPassword123!")

DO:# Simulate modern multi-core CPU (1 billion guesses/sec)

# Print security level

print(result["security_level"]["level"])  # Output: FAIR✅ Use 12+ characters (16+ better)python3 cli.py -p "Pass123" -g 1e9

print(result["security_level"]["emoji"])  # Output: 🟡

✅ Mix all character types

# Print crack time

print(result["estimated_crack_human"])     # Output: 70.55 hours✅ Use random characters# Simulate single GPU (1 trillion guesses/sec)



# Print issues✅ Use unique per accountpython3 cli.py -p "Pass123" -g 1e12

if result["issues"]:

    print("Issues:", result["issues"])✅ Use passphrases: "Correct-Horse-Battery-Staple"

else:

    print("No issues found!")# Simulate GPU farm (10 trillion guesses/sec)



# Export to JSONDON'T:python3 cli.py -p "Pass123" -g 1e13

with open("analysis.json", "w") as f:

    json.dump(result, f, indent=2)❌ Dictionary words```

```

❌ Sequential patterns (abc, 123)

### Advanced Usage

❌ Repeated characters (aaa)---

```python

from audit import analyze_password, entropy_bits, shannon_entropy❌ Personal information



# Get just entropy values❌ Same password everywhere## 🔬 How It Works

pw = "MyPassword123!"

pool_entropy = entropy_bits(pw)```

shannon = shannon_entropy(pw)

print(f"Pool Entropy: {pool_entropy:.2f} bits")### Entropy Calculation

print(f"Shannon Entropy: {shannon:.2f} bits")

### Examples

# Simulate different attack scenarios

result = analyze_password(pw, guesses_per_second=1e12)  # GPUThe tool uses **pool-based entropy**:

print(result["estimated_crack_human"])  # Time with GPU

**Strong:**

# Batch processing

passwords = ["password", "Pass123", "X9@mK2pL"]``````

for pw in passwords:

    result = analyze_password(pw)✅ X9@mK2pLqR!zT4vW#5sUa      (Master - 137 bits)Entropy (bits) = log₂(pool_size) × length

    print(f"{pw}: {result['security_level']['level']}")

```✅ BluePanda#Rocket42!7x       (Excellent - 104 bits)```



---✅ Cr0wn$Jewel&Phoenix9        (Good - 76 bits)



## 📚 Output Formats```**Character Pool Sizes:**



### Human-Readable (Default)- Lowercase letters (a-z): +26



```bash**Weak:**- Uppercase letters (A-Z): +26

python3 cli.py -p "Test123!"

``````- Digits (0-9): +10



Colorful, organized display with:❌ password              (37 bits)- ASCII symbols: +32

- Basic information

- Entropy analysis❌ 123456               (20 bits)- Unicode/Emoji: +128

- Security level & recommendations

- Crack time for different scenarios❌ Pass123              (42 bits)- Spaces: +1

- Hash protection impact

- Pattern warnings```



### JSON Format**Example:**



```bash---```

python3 cli.py -p "Test123!" --json

```Password: "Pass123!"



Machine-readable output with all metrics:## 🔌 Python APIPool = 26 + 26 + 10 + 32 = 94 characters

```json

{Entropy = log₂(94) × 8 = 6.55 × 8 = 52.4 bits

  "password": "Test123!",

  "length": 8,```python```

  "entropy_bits": 52.44,

  "shannon_bits": 24.0,from audit import analyze_password

  "security_level": {

    "level": "FAIR",### Shannon Entropy

    "emoji": "🟡",

    "description": "Fair",# Analyze password

    "recommendation": "Acceptable, but could be stronger"

  },result = analyze_password("MyPassword123!")Measures statistical randomness based on character frequency:

  "crack_scenarios": {

    "cpu_single": {...},

    "cpu_multi": {...},

    "gpu_single": {...},# Get security level```

    "gpu_farm": {...},

    "distributed": {...}print(result["security_level"]["level"])H = -Σ(p_i × log₂(p_i))

  },

  "with_hash_protection": {

    "bcrypt": {...},

    "argon2": {...}# Get crack timeWhere p_i = probability of character i

  },

  "issues": ["sequential-chars"]print(result["estimated_crack_human"])```

}

```



---# Check for issues**Key Insight:** Detects repetitive characters that score high in pool entropy but are actually weak.



## ⚖️ Important Disclaimersprint(result["issues"])



### What This Tool Does ✅### Pattern Detection

- Estimates password entropy based on character analysis

- Detects common weak password patterns# Custom attack speed (GPU)

- Simulates brute-force attack scenarios

- Provides security recommendationsresult = analyze_password("Pass123", guesses_per_second=1e12)Identifies 7 common password weaknesses:



### What This Tool Does NOT Do ❌```

- Replace proper authentication systems

- Account for phishing or social engineering| Pattern | Detection | Example | Risk |

- Test against specific hash implementations

- Guarantee actual security (use proper security practices)---|---------|-----------|---------|------|



### Real Security Requires ✅| Common Password | Dictionary match | "password" | 🔴 Critical |

- Proper hash function implementation

- Strong salt usage## 📊 Example Output| Low Variation | ≤2 unique chars | "aaaa" | 🔴 Critical |

- Account lockout policies

- Multi-factor authentication| Repeated Chars | 3+ same in row | "passsword" | 🟠 Weak |

- Regular security updates

```| Sequential | Ascending/descending | "abc123" | 🟠 Weak |

---

╔════════════════════════════════════════╗| Year-like | 1900-2025 or 00-99 | "Pass1990" | 🟡 Fair |

## 🤝 Contributing

║ 🟡 Password Analysis - FAIR            ║| Single Case | All upper or lower | "PASSWORD" | 🟡 Fair |

Found an issue or have suggestions? Contributions welcome!

╚════════════════════════════════════════╝| All Digits | Only numbers | "123456" | 🔴 Critical |

### Potential Improvements

- Support for language-specific dictionariesBasic Information:

- Keyboard walk pattern detection

- Configuration file support  Password: MyPass123### Crack Time Estimation

- Progress bars for batch processing

- Performance optimizations  Length: 9



---Simulates different attack scenarios:



## 📚 ReferencesEntropy Analysis:



- [NIST Password Guidelines](https://pages.nist.gov/800-63-3/)  Pool Entropy: 53.59 bits```

- [Information Entropy - Wikipedia](https://en.wikipedia.org/wiki/Entropy_(information_theory))

- [Password Cracking - Wikipedia](https://en.wikipedia.org/wiki/Password_cracking)  Shannon Entropy: 26.53 bitsCrack Time = 2^entropy / guesses_per_second

- [Cryptographic Hash Functions](https://en.wikipedia.org/wiki/Cryptographic_hash_function)

- [Passphrase Security](https://xkcd.com/936/)```



---Security Level:



## 🔗 Related Tools  🟡 FAIR - Fair**Attack Scenarios:**



- **[zxcvbn](https://github.com/dropbox/zxcvbn)** - JavaScript password strength estimator  Recommendation: Acceptable, but could be stronger

- **[hashcat](https://hashcat.net/)** - Password cracking tool

- **[John the Ripper](https://www.openwall.com/john/)** - Password auditing software| Scenario | Speed | Device |



---Crack Time (Brute Force):|----------|-------|--------|



**Made with ❤️ for password security education**  Standard CPU: 156.68 hours (max)| CPU Single | 1M/sec | Single core processor |



Last Updated: November 28, 2025    Single GPU: 3.76 minutes (max)| CPU Multi | 1B/sec | Modern multi-core CPU |

Version: 2.0 (Professional Edition)

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
