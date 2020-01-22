from recipe import Recipe
import datetime

class Book:
    
    creation_date = datetime.datetime.now()
    last_update = datetime.datetime.now()

    def __init__(self, name, recipes_list):
        self.name = name
        self.recipes_list = recipes_list
    
    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        all = self.recipes_list['lunch'] + self.recipes_list['starter'] + self.recipes_list['dessert']
        recip = None
        for r in all:
            if r.name == name:
                recip = r
        #recip = [r for r in all if r.name == name]
        if recip != None:
            print(recip)
            return(recip)
        else:
            print("No recipe goes by this name")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in ['lunch', 'starter', 'dessert']:
            print("Not a valid type")
            exit()
        recipes = self.recipes_list[recipe_type]
        for recipe in recipes:
            print(recipe)
        return(recipes)
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        #check that its a correct recipe
        if isinstance(recipe, Recipe) == False:
            print("Please enter a valid recipe")
            exit()
        #check that the recipe is not already in the book
        for rec in self.recipes_list[recipe.recipe_type]:
            if rec.name == recipe.name:
                print("This recipe name already exists")
                exit()
        self.last_update = datetime.datetime.now()
        key = recipe.recipe_type
        self.recipes_list[key].append(recipe)

    def __str__(self):
        print(self.name)
        print(self.creation_date)
        all = self.recipes_list['lunch'] + self.recipes_list['starter'] + self.recipes_list['dessert']
        for r in all:
            print(r)
        #return(self.name + "\n" + str(self.creation_date))
        return("")