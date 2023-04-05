import mysql.connector

# Connect to MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="cf-python",
    password="password"
)

# Initialize a cursor object from conn
cursor = conn.cursor()

# Create a database called task_database if it doesn't exist.
cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")

# Use the task_database database
cursor.execute("USE task_database")

# Create a table called Recipes if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
""")

# Commit the changes and close the connection
conn.commit()
conn.close()

#MAIN MENU
def main_menu(conn, cursor):
    while True:
        print("Select an option:")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            create_recipe(conn, cursor)
        elif choice == 2:
            search_recipe(conn, cursor)
        elif choice == 3:
            update_recipe(conn, cursor)
        elif choice == 4:
            delete_recipe(conn, cursor)
        elif choice == 5:
            conn.commit()
            conn.close()
            break
        else:
            print("Invalid choice. Try again.")


def create_recipe(conn, cursor):
    # Collect recipe details
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time in minutes: "))
    ingredients = []
    while True:
        ingredient = input("Enter ingredient name (press enter to stop adding): ")
        if ingredient:
            ingredients.append(ingredient)
        else:
            break

    # Calculate recipe difficulty
    difficulty = calculate_difficulty(cooking_time, len(ingredients))

    # Convert ingredients list to comma-separated string
    ingredients_string = ", ".join(ingredients)

    # Build SQL query and execute
    query = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES (%s, %s, %s, %s)"
    values = (name, ingredients_string, cooking_time, difficulty)
    cursor.execute(query, values)
    conn.commit()

    print("Recipe created successfully!")


def search_recipe(conn, cursor):
    # Obtain the list of all ingredients
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    all_ingredients = []
    for row in results:
        ingredients = row[0].split(", ")
        for ingredient in ingredients:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    # Display all ingredients to the user and allow them to pick a number
    print("Choose an ingredient to search for:")
    for i, ingredient in enumerate(all_ingredients):
        print(f"{i + 1}. {ingredient}")
    choice = int(input("Enter the number of the ingredient: "))
    search_ingredient = all_ingredients[choice - 1]
    
    # Search for rows that contain the search ingredient within the ingredients column
    query = f"SELECT name, cooking_time, ingredients, difficulty FROM Recipes WHERE ingredients LIKE '%{search_ingredient}%'"
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Display the search results
    if len(results) == 0:
        print("No recipes found.")
    else:
        print(f"Search results for recipes containing {search_ingredient}:")
        for row in results:
            name, cooking_time, ingredients, difficulty = row
            print(f"Name: {name}")
            print(f"Cooking time: {cooking_time} minutes")
            print(f"Ingredients: {ingredients}")
            print(f"Difficulty: {difficulty}")
            print()

def update_recipe(conn, cursor):
    # Fetch all recipes
    cursor.execute("SELECT id, name FROM Recipes")
    recipes = cursor.fetchall()

    # List all recipes to user
    print("Select the recipe ID that you want to update:")
    for recipe in recipes:
        print(f"{recipe[0]}: {recipe[1]}")

    # Prompt user to select a recipe by id
    recipe_id = input("Recipe ID: ")

    # Prompt user to select column to update
    print("Select the column to update:")
    print("1: Name")
    print("2: Cooking Time")
    print("3: Ingredients")
    column_num = int(input("Column number: "))

    # Collect new value from user
    new_value = input("Enter the new value: ")

    # Update the column for the given recipe_id
    if column_num == 1:
        query = f"UPDATE Recipes SET name = '{new_value}' WHERE id = {recipe_id}"
    elif column_num == 2:
        query = f"UPDATE Recipes SET cooking_time = {new_value} WHERE id = {recipe_id}"
        # Recalculate difficulty
        cursor.execute(f"SELECT ingredients FROM Recipes WHERE id = {recipe_id}")
        ingredients = cursor.fetchone()[0].split(", ")
        difficulty = calculate_difficulty(int(new_value), ingredients)
        cursor.execute(f"UPDATE Recipes SET difficulty = '{difficulty}' WHERE id = {recipe_id}")
    elif column_num == 3:
        query = f"UPDATE Recipes SET ingredients = '{new_value}' WHERE id = {recipe_id}"
        # Recalculate difficulty
        ingredients = new_value.split(", ")
        cursor.execute(f"SELECT cooking_time FROM Recipes WHERE id = {recipe_id}")
        cooking_time = cursor.fetchone()[0]
        difficulty = calculate_difficulty(cooking_time, ingredients)
        cursor.execute(f"UPDATE Recipes SET difficulty = '{difficulty}' WHERE id = {recipe_id}")

    # Execute query and commit changes
    cursor.execute(query)
    conn.commit()

    print("Recipe updated successfully!")

def delete_recipe(cursor):
    # Display all the recipes in the table
    cursor.execute("SELECT id, name FROM Recipes")
    results = cursor.fetchall()
    print("Here are all the recipes in the table:")
    for row in results:
        print(row[0], "-", row[1])
    
    # Ask the user for the id of the recipe to be deleted
    recipe_id = input("Enter the ID of the recipe you want to delete: ")
    
    # Build and execute the query to delete the recipe
    delete_query = f"DELETE FROM Recipes WHERE id = {recipe_id}"
    cursor.execute(delete_query)
    print(f"Recipe with ID {recipe_id} has been deleted from the table.")
    
    # Commit the changes to the table
    cursor.connection.commit()
