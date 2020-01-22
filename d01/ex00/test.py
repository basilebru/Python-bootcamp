from book import Book
from recipe import Recipe

miam = Recipe("miam", 1, 55, ["poireau", "yahourt"], "lunch")
#print(miam)
tourte = Recipe("tourte", 1, 5, ["poireau", "carrottes"], "lunch")
#print (tourte)
crumble = Recipe("crumble", 1, -15, ["beurre", "sucre"], "dessert")
#print (crumble)
salade = Recipe("", 3, 10, ["huile", "vinaigrette"], "starter")
#print (salade)
mcdo = Recipe("mcdo", 1, 55, ["poireau", "frites"], "lunch")

book = Book("", {"starter" : [salade], "lunch" : [tourte, miam], "dessert" : [crumble]})
#print(book)

#book.get_recipe_by_name("crumble")
#book.get_recipes_by_types('lunch')

#book.add_recipe(mcdo)
print(book)