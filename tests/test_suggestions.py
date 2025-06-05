from password_utils import (
    LengthRule,
    SpecialRule,
    UppercaseRule,
    DigitRule,
    improvement_suggestions,
)


def test_improvement_suggestions():
    suggestions = improvement_suggestions(
        'weak',
        LengthRule(min_length=8),
        SpecialRule(required=True),
        UppercaseRule(required=True),
        DigitRule(required=True),
    )
    assert 'Increase length to at least 8 characters' in suggestions
    assert 'Add special characters' in suggestions
    assert 'Include uppercase letters' in suggestions
    assert 'Include digits' in suggestions
