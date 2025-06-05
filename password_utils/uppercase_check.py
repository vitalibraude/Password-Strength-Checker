"""Check for uppercase letters."""

from dataclasses import dataclass

@dataclass
class UppercaseRule:
    required: bool = True


def has_uppercase(password: str, rule: UppercaseRule) -> bool:
    """Return True if password contains an uppercase letter when required."""
    if not rule.required:
        return True
    return any(c.isupper() for c in password)
