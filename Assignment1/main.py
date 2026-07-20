import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
# TA CHANGE START: create the objects used by the program.
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()
# TA CHANGE END




def main():
    # TA CHANGE START: run the sandwich machine until the user enters "off".
    machine_is_on = True

    while machine_is_on:
        choice = input(
            "What would you like? (small/ medium/ large/ off/ report): "
        ).lower()

        if choice == "off":
            machine_is_on = False
        elif choice == "report":
            print(f"Bread: {resources['bread']} slice(s)")
            print(f"Ham: {resources['ham']} slice(s)")
            print(f"Cheese: {resources['cheese']} ounce(s)")
        elif choice in recipes:
            order = recipes[choice]
            ingredients = order["ingredients"]

            if sandwich_maker_instance.check_resources(ingredients):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, order["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)
        else:
            print("Invalid selection. Please choose small, medium, large, report, or off.")
    # TA CHANGE END


if __name__ == "__main__":
    main()
