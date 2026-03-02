from __future__ import annotations

import math
import json
import re
import argparse
import sys
from typing import Dict, Any, Set, Optional

MAX_PASSWORD_LENGTH = 512

def load_wordlist(filepath: str) -> Set[str]:
    """Load a password wordlist from a text file into a set.

    Reads line by line, strips whitespace, converts to lowercase, and returns
    a set for O(1) lookup performance.
    """
    wordlist: Set[str] = set()
    try:
        with open(filepath, "r", encoding="utf-8") as fh:
            for line in fh:
                word = line.strip().lower()
                if word:
                    wordlist.add(word)
    except FileNotFoundError:
        return set()
    return wordlist


def _pool_size(password: str) -> int:
    """Calculate character pool size based on character types present.
    
    Returns the total number of possible characters used in the password.
    Higher pool size = stronger entropy potential.
    """
    pool = 0
    
    # Check for lowercase letters (a-z)
    # Adds 26 possible characters to the pool
    if re.search(r"[a-z]", password):
        pool += 26
    
    # Check for uppercase letters (A-Z)
    # Adds 26 possible characters to the pool
    if re.search(r"[A-Z]", password):
        pool += 26
    
    # Check for digits (0-9)
    # Adds 10 possible characters to the pool
    if re.search(r"[0-9]", password):
        pool += 10
    
    # Check for common ASCII symbols: ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~
    # Adds 32 possible special characters to the pool
    if re.search(r"[!\"#$%&'()*+,\-./:;<=>?@\[\\\]^_`{|}~]", password):
        pool += 32
    
    # Check for Unicode/special characters (non-ASCII, includes emoji)
    # Rough estimate: 128 possible extended/Unicode characters
    if re.search(r"[^\x00-\x7F]", password):
        pool += 128
    
    # Check for whitespace characters (spaces, tabs, newlines)
    # Often forgotten but important for entropy calculation
    if re.search(r"\s", password):
        pool += 1
    
    # Fallback: if no recognized patterns detected, count unique characters
    # Prevents edge cases where pool remains 0
    if pool == 0:
        pool = len(set(password)) or 1
    
    return pool

def entropy_bits(password: str) -> float:
    """Calculate password entropy using pool-based model.
    
    Formula: bits = log2(pool_size) × length
    
    This estimates the strength based on character diversity and length.
    Higher entropy = harder to crack.
    """
    # Return 0 bits for empty passwords
    if not password:
        return 0.0
    
    # Calculate the character pool size (character types used)
    pool = _pool_size(password)

    # Apply entropy formula: log2(pool_size) × password length
    # Each character position has pool_size choices, so total possibilities = pool_size^length
    # In bits: log2(pool_size^length) = log2(pool_size) × length
    bits = math.log2(pool) * len(password)

    return bits

def shannon_entropy(password: str) -> float:
    """Calculate Shannon entropy based on character frequency. 
    
    Formula: -Σ(p_i × log2(p_i)) × length
    
    This detects if the password has repeated characters (weak randomness).
    Complements pool-based entropy by catching patterns.
    Example: 'aaaa' has high pool entropy but zero Shannon entropy.
    """
    # Return 0 bits for empty passwords
    if not password:
        return 0.0
    
    # Calculate character frequency distribution
    freq = {}
    for ch in password:
        freq[ch] = freq.get(ch, 0) + 1
    
    length = len(password)
    entropy_value = 0.0

    # Calculate Shannon entropy: sum of (probability × log2(probability))
    # Each unique character contributes based on how often it appears
    for count in freq.values():
        probability = count / length
        entropy_value -= probability * math.log2(probability)
    
    # Multiply by length to get total bits (entropy per character × character count)
    return entropy_value * length

def _is_sequential(s: str, min_len: int = 3) -> bool:
    """Detect if string contains sequential characters (ascending or descending).
    
    Examples: 'abc', '123', 'zyx' return True
    Examples: 'aba', 'qwe', '111' return False
    """
    # Must have minimum length to be considered sequential
    if len(s) < min_len:
        return False
    
    # Convert characters to their ASCII ordinal values
    # This allows comparison of both letters and digits
    seq = ''.join(s)
    vals = [ord(c) for c in seq]
    
    # Check for ascending sequence: each value is 1 more than previous
    ascending = all(vals[i] + 1 == vals[i + 1] for i in range(len(vals) - 1))
    
    # Check for descending sequence: each value is 1 less than previous
    descending = all(vals[i] - 1 == vals[i + 1] for i in range(len(vals) - 1))
    
    return ascending or descending

