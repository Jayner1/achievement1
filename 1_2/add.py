a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))

c = a + b
print("The result is ", c)

recipe_1 = {'name': 'Tea', 'ingredients': [], 'cooking time': []}
recipe_2 = {'name': 'Oatmeal', 'ingredients': [], 'cooking time': []}
recipe_3 = {'name': 'Rice', 'ingredients': [], 'cooking time': []}
recipe_4 = {'name': 'Cereal', 'ingredients': [], 'cooking time': []}
recipe_5 = {'name': 'Omelette', 'ingredients': [], 'cooking time': []}


recipe_2['ingredients'].append({'name': 'water'})
recipe_2['ingredients'].append({'name': 'salt'})

recipe_5['ingredients'].append({'name': 'eggs'})
recipe_5['ingredients'].append({'name': 'peppers'})
recipe_5['ingredients'].append({'name': 'cheese'})

recipe_5['cooking time'].append({'amount':'5 minutes'})