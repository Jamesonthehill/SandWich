from checking_account import CheckingAccount
from savings_account import SavingsAccount


def main():
    # Two different SavingsAccount instances
    savings_one = SavingsAccount(
        "Alex", "S-1001", "072000326", balance=1000, interest_rate=0.03
    )
    savings_two = SavingsAccount(
        "Jordan", "S-1002", "072000326", balance=2500, interest_rate=0.04
    )

    # Two different CheckingAccount instances
    checking_one = CheckingAccount(
        "Alex", "C-2001", "072000326", balance=800, transfer_limit=300
    )
    checking_two = CheckingAccount(
        "Jordan", "C-2002", "072000326", balance=1200, transfer_limit=500
    )

    print("Starting accounts:")
    for account in (savings_one, savings_two, checking_one, checking_two):
        print(account)

    print("\nScenario 1: Alex withdraws $100 from checking.")
    checking_one.withdraw(100)
    print(checking_one)

    print("\nScenario 2: Jordan transfers $200 from checking to savings.")
    checking_two.transfer(200, savings_two)
    print(checking_two)
    print(savings_two)

    print("\nScenario 3: Interest is added to both savings accounts.")
    print(f"{savings_one.owner} earned ${savings_one.apply_interest():.2f}.")
    print(f"{savings_two.owner} earned ${savings_two.apply_interest():.2f}.")
    print(savings_one)
    print(savings_two)

    print("\nScenario 4: A transfer over the checking limit is rejected.")
    try:
        checking_one.transfer(400, savings_one)
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