def _check_spatial_patterns(password: str, min_len: int = 3) -> bool:
    """Detect spatial keyboard patterns (QWERTY, numeric keypad).
    
    Detects sequences of 3+ characters that appear on keyboard layouts:
    - QWERTY rows (forward/reverse): 'qwe', 'asd', 'zxc', '123', etc.
    - Numeric keypad patterns: '789', '456', '147', etc.
    
    Examples:
    - 'qwerty' → True (QWERTY row)
    - 'asdfgh' → True (QWERTY home row)
    - '123' → True (number row)
    - '!@#' → True (shifted number row)
    - '789' → True (numeric keypad top row)
    - '159' → True (numeric keypad diagonal)
    - 'password' → False (no keyboard pattern)
    
    Args:
        password: Password to checkv
        min_len: Minimum pattern length (default: 3)
    
    Returns:
        True if a spatial pattern is detected, False otherwise
    """
    # QWERTY keyboard layout rows
    qwerty_rows = [
        "1234567890",           # Number row
        "!@#$%^&*()",           # Shifted number row (symbols)
        "qwertyuiop",           # Top letter row
        "asdfghjkl",            # Home row
        "zxcvbnm",              # Bottom row
        "`~-_=+[{]}\\|;:'\",<.>/?",  # Additional symbols
    ]
    
    # Numeric keypad layout (standard calculator/phone style)
    # Includes rows, columns, and common diagonals
    numpad_patterns = [
        "789",     # Top row
        "456",     # Middle row
        "123",     # Bottom row
        "741",     # Left column
        "852",     # Middle column
        "963",     # Right column
        "753",     # Diagonal (top-left to bottom-right)
        "159",     # Diagonal (bottom-left to top-right)
        "7410",    # Left column with zero
        "8520",    # Middle column with zero
        "9630",    # Right column with zero
    ]
    
    # Combine all keyboard patterns
    all_patterns = qwerty_rows + numpad_patterns
    
    # Convert password to lowercase for case-insensitive matching
    pw_lower = password.lower()
    
    # Check each possible substring of length >= min_len
    for length in range(min_len, len(password) + 1):
        for i in range(len(password) - length + 1):
            segment = pw_lower[i:i + length]
            
            # Check forward and reverse against all keyboard patterns
            for pattern in all_patterns:
                pattern_lower = pattern.lower()
                
                # Check if segment appears in pattern (forward)
                if segment in pattern_lower:
                    return True
                
                # Check if segment appears in pattern (reverse)
                if segment in pattern_lower[::-1]:
                    return True
    
    return False

def _detect_patterns(password: str, wordlist_set: Optional[Set[str]] = None) -> Dict[str, Any]:
    """
    Detect common password weaknesses and patterns.
    Returns a dict with 'issues' list containing detected patterns:
    - common-password: Matches known breached passwords
    - low-variation: Uses 2 or fewer unique characters (≥4 length)
    - repeated-chars: Contains 3+ identical characters in a row
    - sequential-chars: Contains 3+ ascending/descending characters
    - spatial-pattern: Contains keyboard layout patterns (QWERTY, numpad)
    - year-like: Contains year patterns (1900-2025 or 00-99)
    - missing-uppercase: Has letters but no uppercase characters
    - missing-lowercase: Has letters but no lowercase characters
    - all-digits: Contains only numeric digits
    """
    issues = []
    pw = password
    wordlist = wordlist_set or set()
    
    # Check if password is in common/breached password list
    if pw.lower() in wordlist:
        issues.append("common-password")
    
    # Check for low character variety (≤2 unique chars, password ≥4 chars)
    # Example: 'aaaa' or 'abab' are weak due to low variation
    if len(set(pw)) <= 2 and len(pw) >= 4:
        issues.append("low-variation")
    
    # Check for repeated characters: 3+ same character in a row
    # Example: 'aaa', 'ppppp' indicate weak pattern
    if re.search(r"(.)\1{2,}", pw):
        issues.append("repeated-chars")

    # Check for sequential character patterns (3+ ascending/descending)
    # Example: 'abc', '123', 'zyx' are weak patterns
    for i in range(len(pw) - 2):
        if _is_sequential(pw[i:i+3]):
            issues.append("sequential-chars")
            break
    
    # Check for spatial keyboard patterns (QWERTY rows, numeric keypad)
    # Example: 'qwerty', 'asdf', '789', '!@#' are keyboard patterns
    if _check_spatial_patterns(pw):
        issues.append("spatial-pattern")

    # Check for year-like patterns (1900-2025 or 00-99)
    # These are common weak additions to passwords
    m = re.search(r"(19\d{2}|20\d{2}|\d{2})", pw)
    if m:
        try:
            year = int(m.group(0))
            if 1900 <= year <= 2025 or (0 <= year <= 99):
                issues.append("year-like")
        except Exception:
            pass
    
    # Check for missing case variation (only if password contains letters)
    # Example: 'password!@#' has letters but missing uppercase
    # Example: 'PASSWORD123' has letters but missing lowercase
    has_letters = any(c.isalpha() for c in pw)
    if has_letters:
        has_lowercase = any(c.islower() for c in pw)
        has_uppercase = any(c.isupper() for c in pw)
        
        if not has_uppercase:
            issues.append("missing-uppercase")
        if not has_lowercase:
            issues.append("missing-lowercase")
    
    # Check if password contains only digits
    # Example: '123456' is weak because it's purely numeric
    if pw.isdigit():
        issues.append("all-digits")
    
    # Return sorted, deduplicated list of issues
    return {"issues": sorted(set(issues))}

