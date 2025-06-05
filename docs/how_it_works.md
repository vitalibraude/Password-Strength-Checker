# How It Works

The **Password Strength Checker** evaluates passwords based on a set of rules
specified in `config/config.json`. Each rule is implemented as a small, testable
function inside the `password_utils` package.

Checks performed:

- Minimum length
- Presence of special characters
- Presence of uppercase letters
- Presence of digits
- Blacklist check

The `main.py` script brings these checks together and outputs suggestions for
improving passwords. Results are also logged to `logs/password_checks.log`.
