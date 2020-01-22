cookbook = {
"sandwich":
{"ingredients": "ham, bread, cheese and tomatoes", "meal" : "lunch", "prep_time" : "60"},
"cake":
{"ingredients": "ham, bread, cheese and tomatoes", "meal" : "dessert", "prep_time" : "60"},
"salad":
{"ingredients": "ham, bread, cheese and tomatoes", "meal" : "lunch", "prep_time" : "60"}
}

def print_recipe(recipe):
    if recipe in cookbook:
        print("""
        Recipe for {}:
        Ingredient list: {}
        To be eaten for: {}
        Takes {} minutes of cooking
        """.format(recipe, cookbook[recipe]["ingredients"], 
        cookbook[recipe]["meal"], 
        cookbook[recipe]["prep_time"]))
    else:
        print("""This recipe doesnt exist in cookbook!
        """)

def del_recipe(recipe):
    if recipe in cookbook:
        del cookbook[recipe]
    else:
        print("""This recipe doesnt exist in cookbook!
        """)

def add_recipe(recipe, ingredients, meal, prep):
    cookbook[recipe] = {"ingredients" : ingredients, "meal" : meal, "prep_time" : prep}

def print_cookbook():
    for recipe in cookbook:
        print_recipe(recipe)

choice = "0"

while choice != "5":
    print("""Please select an option by typing the corresponding number:
    1: Add a recipe
    2: Delete a recipe
    3: Print a recipe
    4: Print the cookbook
    5: Quit""")
    choice = input()
    if choice == "1":
        add_recipe(input("Enter the name of your recipe: "), input("Ingredients ? "), 
        input("Meal type ? "), input("Preparation time? "))
    elif choice == "2":
        del_recipe(input("Which recipe do you want to delete? "))
    elif choice == "3":
        print_recipe(input("Which recipe do you want to print? "))
    elif choice == "4":
        print_cookbook()
    else:
        print("""This option does not exist, please type the corresponding number. 
To exit, enter 5.
""")
