import pickle

def display_recipe(recipe):
    print("Recipe Name: {}".format(recipe['name']))
    print("Cooking Time: {}".format(recipe['cooking_time']))
    print("Ingredients: ")
    for ingredient in recipe['ingredients']:
        print(" - {}".format(ingredient))
    print("Difficulty: {}".format(recipe['difficulty']))


recipe = {
    'name': '...',
    'cooking_time': '...',
    'ingredients': [...],
    'difficulty': '...'
}

def search_ingredient(data):
    # Show all available ingredients
    print("Available ingredients:")
    for i, ingredient in enumerate(data['all_ingredients']):
        print("{}) {}".format(i+1, ingredient))

    try:
        # Ask user to choose an ingredient
        choice = int(input("Enter the number of the ingredient you want to search for: "))
        ingredient_searched = data['all_ingredients'][choice-1]

        # Search for the ingredient in each recipe
        print("Recipes containing {}:".format(ingredient_searched))
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
    except (ValueError, IndexError):
        # Handle incorrect input
        print("Invalid input. Please enter a number from the list.")

# Ask user for filename
filename = input("Enter the filename of your recipe data: ")

# Load data from file using pickle
try:
    with open(filename, 'rb') as f:
        data = pickle.load(f)
except FileNotFoundError:
    print("Error: file not found")
    exit()
else:
    # Perform recipe search by ingredient
    search_ingredient(data)

