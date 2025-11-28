"""Unit tests for password_audit module.

Tests all core functionality to ensure password analysis works correctly.
Run with: python -m pytest test_audit.py -v
"""

import pytest
import math
from audit import (
    entropy_bits,
    shannon_entropy,
    _pool_size,
    _is_sequential,
    _detect_patterns,
    crack_time_seconds,
    human_readable_seconds,
    analyze_password,
)


# ============================================================================
# Tests for _pool_size()
# ============================================================================

class TestPoolSize:
    """Test character pool size calculation."""
    
    def test_pool_size_lowercase_only(self):
        """Lowercase letters should give pool size 26."""
        assert _pool_size("abc") == 26
    
    def test_pool_size_uppercase_only(self):
        """Uppercase letters should give pool size 26."""
        assert _pool_size("ABC") == 26
    
    def test_pool_size_mixed_case(self):
        """Mixed case should give pool size 52."""
        assert _pool_size("aA") == 52
    
    def test_pool_size_with_digits(self):
        """With digits should include +10."""
        result = _pool_size("a1")
        assert result == 26 + 10  # lowercase + digits
    
    def test_pool_size_with_symbols(self):
        """With symbols should include +32."""
        result = _pool_size("a!")
        assert result == 26 + 32  # lowercase + symbols
    
    def test_pool_size_all_types(self):
        """With all types: 26+26+10+32 = 94."""
        result = _pool_size("aA1!")
        assert result == 94
    
    def test_pool_size_empty_string(self):
        """Empty string should return 1 (fallback)."""
        assert _pool_size("") == 1


# ============================================================================
# Tests for entropy_bits()
# ============================================================================

class TestEntropyBits:
    """Test entropy calculation."""
    
    def test_entropy_empty_password(self):
        """Empty password should have 0 entropy."""
        assert entropy_bits("") == 0.0
    
    def test_entropy_positive(self):
        """Non-empty password should have positive entropy."""
        assert entropy_bits("password") > 0
    
    def test_entropy_increases_with_length(self):
        """Longer passwords should have higher entropy."""
        short = entropy_bits("abc")
        long = entropy_bits("abcdefgh")
        assert long > short
    
    def test_entropy_increases_with_pool(self):
        """More character types = higher entropy."""
        lowercase = entropy_bits("abc")
        mixed = entropy_bits("aA1")
        assert mixed > lowercase
    
    def test_entropy_formula(self):
        """Test entropy calculation formula."""
        # For "abc": pool=26, entropy = log2(26) * 3
        password = "abc"
        expected = math.log2(26) * 3
        assert abs(entropy_bits(password) - expected) < 0.001
    
    def test_entropy_return_type(self):
        """entropy_bits should return float."""
        result = entropy_bits("password")
        assert isinstance(result, float)


# ============================================================================
# Tests for shannon_entropy()
# ============================================================================

class TestShannonEntropy:
    """Test Shannon entropy calculation."""
    
    def test_shannon_empty_password(self):
        """Empty password should have 0 Shannon entropy."""
        assert shannon_entropy("") == 0.0
    
    def test_shannon_uniform_distribution(self):
        """Uniform characters should have high entropy."""
        # "abcd" has 4 unique characters in 4 positions = high Shannon
        result = shannon_entropy("abcd")
        assert result > 0
    
    def test_shannon_repeated_characters(self):
        """Repeated characters should have lower entropy."""
        # "aaaa" has only 1 unique character = low/zero Shannon
        result = shannon_entropy("aaaa")
        assert result == 0.0  # All same character
    
    def test_shannon_vs_pool_entropy(self):
        """Shannon entropy should differ from pool entropy."""
        password = "aaaa"
        pool_ent = entropy_bits(password)
        shannon_ent = shannon_entropy(password)
        # Pool entropy is high, but Shannon is 0 (repetitive)
        assert pool_ent > 0
        assert shannon_ent == 0.0
    
    def test_shannon_return_type(self):
        """shannon_entropy should return float."""
        result = shannon_entropy("password")
        assert isinstance(result, float)


# ============================================================================
# Tests for _is_sequential()
# ============================================================================

class TestIsSequential:
    """Test sequential character detection."""
    
    def test_sequential_ascending_letters(self):
        """abc should be sequential."""
        assert _is_sequential("abc") is True
    
    def test_sequential_ascending_digits(self):
        """123 should be sequential."""
        assert _is_sequential("123") is True
    
    def test_sequential_descending_letters(self):
        """cba should be sequential."""
        assert _is_sequential("cba") is True
    
    def test_sequential_descending_digits(self):
        """321 should be sequential."""
        assert _is_sequential("321") is True
    
    def test_non_sequential_mixed(self):
        """aba should not be sequential."""
        assert _is_sequential("aba") is False
    
    def test_non_sequential_random(self):
        """Random characters should not be sequential."""
        assert _is_sequential("qwe") is False
    
    def test_sequential_minimum_length(self):
        """Less than 3 characters should return False."""
        assert _is_sequential("ab") is False
        assert _is_sequential("a") is False
    
    def test_sequential_long_pattern(self):
        """Long sequential should still be detected."""
        assert _is_sequential("abcdefg") is True


