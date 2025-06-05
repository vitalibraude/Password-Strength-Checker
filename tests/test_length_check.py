from password_utils.length_check import LengthRule, check_length


def test_check_length():
    rule = LengthRule(min_length=8)
    assert check_length('12345678', rule)
    assert not check_length('short', rule)
