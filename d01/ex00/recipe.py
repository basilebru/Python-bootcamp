class Recipe:
    def __init__(self, name = None, cooking_lvl = None, cooking_time = None, ingredients = None, recipe_type = None, description = None):
        
        #check if mandatory fields are empty
        if (name == None or cooking_lvl == None or cooking_time == None or ingredients == None or recipe_type == None):
            print("Recette: " + name + "\nOnly description field can be empty")
            exit()
        
        #check name
        if isinstance(name, str) == False:
            print("Recette: " + name + "\n-->Name should be str")
            exit()
        self.name = name

        #check cooking_lvl
        if isinstance(cooking_lvl, int) == False:
            print("Recette: " + name + "\n-->Cooking_lvl should be digit")
            exit()
        elif cooking_lvl > 5 or cooking_lvl < 1:
            print("Recette: " + name + "\n-->Cooking_lvl should be between 1 and 5")
            exit()
        else:
            self.cooking_lvl = cooking_lvl
        
        #check cooking time
        if isinstance(cooking_time, int) == False or cooking_time < 0:
            print("Recette: " + name + "\n-->Cooking_time should be a positive number")
            exit()
        else:
            self.cooking_time = cooking_time
        
        #check ingredients
        if isinstance(ingredients, list) == False:
            print("Recette: " + name + "\n-->Ingredients should be a list")
            exit()
        elif all(isinstance(n, str) for n in ingredients) == False:
            print("Recette: " + name + "\n-->All ingredients should be str")
            exit()
        else:
            self.ingredients = ingredients
        
        #check recipe type
        if recipe_type in {"starter", "lunch", "dessert"}:
            self.recipe_type = recipe_type
        else:
            print("Recette: " + name + "\n-->Recipe_type can be 'starter', 'lunch' or 'dessert'")
            exit()
        self.description = description
    
    def __str__(self):
        return ("Recipe name: " + self.name + 
        "\n--ingredients: " + ','.join([str(elem) for elem in self.ingredients]) +
        "\n--cooking time: " + str(self.cooking_time) +
        "\n--cooking lvl: " + str(self.cooking_lvl))