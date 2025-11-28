"""password_audit package

Lightweight password auditing utilities.
"""

from .audit import analyze_password, entropy_bits, shannon_entropy

__all__ = ["analyze_password", "entropy_bits", "shannon_entropy"]