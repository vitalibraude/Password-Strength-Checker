"""Provide suggestions to improve password strength."""

from typing import List

from .length_check import LengthRule, check_length
from .special_check import SpecialRule, has_special
from .uppercase_check import UppercaseRule, has_uppercase
from .digits_check import DigitRule, has_digit


def improvement_suggestions(password: str,
                            length_rule: LengthRule,
                            special_rule: SpecialRule,
                            uppercase_rule: UppercaseRule,
                            digit_rule: DigitRule) -> List[str]:
    """Return a list of suggestions for improving the password."""
    suggestions: List[str] = []

    if not check_length(password, length_rule):
        suggestions.append(f"Increase length to at least {length_rule.min_length} characters")
    if not has_special(password, special_rule):
        suggestions.append("Add special characters")
    if not has_uppercase(password, uppercase_rule):
        suggestions.append("Include uppercase letters")
    if not has_digit(password, digit_rule):
        suggestions.append("Include digits")
    return suggestions