def crack_time_seconds(entropy_bits_value: float, guesses_per_second: float) -> float:
    """Estimate time to crack (seconds) assuming brute-force exhaustive search.

    Use 2**entropy / guesses_per_second as an estimate of average full search.
    """
    if guesses_per_second <= 0:
        raise ValueError("guesses_per_second must be > 0")
    
    # Prevent overflow for very large entropy values
    # 2^1024 is already astronomically large
    if entropy_bits_value > 1024:
        return float('inf')  # Return infinity for unreasonably large entropy
    
    # number of guesses ~ 2**entropy (search space size)
    guesses = 2 ** entropy_bits_value
    return guesses / guesses_per_second

def _calculate_crack_scenarios(entropy_bits_value: float) -> Dict[str, Dict[str, float]]:
    """Calculate crack times for different attack scenarios.
    
    Returns times for various guessing speeds:
    - cpu_single: Single CPU core
    - cpu_multi: Modern multi-core CPU
    - gpu_single: Single GPU
    - gpu_farm: GPU farm (10 GPUs)
    - distributed: Large botnet
    """
    # Different attack scenarios (guesses per second)
    scenarios = {
        "cpu_single": 1e6,      # Single CPU: 1 million/sec
        "cpu_multi": 1e9,       # Multi-core CPU: 1 billion/sec (modern)
        "gpu_single": 1e12,     # Single GPU: 1 trillion/sec
        "gpu_farm": 1e13,       # 10 GPUs combined
        "distributed": 1e15,    # Large botnet
    }
    
    results = {}
    for scenario, guesses_per_sec in scenarios.items():
        if entropy_bits_value > 0:
            max_time = 2 ** entropy_bits_value / guesses_per_sec
        else:
            max_time = 0
        avg_time = max_time / 2  # Average = max / 2
        
        results[scenario] = {
            "guesses_per_second": guesses_per_sec,
            "max_seconds": max_time,
            "avg_seconds": avg_time,
        }
    
    return results

def _apply_hash_penalty(base_seconds: float, hash_type: str = "bcrypt") -> float:
    """Apply slowdown factor based on hash function.
    
    Real systems use hash functions that deliberately slow down:
    - Plain text: 1x (1 microsecond per guess)
    - MD5: 1x (very fast, dangerous)
    - SHA256: 1x (fast, not ideal for passwords)
    - bcrypt: ~100-500x slower (good)
    - Argon2: ~1000x slower (excellent)
    - scrypt: ~500-2000x slower (very good)
    """
    penalties = {
        "plaintext": 1,      # No penalty
        "md5": 1,            # Very fast, dangerous
        "sha256": 1,         # Fast, not secure
        "bcrypt": 200,       # ~200x slower (bcrypt cost=12)
        "argon2": 1000,      # ~1000x slower
        "scrypt": 1000,      # ~1000x slower
    }
    
    penalty = penalties.get(hash_type.lower(), 1)
    return base_seconds * penalty

