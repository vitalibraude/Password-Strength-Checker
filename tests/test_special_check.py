from password_utils.special_check import SpecialRule, has_special


def test_has_special():
    rule = SpecialRule(required=True)
    assert has_special('hello!world', rule)
    assert not has_special('helloworld', rule)
    rule.required = False
    assert has_special('helloworld', rule)
