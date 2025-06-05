from password_utils.uppercase_check import UppercaseRule, has_uppercase


def test_has_uppercase():
    rule = UppercaseRule(required=True)
    assert has_uppercase('Hello', rule)
    assert not has_uppercase('hello', rule)
    rule.required = False
    assert has_uppercase('hello', rule)
