"""Check if a password is blacklisted."""

from dataclasses import dataclass
from pathlib import Path

@dataclass
class BlacklistRule:
    blacklist_file: Path


def is_blacklisted(password: str, rule: BlacklistRule) -> bool:
    """Return True if password appears in the blacklist file."""
    try:
        if rule.blacklist_file.exists():
            with rule.blacklist_file.open('r', encoding='utf-8') as f:
                blacklisted = {line.strip() for line in f if line.strip()}
            return password in blacklisted
    except IOError:
        pass
    return False
