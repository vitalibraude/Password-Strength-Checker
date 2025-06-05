"""Entry point for the Password Strength Checker."""

import json
from pathlib import Path
import logging
from typing import Dict

from password_utils import (
    LengthRule,
    SpecialRule,
    UppercaseRule,
    DigitRule,
    BlacklistRule,
    check_length,
    has_special,
    has_uppercase,
    has_digit,
    is_blacklisted,
    improvement_suggestions,
)

CONFIG_FILE = Path('config/config.json')
LOG_DIR = Path('logs')
LOG_DIR.mkdir(exist_ok=True)
logging.basicConfig(
    filename=LOG_DIR / 'password_checks.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)


def load_config(path: Path) -> Dict[str, object]:
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def evaluate_password(password: str, config: Dict[str, object]) -> Dict[str, object]:
    """Evaluate the password against configured rules."""
    length_rule = LengthRule(config.get('min_length', 8))
    special_rule = SpecialRule(config.get('require_special', True))
    uppercase_rule = UppercaseRule(config.get('require_uppercase', True))
    digit_rule = DigitRule(config.get('require_digits', True))
    blacklist_rule = BlacklistRule(Path(config.get('blacklist_file', '')))

    results = {
        'length_ok': check_length(password, length_rule),
        'special_ok': has_special(password, special_rule),
        'uppercase_ok': has_uppercase(password, uppercase_rule),
        'digit_ok': has_digit(password, digit_rule),
        'blacklisted': is_blacklisted(password, blacklist_rule),
    }
    results['suggestions'] = improvement_suggestions(
        password, length_rule, special_rule, uppercase_rule, digit_rule
    )
    return results


def main() -> None:
    config = load_config(CONFIG_FILE)
    password = input("Enter password to evaluate: ")
    results = evaluate_password(password, config)

    if results['blacklisted']:
        print('Password is blacklisted! Choose another.')
    elif all([
        results['length_ok'],
        results['special_ok'],
        results['uppercase_ok'],
        results['digit_ok'],
    ]):
        print('Password looks strong!')
    else:
        print('Password could be stronger:')
        for suggestion in results['suggestions']:
            print(f"- {suggestion}")

    logging.info("%s => %s", password, results)


if __name__ == '__main__':
    main()
