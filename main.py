import coffe
import math
profit = 0
program_run = True
water_in_machine = int(coffe.resources["water"])
coffe_in_machine = int(coffe.resources["coffee"])
milk_in_machine = int(coffe.resources["milk"])
while program_run:
    print("What would you like? (espresso/latte/cappuccino:")
    coffe_type = input().lower()
    water_to_do = 0
    milk_to_do = 0
    coffe_to_do = 0
    def resources_sufficient(coffe_type):
        global water_to_do
        global milk_to_do
        global coffe_to_do
        coffe_to_do = coffe.MENU[coffe_type]
        coffe_ingredients = coffe_to_do["ingredients"]
        water_to_do = int(coffe_ingredients["water"])
        if coffe_type != "espresso":
            milk_to_do = int(coffe_ingredients["milk"])
        coffe_to_do = int(coffe_ingredients["coffee"])
        return coffe_to_do, water_to_do, milk_to_do

    def coffe_to_do_check(coffe_type):
        global water_in_machine
        global water_to_do
        global coffe_in_machine
        global coffe_to_do
        global enough_resources
        if coffe_type != "espresso":
            global milk_to_do
            global milk_in_machine
        is_water_enough = water_in_machine - water_to_do
        if coffe_type != "espresso":
            is_milk_enough = milk_in_machine - milk_to_do
        else:
            is_milk_enough = 0
        is_coffe_enough = coffe_in_machine - coffe_to_do
        if is_coffe_enough < 0 or is_milk_enough < 0 or is_water_enough < 0:
            print("sorry no ingredients wait for machine refill")
        else:
            enough_resources = True
            print("insert money")
            return enough_resources, coffe_to_do, milk_to_do, water_to_do

    def coffe_payment():
        global transaction_succes
        print(f"you have to pay: {coffe_cost}")
        quarters = int(input("insert quarters $0.25:"))
        dimes = int(input("insert dimes $0.10:"))
        nickles = int(input("insert nickles $0.05"))
        pennies = int(input("insert pennies $0.01"))
        payment = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
        is_enough = payment - coffe_cost
        if is_enough >= 0:
            print(f"Here is your change {round(is_enough, 2)}")
            transaction_succes = True
            return transaction_succes
        else:
            print("not enough money")


    if coffe_type == "off":
        program_run = False
    elif coffe_type == "report":
        print(f" coffe: {coffe_in_machine}")
        print(f" milk: {milk_in_machine}")
        print(f" water: {water_in_machine}")
        print(f" profit: {profit}")
    elif coffe_type == "latte" or coffe_type == "espresso" or coffe_type == "cappuccino":
        coffe_cost_type = coffe.MENU[coffe_type]
        transaction_succes = False
        enough_resources = False
        resources_sufficient(coffe_type)
        coffe_to_do_check(coffe_type)
        coffe_cost = float(coffe_cost_type["cost"])
        if enough_resources == True:
            coffe_payment()
        if transaction_succes == True:
            profit += coffe_cost
            print(f"Here is your {coffe_type}")
            coffe_in_machine = coffe_in_machine - coffe_to_do
            milk_in_machine -= milk_to_do
            water_in_machine -= water_to_do








