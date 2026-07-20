class Cashier:
    def process_coins(self):
        """Ask for coins and return their total monetary value."""
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total = (
            large_dollars * 1.00
            + half_dollars * 0.50
            + quarters * 0.25
            + nickels * 0.05
        )
        return round(total, 2)

    def transaction_result(self, coins, cost):
        """Return True for accepted payment or False after a refund."""
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False

        change = round(coins - cost, 2)
        print(f"Here is ${change} in change.")
        return True
