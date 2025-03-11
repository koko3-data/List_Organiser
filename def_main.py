shopping_categories = {
    "Fruits": [],
    "Bakery": [],
    "Dairy": [],
    "Others": []

}
item_cost = {}


# def func_name():
#     input_name = input("Enter your name: ")
#     my_name = "my name is " +  input_name
#     print(my_name)
# func_name()

def user_input():
    ask_user = input("Will you like to enter a list of shopping items (y/n) :  " ).lower()
    if ask_user == 'n':
        return []
    elif ask_user == 'y':
        print('\033[1;31m' + "Please prioritize urgent items by adding a '!' e.g Orange!, Bagel!" + '\033[0m')
        shop_input = input("Please enter shopping list e.g Orange , Apple (,): ").lower().split(",")
        return shop_input



def sort_input(shop_input):
    sorted_list = [item.strip() for item in shop_input]
    save_sorted = sorted(set(sorted_list))
    return save_sorted

def essential_item(save_sorted):
    essential = []
    non_essential = []
    for item in save_sorted:
        if item.endswith("!"):
            essential.append(item.strip("!"))
        else:
            non_essential.append(item)
    sorted_list = essential + non_essential
    return sorted_list,essential


def user_budget():
    ask_user_budget = input('\033[1;31m' + "Please give an estimated budget amount for your shopping e.g 100  : " + '\033[0m')
    user_input_budget = float(ask_user_budget)
    return user_input_budget

def prioritise_item(sorted_list,shopping_categories,essential):
    for item in sorted_list:
        if item in ["milk", "eggs", "butter", "cheese", "yogurt"]:
            shopping_categories["Dairy"].append(item)
        elif item in ["apple", "banana", "orange", "guava", "watermelon"]:
            shopping_categories["Fruits"].append(item)
        elif item in ["bread", "croissant", "bagel", "cake"]:
            shopping_categories["Bakery"].append(item)
        else:
            shopping_categories["Others"].append(item)
        for key, value in shopping_categories.items():
            for i in range(len(value)):
                if value[i] in essential:
                    value[i] = f"{value[i]}(Essential)"
    print('\033[1;31m' + "Your Prioritised shopping List" + '\033[0m')
    for key, value in shopping_categories.items():
        print(f"{key}: {','.join(value) if value else 'None'}")

def user_cost(shopping_categories,item_cost,user_input_budget):
    for key, value in shopping_categories.items():
        for i in range(len(value)):
            item_name = value[i].replace("(Essential)", "").strip()
            while True:
                try:
                    cost = float(input('\033[1;31m' + f"Enter cost per {item_name}: " + '\033[0m'))
                    item_cost[item_name] = cost
                    break
                except ValueError:
                    print("Enter a valid cost of item. ")
    print("Your shopping list with cost per item")
    total_cost = 0
    for item_name, cost in item_cost.items():
        print(f"{item_name} : {cost}")
        total_cost += cost
    print('\033[1;31m' + f"Total Estimated Cost of item = {total_cost}" + '\033[0m')
    if total_cost > user_input_budget:
        overdrawn_amount = total_cost - user_input_budget
        print('\033[1;31m' + f"You are over the budget by {overdrawn_amount}"'\033[0m')
    else:
        print('\033[1;31m' + "Your are within your Estimated Budget" + '\033[0m')
#
# def save_file():


while True:
    my_actual_list = user_input()
    if not my_actual_list:
        break
    else:
        my_sorted_list = sort_input(my_actual_list)
        my_essential_list,essential_only = essential_item(my_sorted_list)
        my_budget_list = user_budget()
        my_priority_list = prioritise_item(my_essential_list,shopping_categories,essential_only)
        my_user_cost = user_cost(shopping_categories,item_cost,my_budget_list)


