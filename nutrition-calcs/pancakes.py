from nutrition_calc import *

pancakes = recipe('pancakes')
pancakes.servings = 1

cream_cheese = ingredient('cream cheese')
cream_cheese.servings = 2
cream_cheese.calories = 100
cream_cheese.fat = 12
cream_cheese.saturated_fat = 8
cream_cheese.cholesterol = 30

almond_flour = ingredient('almond flour')
almond_flour.servings = 1
almond_flour.calories = 90
almond_flour.fat = 8
almond_flour.saturated_fat = 0.5
almond_flour.carbohydrate = 3
almond_flour.fiber = 1
almond_flour.sugar = 1
almond_flour.protein = 3
almond_flour.calcium = 30
almond_flour.potassium = 100

butter = ingredient('butter')
butter.servings = 2
butter.calories = 100
butter.fat = 12
butter.saturated_fat = 8
butter.cholesterol = 30

eggs = ingredient('eggs')
eggs.servings = 1
eggs.calories = 70
eggs.fat = 5
eggs.saturated_fat = 1.5
eggs.polyunsaturated_fat = 1
eggs.monounsaturated_fat = 2
eggs.cholesterol = 185
eggs.sodium = 70
eggs.protein = 6
eggs.calcium = 20
eggs.iron = 0.72
eggs.phosphorus = 100
eggs.potassium = 70
eggs.riboflavin = 0.26
eggs.vitamin_a = 300
eggs.vitamin_d = 40
eggs.vitamin_e = 8
eggs.zinc = 0.6

pancakes.add_ingredient(cream_cheese)
pancakes.add_ingredient(almond_flour)
pancakes.add_ingredient(butter)
pancakes.add_ingredient(eggs)

pancakes.latex_nutrition_label()