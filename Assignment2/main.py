import cashier
import data
import sandwich_maker


resources = data.resources
recipes = data.recipes

sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()


def show_report():
    print(f"Bread: {resources['bread']} slice(s)")
    print(f"Ham: {resources['ham']} slice(s)")
    print(f"Cheese: {resources['cheese']} ounce(s)")


def main():
    machine_is_on = True

    while machine_is_on:
        choice = input(
            "What would you like? (small/ medium/ large/ off/ report): "
        ).lower()

        if choice == "off":
            machine_is_on = False
        elif choice == "report":
            show_report()
        elif choice in recipes:
            order = recipes[choice]
            ingredients = order["ingredients"]

            if sandwich_maker_instance.check_resources(ingredients):
                coins = cashier_instance.process_coins()
                payment_accepted = cashier_instance.transaction_result(
                    coins, order["cost"]
                )
                if payment_accepted:
                    sandwich_maker_instance.make_sandwich(choice, ingredients)
        else:
            print("Invalid selection. Please choose a listed option.")


if __name__ == "__main__":
    main()
