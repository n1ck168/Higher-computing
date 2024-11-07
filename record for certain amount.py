#create record for certain number + search through record

from dataclasses import dataclass
@dataclass
class recipe () :
    RecipeTitle : int = 0
    mainingredient : str = ''
    costperportion : int = 0
    averageRating = 0
    CookingTime = 0

recipedetails = [ recipe ( ) for x in range (5)]

for i in range (len(recipedetails)):
    recipedetails[i].cookingtime > 10
    print(recipedetails[i]... whatever variable