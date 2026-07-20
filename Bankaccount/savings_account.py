from bank_account import BankAccount


class SavingsAccount(BankAccount):
    """A bank account that can earn interest."""

    def __init__(
        self,
        owner,
        account_number,
        routing_number,
        balance=0.0,
        interest_rate=0.0,
    ):
        super().__init__(owner, account_number, routing_number, balance)
        self.interest_rate = float(interest_rate)

    def apply_interest(self):
        if self.interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")

        interest_earned = round(self._balance * self.interest_rate, 2)
        self._balance = round(self._balance + interest_earned, 2)
        return interest_earned
