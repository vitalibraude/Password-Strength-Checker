from password_utils.digits_check import DigitRule, has_digit


def test_has_digit():
    rule = DigitRule(required=True)
    assert has_digit('abc1', rule)
    assert not has_digit('abc', rule)
    rule.required = False
    assert has_digit('abc', rule)
