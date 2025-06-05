"""Password length checker module."""

from dataclasses import dataclass

@dataclass
class LengthRule:
    min_length: int = 8


def check_length(password: str, rule: LengthRule) -> bool:
    """Return True if password meets the minimum length."""
    return len(password) >= rule.min_length
