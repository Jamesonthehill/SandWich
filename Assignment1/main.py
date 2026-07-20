recipes = {
    "small": {
        "ingredients": {
            "bread": 2,
            "ham": 4,
            "cheese": 4,
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,
            "ham": 6,
            "cheese": 8,
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,
            "ham": 8,
            "cheese": 12,
        },
        "cost": 5.50,
    },
}

resources = {
    "bread": 12,
    "ham": 18,
    "cheese": 24,
}


class SandwichMachine:
    def __init__(self, machine_resources):
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Return True when an order can be made, or False if supplies are low."""
        for item, amount_needed in ingredients.items():
            if amount_needed > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct ingredients and announce the completed sandwich."""
        for item, amount_needed in order_ingredients.items():
            self.machine_resources[item] -= amount_needed

        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

    def show_report(self):
        print(f"Bread: {self.machine_resources['bread']} slice(s)")
        print(f"Ham: {self.machine_resources['ham']} slice(s)")
        print(f"Cheese: {self.machine_resources['cheese']} ounce(s)")


def main():
    machine = SandwichMachine(resources)
    machine_is_on = True

    while machine_is_on:
        choice = input(
            "What would you like? (small/ medium/ large/ off/ report): "
        ).lower()

        if choice == "off":
            machine_is_on = False
        elif choice == "report":
            machine.show_report()
        elif choice in recipes:
            order = recipes[choice]
            ingredients = order["ingredients"]

            if machine.check_resources(ingredients):
                coins = machine.process_coins()
                if machine.transaction_result(coins, order["cost"]):
                    machine.make_sandwich(choice, ingredients)
        else:
            print("Invalid selection. Please choose a listed option.")


if __name__ == "__main__":
    main()
