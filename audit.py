"""Core password auditing functions.

Simple, offline-safe estimations: entropy, crack time (configurable guesses/sec),
and basic pattern detections. Designed for assessment and education — not for
performing attacks.
"""
from __future__ import annotations

import math
import json
import re
from typing import Dict, Any

COMMON_PASSWORDS = {
    # Most common passwords
    "password", "123456", "123456789", "qwerty", "abc123",
    "password1", "letmein", "admin", "welcome",
    
    # Top 2025 breached passwords
    "123456", "admin", "12345678", "123456789", "1234", "Aa123456", "12345", "password", "123", "1234567890",
    "1234567", "123123", "111111", "12345678910", "P@ssw0rd", "Password", "admin123", "1111111", "Pass@123", 
    "123456a", "000000", "abc123", "qwerty", "qwerty123", "qwerty1", "123456789a", "123qwe", "letmein", "welcome",
    "welcome1", "password1", "password1!", "Password1", "123abc", "123123123", "guest", "guest123", "test",
    "test123", "demo", "demo123", "user", "user123", "login", "login123", "123!@#", "1234qwer", "qwertyuiop",
    "zxcvbn", "asdfgh", "asdfghjkl", "123321", "654321", "777777", "88888888", "999999", "iloveyou", "secret",
    "secret123", "dragon", "monkey", "football", "baseball", "12345678a", "Passw0rd123", "admin!23", "admin@",
    "password!", "P@ssword", "123456789!", "1q2w3e4r", "1qaz2wsx", "qazwsx", "1q2w3e4r5t", "00000000", "11111111",
    "1234567899", "qwe123", "qwe12345", "abcd1234", "abcd123", "admin2025", "password2025", "welcome123", "letmein123",
    "root", "root123", "root@123", "user2025", "passw0rd123", "Pa$$word1", "Pa$$w0rd2025", "Qwerty123!", "admin1234", "12345a"
}


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

def _detect_patterns(password: str) -> Dict[str, Any]:
    """Detect common password weaknesses and patterns.
    
    Returns a dict with 'issues' list containing detected patterns:
    - common-password: Matches known breached passwords
    - low-variation: Uses 2 or fewer unique characters (≥4 length)
    - repeated-chars: Contains 3+ identical characters in a row
    - sequential-chars: Contains 3+ ascending/descending characters
    - year-like: Contains year patterns (1900-2025 or 00-99)
    - single-case: All lowercase or all uppercase
    - all-digits: Contains only numeric digits
    """
    issues = []
    pw = password
    
    # Check if password is in common/breached password list
    if pw.lower() in COMMON_PASSWORDS:
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
    
    # Check for single case usage (all lowercase or all uppercase)
    # Example: 'password' or 'PASSWORD' without case mixing
    if pw.islower() or pw.isupper():
        issues.append("single-case")
    
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

def analyze_password(password: str, guesses_per_second: float = 1e9) -> Dict[str, Any]:
    """Run a basic analysis and return structured results."""
    if password is None:
        raise ValueError("password must be provided")
    bits = entropy_bits(password)
    shannon = shannon_entropy(password)
    seconds = crack_time_seconds(bits, guesses_per_second) if bits > 0 else 0.0
    patterns = _detect_patterns(password)
    
    # Yeni: Scenario analizi
    scenarios = _calculate_crack_scenarios(bits)
    
    # Yeni: Hash penalties
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
    import sys
    print(json.dumps(analyze_password(sys.argv[1] if len(sys.argv) > 1 else "", 1e6), indent=2))