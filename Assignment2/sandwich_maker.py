class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Return True when the order can be made; otherwise return False."""
        for item, amount_needed in ingredients.items():
            if amount_needed > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the ingredients and announce the completed sandwich."""
        for item, amount_needed in order_ingredients.items():
            self.machine_resources[item] -= amount_needed

        print(f"{sandwich_size} sandwich is ready. Bon appetit!")
