"""Check for digits."""

from dataclasses import dataclass

@dataclass
class DigitRule:
    required: bool = True


def has_digit(password: str, rule: DigitRule) -> bool:
    """Return True if password contains a digit when required."""
    if not rule.required:
        return True
    return any(c.isdigit() for c in password)
