class BankAccount:
    """Base class shared by savings and checking accounts."""

    def __init__(self, owner, account_number, routing_number, balance=0.0):
        self.owner = owner
        self._account_number = account_number  # Protected member
        self.__routing_number = routing_number  # Private member
        self._balance = float(balance)

    @property
    def account_number(self):
        return self._account_number

    @property
    def balance(self):
        return self._balance

    def get_routing_number(self):
        """Provide controlled access to the private routing number."""
        return self.__routing_number

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self._balance = round(self._balance + amount, 2)
        return self._balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self._balance:
            raise ValueError("Insufficient funds.")

        self._balance = round(self._balance - amount, 2)
        return self._balance

    def __str__(self):
        return (
            f"{self.__class__.__name__}(owner={self.owner}, "
            f"account={self._account_number}, balance=${self._balance:.2f})"
        )
