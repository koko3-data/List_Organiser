import os
import json
shopping_categories = {
    "Fruits": [],
    "Bakery": [],
    "Dairy": [],
    "Others": []

}
item_cost = {}

        # data = json.load(file)
        # shopping_categories = data["category"]
        # item_cost = data["cost"]
while True:
        ask_user = input("Will you like to enter a list of shopping items (y/n) :  " ).lower()
        if ask_user == "n" :
            break
        elif ask_user == "y":
            print('\033[1;31m' + "Please prioritize urgent items by adding a '!' e.g Orange!, Bagel!"+ '\033[0m')
            user_input = input("Please enter shopping list e.g Orange , Apple (,): ").lower().split(",")
            save_user_input = [item.strip() for item in user_input]
            sorted_user_input = sorted(set(save_user_input))
            Essential = []
            Non_Essential = []
            for item in sorted_user_input:
                if item.endswith("!"):
                    Essential.append(item.strip("!") )
                else:
                    Non_Essential.append(item)
            sorted_items = Essential + Non_Essential

            # for index, items in enumerate (sorted_user_input, start= 1):
            #     print(f" {index}.{items}")
                #Level 2
            for index, item in enumerate(sorted_items, start=1):
                print(f" {index}.{item}")
            for item in sorted_items :
                if item in ["milk", "eggs", "butter" , "cheese" , "yogurt"] :
                    shopping_categories ["Dairy"] . append(item)
                elif item in ["apple", "banana", "orange" , "guava", "watermelon"] :
                    shopping_categories ["Fruits"] . append(item)
                elif item in ["bread", "croissant", "bagel", "cake"]:
                    shopping_categories["Bakery"].append(item)
                else:
                    shopping_categories["Others"].append(item)
                for key,value in shopping_categories.items():
                    for i in range(len(value)) :
                        if value[i] in Essential :
                            value[i] = f"{value[i]}(Essential)"

        print('\033[1;31m'+ "Your Prioritised shopping List"+'\033[0m')
        for key, value in shopping_categories.items():
            print(f"{key}: {','.join(value) if value else 'None'}")

        ask_user_budget = input('\033[1;31m'+"Please give an estimated budget amount for your shopping e.g 100  : "+'\033[0m')
        user_budget = float(ask_user_budget)


        for key,value in shopping_categories.items():
            for i in range(len(value)):
                item_name = value[i].replace("(Essential)", "").strip()
                while True:
                    try:
                        cost = float(input('\033[1;31m'+f"Enter cost per {item_name}: "+'\033[0m'))
                        item_cost[item_name] = cost
                        break
                    except ValueError:
                        print("Enter a valid cost of item. ")
        print("Your shopping list with cost per item")
        total_cost = 0
        for item_name, cost in item_cost.items():
            print(f"{item_name} : {cost}")
            total_cost +=cost
        print('\033[1;31m'+f"Total Estimated Cost of item = {total_cost}"+'\033[0m')
        if total_cost > user_budget :
            overdrawn_amount = total_cost - user_budget
            print('\033[1;31m'+f"You are over the budget by {overdrawn_amount}"'\033[0m')
        else:
            print('\033[1;31m'+"Your are within your Estimated Budget"+'\033[0m')






                    #Level 3
                # for key, item in shopping_categories.items():
                #     if item in sorted_user_input is ["Fruits"]:
                #         shopping_categories["Fruits"] . append(item)
                #     elif item in sorted_user_input is ["Bakery"] :
                #         shopping_categories["Bakery"] . append(item)
                #     elif item in sorted_user_input is ["Dairy"] :
                #         shopping_categories["Dairy"] . append(item)
                #     else:
                #         shopping_categories["Other"] . append(item)
                #     print(f" {key} : {item}")
                # for item in sorted_user_input:
                #     found_category = False
            #     for key,values in shopping_categories.items():
            #         if item in values:
            #             found_category = True
            #             break
            #     if not found_category:
            #         shopping_categories["Other"].append(item)
            #         print(f"{key}: {",". join(items)} )




