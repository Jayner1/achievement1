# Initialize empty list to store recipes
recipes_list = []
# Initialize empty list to store ingredients
ingredients_list = []

def take_recipe():
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = []
    while True:
        ingredient = input("Enter an ingredient or type 'done' to finish: ")
        if ingredient == 'done':
            break
        ingredients.append(ingredient)
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    return recipe

# Ask the user for the number of recipes they want to enter
n = int(input("How many recipes would you like to enter? "))

# Loop over n and get n recipes from the user
for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)

# Print out the list of recipes and ingredients
print("Recipes:")
for recipe in recipes_list:
    print(recipe)

print("Ingredients:")
for ingredient in ingredients_list:
    print(ingredient)

# Loop over recipes_list and determine the difficulty of each recipe
for recipe in recipes_list:
    cooking_time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])

    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

    recipe['difficulty'] = difficulty

# Loop over recipes_list and display each recipe in the specified format
for recipe in recipes_list:
    print(f"{recipe['name']} ({recipe['cooking_time']} minutes):")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print("- " + ingredient)
    print(f"Difficulty: {recipe['difficulty']}")
    print("")

all_ingredients = set()
for recipe in recipes_list:
    all_ingredients.update(recipe['ingredients'])

# Sort the ingredients in alphabetical order and print them
sorted_ingredients = sorted(all_ingredients)
print("All Ingredients: ")
for ingredient in sorted_ingredients:
    print("- {}".format(ingredient))