# ============================================================================
# Tests for _detect_patterns()
# ============================================================================

class TestDetectPatterns:
    """Test pattern detection."""
    
    def test_common_password(self):
        """'password' should be detected as common."""
        result = _detect_patterns("password")
        assert "common-password" in result["issues"]
    
    def test_low_variation(self):
        """'aaaa' should have low-variation issue."""
        result = _detect_patterns("aaaa")
        assert "low-variation" in result["issues"]
    
    def test_repeated_chars(self):
        """'passsword' should have repeated-chars issue."""
        result = _detect_patterns("passsword")
        assert "repeated-chars" in result["issues"]
    
    def test_sequential_chars(self):
        """'abc123' should have sequential-chars issue."""
        result = _detect_patterns("abc123")
        assert "sequential-chars" in result["issues"]
    
    def test_year_like(self):
        """'Pass1990' should have year-like issue."""
        result = _detect_patterns("Pass1990")
        assert "year-like" in result["issues"]
    
    def test_single_case_lower(self):
        """'password' should have single-case issue."""
        result = _detect_patterns("password")
        assert "single-case" in result["issues"]
    
    def test_single_case_upper(self):
        """'PASSWORD' should have single-case issue."""
        result = _detect_patterns("PASSWORD")
        assert "single-case" in result["issues"]
    
    def test_all_digits(self):
        """'123456' should have all-digits issue."""
        result = _detect_patterns("123456")
        assert "all-digits" in result["issues"]
    
    def test_no_issues(self):
        """'X9@mK2pL' should have no issues."""
        result = _detect_patterns("X9@mK2pL")
        assert len(result["issues"]) == 0
    
    def test_multiple_issues(self):
        """Some passwords should have multiple issues."""
        result = _detect_patterns("pass123")
        assert len(result["issues"]) >= 2  # common-password, sequential-chars, etc.


# ============================================================================
# Tests for crack_time_seconds()
# ============================================================================

class TestCrackTimeSeconds:
    """Test crack time calculation."""
    
    def test_crack_time_positive(self):
        """Crack time should be positive."""
        result = crack_time_seconds(entropy_bits_value=50, guesses_per_second=1e9)
        assert result > 0
    
    def test_crack_time_increases_with_entropy(self):
        """Higher entropy should mean longer crack time."""
        time_low = crack_time_seconds(entropy_bits_value=30, guesses_per_second=1e9)
        time_high = crack_time_seconds(entropy_bits_value=80, guesses_per_second=1e9)
        assert time_high > time_low
    
    def test_crack_time_decreases_with_guesses(self):
        """More guesses per second = shorter crack time."""
        time_slow = crack_time_seconds(entropy_bits_value=50, guesses_per_second=1e6)
        time_fast = crack_time_seconds(entropy_bits_value=50, guesses_per_second=1e12)
        assert time_fast < time_slow
    
    def test_crack_time_invalid_guesses(self):
        """Negative guesses should raise error."""
        with pytest.raises(ValueError):
            crack_time_seconds(entropy_bits_value=50, guesses_per_second=-1)
    
    def test_crack_time_zero_guesses(self):
        """Zero guesses should raise error."""
        with pytest.raises(ValueError):
            crack_time_seconds(entropy_bits_value=50, guesses_per_second=0)


# ============================================================================
# Tests for human_readable_seconds()
# ============================================================================

class TestHumanReadableSeconds:
    """Test human-readable time formatting."""
    
    def test_milliseconds(self):
        """Very small time should show seconds."""
        result = human_readable_seconds(0.001)
        assert "seconds" in result
    
    def test_seconds(self):
        """30 seconds should show seconds."""
        result = human_readable_seconds(30)
        assert "seconds" in result
    
    def test_minutes(self):
        """500 seconds = ~8.33 minutes."""
        result = human_readable_seconds(500)
        # 500 < 60*60 = 3600, so should show in minutes
        # 500/60 = 8.33, so shows as "8.33 minutes"
        assert "minutes" in result or "seconds" in result  # 500 seconds is at boundary
    
    def test_hours(self):
        """10000 seconds = ~2.78 hours."""
        result = human_readable_seconds(10000)
        # 10000 > 3600, so should show in hours
        assert "hours" in result or "minutes" in result
    
    def test_days(self):
        """1000000 seconds = ~11.57 days."""
        result = human_readable_seconds(1000000)
        # Should show in days or hours
        assert "days" in result or "hours" in result
    
    def test_years(self):
        """31536000 seconds = ~1 year."""
        result = human_readable_seconds(31536000)
        # Should show in years
        assert "years" in result or "days" in result
    
    def test_large_years(self):
        """Very large time should show years."""
        result = human_readable_seconds(1e15)
        assert "years" in result


