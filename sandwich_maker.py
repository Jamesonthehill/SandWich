
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        # TA CHANGE START: verify every required ingredient before accepting payment.
        for item, amount_needed in ingredients.items():
            if amount_needed > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True
        # TA CHANGE END

    def make_sandwich(self, sandwich_size, order_ingredients):
        # TA CHANGE START: deduct ingredients only after a successful transaction.
        for item, amount_needed in order_ingredients.items():
            self.machine_resources[item] -= amount_needed
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")
        # TA CHANGE END
