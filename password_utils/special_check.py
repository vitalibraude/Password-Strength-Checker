"""Check for presence of special characters."""

import re
from dataclasses import dataclass

@dataclass
class SpecialRule:
    required: bool = True
    pattern: str = r"[^\w\s]"  # any non-alphanumeric, non-space char


def has_special(password: str, rule: SpecialRule) -> bool:
    """Return True if password contains a special character when required."""
    if not rule.required:
        return True
    return re.search(rule.pattern, password) is not None
