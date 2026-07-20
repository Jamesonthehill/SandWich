# Bank Account Inheritance Assignment

## Requirement Map

- `bank_account.py`: parent `BankAccount` class, protected `_account_number`,
  and private `__routing_number`.
- `savings_account.py`: `SavingsAccount` subclass with `apply_interest()`.
- `checking_account.py`: `CheckingAccount` subclass with a per-transfer
  dollar limit.
- `main.py`: imports both subclasses, creates two instances of each, and runs
  withdrawal, transfer, interest, and rejected-transfer scenarios.

## Run

From this directory, run:

```bash
python3 main.py
```

This solution interprets "transfer limitation" as the maximum dollar amount
allowed in one checking-account transfer.
