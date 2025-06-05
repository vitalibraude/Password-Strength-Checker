from pathlib import Path

from password_utils.blacklist_check import BlacklistRule, is_blacklisted


BLACKLIST_FILE = Path('examples/blacklist.txt')


def test_is_blacklisted(tmp_path):
    rule = BlacklistRule(BLACKLIST_FILE)
    assert is_blacklisted('password', rule)
    assert not is_blacklisted('uniquePass', rule)
