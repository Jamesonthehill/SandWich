from bank_account import BankAccount


class CheckingAccount(BankAccount):
    """A bank account with a maximum amount allowed per transfer."""

    def __init__(
        self,
        owner,
        account_number,
        routing_number,
        balance=0.0,
        transfer_limit=500.0,
    ):
        super().__init__(owner, account_number, routing_number, balance)
        self.transfer_limit = float(transfer_limit)

    def transfer(self, amount, destination_account):
        if amount <= 0:
            raise ValueError("Transfer amount must be greater than zero.")
        if amount > self.transfer_limit:
            raise ValueError(
                f"Transfer exceeds the ${self.transfer_limit:.2f} limit."
            )

        self.withdraw(amount)
        destination_account.deposit(amount)
        return self._balance
