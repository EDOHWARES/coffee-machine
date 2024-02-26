# Author: Edoh Emmanuel Gideon
# Date: February 25, 2024
# Description: This Python script performs simulates a coffee machine.

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def check_resource_sufficiency(coffee_type, menu, resource):
    """
    Check if resource to make coffee is available.
    :param coffee_type: The type of coffee the user wants.
    :param menu: The menu containing the type of coffee's details.
    :param resource: The available resource to make coffee.
    :return: A list, containing a dict that states "TRUE" and the insufficient resources,
    otherwise; returns a list that contains a dict that states "FALSE".
    """
    coffee_type = menu[f"{coffee_type}"]
    coffee_type_ingredient = coffee_type["ingredients"]
    coffee_type_water, coffee_type_coffee, coffee_type_milk = [coffee_type_ingredient["water"],
                                                               coffee_type_ingredient["coffee"],
                                                               coffee_type_ingredient.get("milk")]

    r = []
    if (coffee_type_water > resource["water"] or coffee_type_coffee > resource["coffee"] or
            coffee_type_milk > resource.get("milk")):
        p = {"pass": False}
        r.append(p)
        if coffee_type_water > resource["water"]:
            r.append("water")
        if coffee_type_coffee > resource["coffee"]:
            r.append("coffee")
        if coffee_type_milk > resource["milk"]:
            r.append("milk")
        else:
            pass

        return r
    else:
        p = {"pass": True}
        r.append(p)

        return r


def prompt_to_check_report():
    """
    Prompts user to input a report so as the view the resource details
    :return: A string telling user to input "REPORT"
    """
    p = '[Wanna check report on available resources? Input "report]"'

    return p


def process_coins():
    """
    Process inputted coins
    :return: The inputted coins in a dollar-converted-form.
    """
    print("Please insert coins...")
    query = "Invalid input! Input has to be a digit..."
    quarters = ""
    while not quarters.isdigit():
        quarters = input("How many quarters?: ")

        if not quarters.isdigit():
            print(query)

    dimes = ""
    while not dimes.isdigit():
        dimes = input("How many dimes?: ")

        if not quarters.isdigit():
            print(query)

    nickels = ""
    while not nickels.isdigit():
        nickels = input("How many nickels?: ")

        if not nickels.isdigit():
            print(query)

    pennies = ""
    while not pennies.isdigit():
        pennies = input("How many pennies?: ")

        if not pennies.isdigit():
            print(query)

    quarters = int(quarters)
    dimes = int(dimes)
    nickels = int(nickels)
    pennies = int(pennies)

    dict_of_coins = {
        "quarters": quarters,
        "dimes": dimes,
        "nickels": nickels,
        "pennies": pennies
    }

    # convert dict_of_coins to dollar
    in_dollar = 0
    in_dollar += dict_of_coins["quarters"] * 0.25
    in_dollar += dict_of_coins["dimes"] * 0.10
    in_dollar += dict_of_coins["nickels"] * 0.05
    in_dollar += dict_of_coins["pennies"] * 0.01

    return in_dollar


def modify_resource(menu, coffee_type, resource):
    """
    Modifies the resources; water, coffee, milk and money.
    :param menu: The general menu that contains the three coffee's data.
    :param coffee_type: The type of coffee user wants.
    :param resource: The coffee machine's resources
    :return: Nothing
    """
    resource["water"] = resource["water"] - menu[f"{coffee_type}"]["ingredients"]["water"]
    resource["milk"] = resource["milk"] - menu[f"{coffee_type}"]["ingredients"]["milk"]
    resource["coffee"] = resource["coffee"] - menu[f"{coffee_type}"]["ingredients"]["coffee"]

    resource["money"] = resource["money"] + menu[f"{coffee_type}"]["cost"]


def ask_for_refill():
    """
    Ask for a refill of the coffee machine
    :return: True if user wants a refill, otherwise: False.
    """
    refill = ""
    while refill != "yes" and refill != "no":
        refill = input("Wanna refill coffee machine? (yes or no): ").lower()

        if not refill:
            print("Input yes or no!")
        else:
            pass

    if refill == "yes":
        return True
    else:
        return False


user_want = ""


def main():
    global user_want
    while user_want != "off":
        user_want = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if user_want == "report":
            print(f"""
            Water: {resources["water"]}ml
            Milk: {resources["milk"]}ml
            Coffee: {resources["coffee"]}g
            Money: ${resources["money"]}
            
            
            SECRET KEY ->
            To_Refill: input "refill"
            """)
        elif user_want == "off":
            print("Coffee machine switched off successfully!")
        elif user_want == "espresso" or user_want == "latte" or user_want == "cappuccino":
            if check_resource_sufficiency(user_want, MENU, resources)[0]["pass"]:
                funds_in_dollar = process_coins()
                if funds_in_dollar < MENU["{}".format(user_want)]["cost"]:
                    print(f"Sorry, ${funds_in_dollar} not enough money! Money refunded...")
                elif funds_in_dollar == MENU["{}".format(user_want)]["cost"]:
                    modify_resource(MENU, user_want, resources)
                    print(f"""
                    You made an exact cost payment of ${round(funds_in_dollar, 2)}
                    Here is your {user_want}, ENJOY!
                    """)
                else:
                    modify_resource(MENU, user_want, resources)
                    print(f"""
                    Coins in dollar: ${round(funds_in_dollar, 2)}
                    Here is your change: ${round(funds_in_dollar - MENU["{}".format(user_want)]["cost"], 2)}
                    Here is your {user_want}, ENJOY!
                    """)
            else:
                message = "Sorry there is not enough "
                insufficient_items = []
                for result in check_resource_sufficiency(user_want, MENU, resources)[1:]:
                    insufficient_items.append(result)

                if len(insufficient_items) == 1:
                    print(message + "{}".format(insufficient_items[0]))
                    print(prompt_to_check_report())
                elif len(insufficient_items) == 2:
                    print("{}{}".format(message, "{} and {}".format(insufficient_items[0], insufficient_items[1])))
                    print(prompt_to_check_report())
                elif len(insufficient_items) == 3:
                    print("{0}{1}".format(message, "{}, {} and {}".format(insufficient_items[0], insufficient_items[1],
                                                                          insufficient_items[2])))
                    print(prompt_to_check_report())

        elif user_want != "espresso" and user_want != "latte" and user_want != "cappuccino" and user_want != "refill":
            print("[Input must be any of espresso, latte or cappuccino!]")
        elif user_want == "refill":
            try:
                def restart():
                    import sys
                    print("""
                    Refilling now .......
                    
                    .....................
                    
                    Successful!
                    """)

                    import os
                    os.execv(sys.executable, ["python"] + sys.argv)
                restart()
            except FileNotFoundError:
                print("Something went wrong...")
        else:
            pass


if __name__ == "__main__":
    main()
