from nutrition_calc import *

# Breakfast Burritos
breakfast_burritos = recipe('breakfast burritos')
breakfast_burritos.servings = 8

avocado_oil = ingredient('avocado oil')
avocado_oil.servings = 3
avocado_oil.calories = 120
avocado_oil.fat = 14
avocado_oil.saturated_fat = 1.5
avocado_oil.polyunsaturated_fat = 2
avocado_oil.monounsaturated_fat = 10
avocado_oil.product_url = 'https://www.dillons.com/p/simple-truth-organic-refined-avocado-oil-bottle/0001111003441'

russet_potato = ingredient('russet potato')
russet_potato.servings = 1
russet_potato.calories = 168
russet_potato.fat = 0.2
russet_potato.saturated_fat = 0.1
russet_potato.trans_fat = 0
russet_potato.polyunsaturated_fat = 0.1
russet_potato.monounsaturated_fat = 0
russet_potato.cholesterol = 0
russet_potato.sodium = 24
russet_potato.potassium = 952
russet_potato.carbohydrate = 37
russet_potato.fiber = 4
russet_potato.sugar = 1.9
russet_potato.protein = 4.5
russet_potato.product_url = 'https://www.dillons.com/p/russet-potato/0000000004072'
russet_potato.nutrition_url = 'https://www.nutritionix.com/food/russet-potato'

eggs = ingredient('eggs')
eggs.servings = 12
eggs.calories = 70
eggs.fat = 5
eggs.saturated_fat = 1.5
eggs.trans_fat = 0
eggs.polyunsaturated_fat = 1
eggs.monounsaturated_fat = 2
eggs.cholesterol = 185
eggs.sodium = 70
eggs.carbohydrate = 0
eggs.protein = 6
eggs.calcium = 20
eggs.iron = 0.72
eggs.phosphorus = 100
eggs.potassium = 70
eggs.riboflavin = 0.26
eggs.vitamin_a = 300
eggs.vitamin_d = 40
eggs.vitamin_e = 8
eggs.zinc = 0
eggs.product_url = 'https://www.dillons.com/p/simple-truth-natural-cage-free-large-brown-eggs/0001111079770'

green_chiles = ingredient('green chiles')
green_chiles.servings = 4
green_chiles.calories = 5
green_chiles.sodium = 95
green_chiles.carbohydrate = 1
green_chiles.iron = 0.36
green_chiles.product_url = 'https://www.dillons.com/p/kroger-diced-green-chile-peppers/0001111084009'

sausage = ingredient('breakfast sausage links')
sausage.servings = 8 / 3
sausage.calories = 170
sausage.fat = 13
sausage.saturated_fat = 4.5
sausage.cholesterol = 45
sausage.sodium = 560
sausage.carbohydrate = 2
sausage.sugar = 1
sausage.protein = 10
sausage.iron = 1.1
sausage.potassium = 70
sausage.product_url = 'https://www.dillons.com/p/kroger-original-breakfast-sausage-links/0001111097293'

tortilla = ingredient('tortilla')
tortilla.servings = 8
tortilla.calories = 110
tortilla.fat = 4
tortilla.saturated_fat = 1.5
tortilla.sodium = 450
tortilla.carbohydrate = 31
tortilla.fiber = 23
tortilla.protein = 8
tortilla.calcium = 100
tortilla.iron = 1
tortilla.potassium = 30
tortilla.product_url = 'https://www.dillons.com/p/mission-carb-balance-low-carb-whole-wheat-burrito-tortillas/0007373100118'

cheese = ingredient('mexican blend shredded cheese')
cheese.servings = 8
cheese.calories = 110
cheese.fat = 9
cheese.saturated_fat = 5
cheese.cholesterol = 25
cheese.sodium = 170
cheese.carbohydrate = 1
cheese.protein = 6
cheese.calcium = 210

salt = ingredient('salt')
salt.servings = 1
salt.sodium = 2325
salt.calcium = 1.4
salt.potassium = 0.5
salt.nutrition_url = 'https://www.nutritionvalue.org/Salt%2C_table_nutritional_value.html?size=1+tsp+%3D+6+g'

pepper = ingredient('black pepper')
pepper.servings = 1
pepper.fat = 0.1
pepper.sodium = 0.5
pepper.carbohydrate = 1.5
pepper.fiber = 0.6
pepper.protein = 0.2
pepper.calcium = 10
pepper.iron = 0.2
pepper.potassium = 31


breakfast_burritos.add_ingredient(avocado_oil)
breakfast_burritos.add_ingredient(russet_potato)
breakfast_burritos.add_ingredient(eggs)
breakfast_burritos.add_ingredient(green_chiles)
breakfast_burritos.add_ingredient(sausage)
breakfast_burritos.add_ingredient(tortilla)
breakfast_burritos.add_ingredient(cheese)
breakfast_burritos.add_ingredient(salt)
breakfast_burritos.add_ingredient(pepper)

breakfast_burritos.latex_nutrition_label()