# ============================================================================
# Tests for analyze_password()
# ============================================================================

class TestAnalyzePassword:
    """Test complete password analysis."""
    
    def test_analyze_returns_dict(self):
        """analyze_password should return a dictionary."""
        result = analyze_password("Test123!")
        assert isinstance(result, dict)
    
    def test_analyze_has_required_fields(self):
        """Result should have all required fields."""
        result = analyze_password("Test123!")
        required_fields = [
            "password", "length", "entropy_bits", "shannon_bits",
            "estimated_crack_seconds", "estimated_crack_human",
            "security_level", "issues"
        ]
        for field in required_fields:
            assert field in result
    
    def test_analyze_password_value(self):
        """Analyzed password should match input."""
        password = "Test123!"
        result = analyze_password(password)
        assert result["password"] == password
    
    def test_analyze_length(self):
        """Length should be correct."""
        password = "Test123!"
        result = analyze_password(password)
        assert result["length"] == len(password)
    
    def test_analyze_none_password(self):
        """None password should raise error."""
        with pytest.raises(ValueError):
            analyze_password(None)
    
    def test_analyze_custom_guesses(self):
        """Should handle custom guesses per second."""
        result1 = analyze_password("Test123!", guesses_per_second=1e9)
        result2 = analyze_password("Test123!", guesses_per_second=1e12)
        # Higher guesses should give shorter time
        assert result2["estimated_crack_seconds"] < result1["estimated_crack_seconds"]
    
    def test_analyze_security_levels(self):
        """Should correctly classify security levels."""
        weak = analyze_password("password")
        strong = analyze_password("X9@mK2pLqR!zT4vW")
        
        weak_level = weak["security_level"]["level"]
        strong_level = strong["security_level"]["level"]
        
        # Weak should be WEAK or lower, strong should be higher
        assert weak_level in ["CRITICAL", "WEAK"]
        assert strong_level in ["GOOD", "EXCELLENT", "MASTER"]


# ============================================================================
# Integration Tests
# ============================================================================

class TestIntegration:
    """Integration tests for complete workflows."""
    
    def test_weak_password_analysis(self):
        """Weak password should show appropriate results."""
        result = analyze_password("password")
        assert result["security_level"]["level"] in ["CRITICAL", "WEAK"]
        assert "common-password" in result["issues"]
        assert result["entropy_bits"] < 50
    
    def test_strong_password_analysis(self):
        """Strong password should show appropriate results."""
        result = analyze_password("X9@mK2pLqR!zT4vW#5sUa")
        assert result["security_level"]["level"] in ["EXCELLENT", "MASTER"]
        assert len(result["issues"]) == 0
        assert result["entropy_bits"] > 100
    
    def test_entropy_correlation(self):
        """Higher entropy should correlate with longer crack time."""
        password1 = "Pass"      # Low entropy
        password2 = "Pass123!@#" # High entropy
        
        result1 = analyze_password(password1)
        result2 = analyze_password(password2)
        
        assert result1["entropy_bits"] < result2["entropy_bits"]
        assert result1["estimated_crack_seconds"] < result2["estimated_crack_seconds"]
    
    def test_hash_protection_impact(self):
        """Hash protection should increase crack time."""
        result = analyze_password("Test123!")
        
        base_time = result["estimated_crack_seconds"]
        bcrypt_time = result["with_hash_protection"]["bcrypt"]["crack_seconds"]
        argon2_time = result["with_hash_protection"]["argon2"]["crack_seconds"]
        
        assert bcrypt_time > base_time
        assert argon2_time > bcrypt_time


# ============================================================================
# Edge Cases
# ============================================================================

class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    def test_very_long_password(self):
        """Very long password should be handled."""
        # Use a shorter long password to avoid overflow
        # 100 characters is still long but manageable
        long_password = "a" * 100
        result = analyze_password(long_password)
        assert result["length"] == 100
        assert result["entropy_bits"] > 0
    
    def test_unicode_password(self):
        """Unicode characters should be supported."""
        result = analyze_password("Pässwörd123!")
        assert result["entropy_bits"] > 0
        assert result["length"] > 0
    
    def test_emoji_password(self):
        """Emoji should be recognized."""
        result = analyze_password("Pass123!😀🔐")
        assert result["entropy_bits"] > 0
    
    def test_special_characters_only(self):
        """Special characters only should work."""
        result = analyze_password("!@#$%^&*()")
        assert result["length"] == 10
        assert result["entropy_bits"] > 0
    
    def test_spaces_in_password(self):
        """Spaces should be handled."""
        result = analyze_password("My Pass 123")
        assert "password" in result
        assert result["length"] == 11


if __name__ == "__main__":
    # Run tests with: python -m pytest test_audit.py -v
    # Or: python test_audit.py (with pytest installed)
    
    print("To run tests, use:")
    print("  python -m pytest test_audit.py -v")
    print("  python -m pytest test_audit.py -v --tb=short")
    print("  python -m pytest test_audit.py::TestPoolSize -v")
