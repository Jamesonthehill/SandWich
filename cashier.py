class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        # TA CHANGE START: collect each accepted coin and calculate its value.
        print("Please insert coins.")
        large_dollars = int(input("How many large dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))

        total = (
            large_dollars * 1.00
            + half_dollars * 0.50
            + quarters * 0.25
            + nickels * 0.05
        )
        return round(total, 2)
        # TA CHANGE END

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        # TA CHANGE START: accept sufficient payment and return any change.
        if coins < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False

        change = round(coins - cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        return True
        # TA CHANGE END