def _get_security_level(entropy_bits_value: float) -> Dict[str, Any]:
    """Classify password security based on entropy.
    
    Returns security level and recommendations.
    """
    levels = {
        (0, 30): {
            "level": "CRITICAL",
            "emoji": "🔴",
            "description": "Extremely Weak",
            "recommendation": "Change immediately - easily crackable"
        },
        (30, 50): {
            "level": "WEAK",
            "emoji": "🟠",
            "description": "Weak",
            "recommendation": "Add length, mix character types"
        },
        (50, 70): {
            "level": "FAIR",
            "emoji": "🟡",
            "description": "Fair",
            "recommendation": "Acceptable, but could be stronger"
        },
        (70, 90): {
            "level": "GOOD",
            "emoji": "🟢",
            "description": "Good",
            "recommendation": "Strong password - well done!"
        },
        (90, 120): {
            "level": "EXCELLENT",
            "emoji": "🟢",
            "description": "Excellent",
            "recommendation": "Very strong password - excellent!"
        },
        (120, float('inf')): {
            "level": "MASTER",
            "emoji": "💎",
            "description": "Master Level",
            "recommendation": "Exceptional strength - top tier!"
        }
    }
    
    for (min_bits, max_bits), info in levels.items():
        if min_bits <= entropy_bits_value < max_bits:
            return info
    
    return {
        "level": "UNKNOWN",
        "emoji": "❓",
        "description": "Unknown",
        "recommendation": "Unable to classify"
    }

def human_readable_seconds(s: float) -> str:
    if s < 1:
        return f"{s:.3f} seconds"
    units = [
        (60, "seconds"),
        (60, "minutes"),
        (24, "hours"),
        (365, "days"),
        (1000, "years"),
    ]
    value = s
    current_unit = "seconds"
    for factor, next_unit in units:
        if value < factor:
            return f"{value:.2f} {current_unit}"
        value /= factor
        current_unit = next_unit
    return f">= {value:.2f} {current_unit}"

def analyze_password(
    password: str,
    guesses_per_second: float = 1e9,
    wordlist_set: Optional[Set[str]] = None,
) -> Dict[str, Any]:
    """Run a basic analysis and return structured results."""
    if password is None:
        raise ValueError("password must be provided")
    bits = entropy_bits(password)
    shannon = shannon_entropy(password)
    seconds = crack_time_seconds(bits, guesses_per_second) if bits > 0 else 0.0
    patterns = _detect_patterns(password, wordlist_set)
    
    #Scenario analizi
    scenarios = _calculate_crack_scenarios(bits)
    
    #Hash penalties
    bcrypt_seconds = _apply_hash_penalty(seconds, "bcrypt")
    argon2_seconds = _apply_hash_penalty(seconds, "argon2")
    
    # Yeni: Security level
    security = _get_security_level(bits)
    
    result = {
        "password": password,
        "length": len(password),
        "entropy_bits": bits,
        "shannon_bits": shannon,
        "guesses_per_second": guesses_per_second,
        "estimated_crack_seconds": seconds,
        "estimated_crack_human": human_readable_seconds(seconds),
        
        # Yeni alanlar
        "security_level": security,
        "crack_scenarios": {
            scenario: {
                "description": scenario.replace("_", " ").title(),
                "max_time_human": human_readable_seconds(data["max_seconds"]),
                "avg_time_human": human_readable_seconds(data["avg_seconds"]),
                "max_seconds": data["max_seconds"],
                "avg_seconds": data["avg_seconds"],
            }
            for scenario, data in scenarios.items()
        },
        "with_hash_protection": {
            "bcrypt": {
                "description": "With bcrypt (cost=12, ~200x slower)",
                "crack_time_human": human_readable_seconds(bcrypt_seconds),
                "crack_seconds": bcrypt_seconds,
            },
            "argon2": {
                "description": "With Argon2 (~1000x slower)",
                "crack_time_human": human_readable_seconds(argon2_seconds),
                "crack_seconds": argon2_seconds,
            }
        }
    }
    result.update(patterns)
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Password auditing tool (module)")
    parser.add_argument("password", nargs="?", default="", help="Password to analyze")
    parser.add_argument("-g", "--guesses", type=float, default=1e6,
                        help="Guesses per second attacker can try (default: 1e6)")
    parser.add_argument(
        "-w",
        "--wordlist",
        default="Wordlists/100k-most-used-passwords-NCSC.txt",
        help="Path to password wordlist (default: Wordlists/100k-most-used-passwords-NCSC.txt)",
    )
    args = parser.parse_args()

    print(f"Loading wordlist: {args.wordlist}")
    wordlist_set = load_wordlist(args.wordlist)
    print(f"Loaded {len(wordlist_set)} passwords into memory")

    if len(args.password) > MAX_PASSWORD_LENGTH:
        print(
            f"Error: Input exceeds the maximum allowed length of "
            f"{MAX_PASSWORD_LENGTH} characters."
        )
        sys.exit(1)

    result = analyze_password(args.password, args.guesses, wordlist_set)
    print(json.dumps(result, indent=2))
