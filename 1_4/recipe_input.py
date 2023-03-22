import pickle

def take_recipe():

 # Ask the user for the recipe name, cooking time, and ingredients
    recipe_name = input("Enter the recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients = input("Enter the ingredients (seperated by commas): ").split(",")

# Calculate the difficulty of the recipe
    difficulty = calc_difficulty(cooking_time, len(ingredients))

# Gather all the attributes into a dictionary
    recipe = {
        "name": recipe_name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }

# Return the recipe dictionary
    return recipe

# Use cooking time and ingredients to set difficulty of recipe
def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"
    return difficulty

# Ask the user for the filename to load
filename = input("Enter the filename to load: ")

try:
    # Open the file and load its contents into the data variable
    with open(filename, "rb") as f:
        data = pickle.load(f)

except FileNotFoundError:
    # Create a new data dictionary with empty lists for recipes and ingredients
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }

except Exception as e:
    # Handle any other exceptions and print an error message
    print(f"Error loading file: {e}")
    data = {
        "recipes_list": [],
        "all_ingredients": []
    }

else:
    # Close the file stream
    f.close()

finally:
    # Extract the recipes and ingredients lists from the data dictionary
    recipes_list = data["recipes_list"]
    all_ingredients = data["all_ingredients"]


# Ask the user how many recipes they want to enter
num_recipes = int(input("How many recipes would you like to enter? "))

# Define an empty list to store the recipes
recipes_list = []

# Define an empty set to store all ingredients
all_ingredients = set()

# Loop through each recipe and call the take_recipe() function
for i in range(num_recipes):
    print(f"Enter details for Recipe #{i+1}:")
    recipe = take_recipe()
    recipes_list.append(recipe)
    
    # Add the ingredients of the current recipe to the set of all ingredients
    for ingredient in recipe["ingredients"]:
        all_ingredients.add(ingredient)

# Convert the set of all ingredients back to a list
all_ingredients = list(all_ingredients)

data = {
    "recipes_list": recipes_list,
    "all_ingredients": all_ingredients
}

# Ask the user for the filename
filename = input("Enter a filename to save the recipes: ")

# Open the file in binary write mode
with open(filename, "wb") as f:
    # Write the data to the file using pickle.dump()
    pickle.dump(data, f)
    
# Print a success message
print(f"The recipes have been saved to {filename}")