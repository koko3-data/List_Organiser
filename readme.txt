

Task: Smart Shopping List Organizer
Scenario:
Imagine you are building a smart shopping list manager that helps users organize and optimize their grocery lists.

Level 1: Basic Shopping List
Ask the user to enter a list of grocery items, separated by commas.
Store them in a Python list.
Display the sorted shopping list.
Example Input:

Enter your shopping items (comma-separated): milk, eggs, bread, bananas
Example Output:

Your shopping list:
1. Bananas
2. Bread
3. Eggs
4. Milk
Level 2: Avoiding Duplicates
Modify the program to remove duplicate items automatically.
Display the cleaned-up list.
Example Input:

Enter your shopping items: milk, eggs, bread, milk, bread, bananas
Example Output:

Your shopping list:
1. Bananas
2. Bread
3. Eggs
4. Milk
Level 3: Categorizing Items
Enhance the program to categorize items based on predefined groups.
Example categories:
Dairy: milk, cheese, yogurt
Fruits: apples, bananas, oranges
Bakery: bread, croissant, bagel
Other: items that don’t fit predefined categories.
Example Input:

Enter your shopping items: milk, cheese, apples, bread, chocolate
Example Output:

Your categorized shopping list:
Dairy:
- Cheese
- Milk

Fruits:
- Apples

Bakery:
- Bread

Other:
- Chocolate
Level 4: Prioritizing Essentials
Some items are more urgent than others. Let the user mark essential items by adding a ! at the end (e.g., "milk!").
Display essential items first, then the rest.
Example Input:

Enter your shopping items: milk!, cheese, apples, bread!, chocolate
Example Output:

Your prioritized shopping list:
1. Bread (Essential)
2. Milk (Essential)
3. Apples
4. Cheese
5. Chocolate
Level 5: Budget-Friendly Shopping
Allow the user to add estimated prices for items.
Calculate the total estimated cost of their shopping.
If the user provides a budget, check if they are within the limit and suggest adjustments.
Example Input:


Enter your shopping items with prices (format: item=price): milk=2.5, bread=1.8, apples=3, chocolate=5
Enter your budget: 7
Example Output:

Your total estimated cost: $12.3
You are over budget by $5.3! Consider removing chocolate.
Bonus Level: Saving & Loading Shopping Lists
Let users save their shopping list to a file (shopping_list.txt).
Allow users to load previous shopping lists when they reopen the program.

