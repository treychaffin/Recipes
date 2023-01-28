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


breakfast_burritos.add_ingredient(avocado_oil)
breakfast_burritos.add_ingredient(russet_potato)
breakfast_burritos.add_ingredient(eggs)

print(breakfast_burritos.name)
print('           calories: ',breakfast_burritos.calories())
print('                fat: ',breakfast_burritos.fat())
print('      saturated fat: ',breakfast_burritos.saturated_fat())
print('          trans fat: ',breakfast_burritos.trans_fat())
print('polyunsaturated fat: ',breakfast_burritos.polyunsaturated_fat())
print('monounsaturated fat: ',breakfast_burritos.monounsaturated_fat())
print('        cholesterol: ',breakfast_burritos.cholesterol())
print('             sodium: ',breakfast_burritos.sodium())
print('       carbohydrate: ',breakfast_burritos.carbohydrate())
print('              fiber: ',breakfast_burritos.fiber())
print('              sugar: ',breakfast_burritos.sugar())
print('            protein: ',breakfast_burritos.protein())
print('            calcium: ',breakfast_burritos.calcium())
print('               iron: ',breakfast_burritos.iron())
print('         phosphorus: ',breakfast_burritos.phosphorus())
print('          potassium: ',breakfast_burritos.potassium())
print('         riboflavin: ',breakfast_burritos.riboflavin())
print('          vitamin a: ',breakfast_burritos.vitamin_a())
print('          vitamin c: ',breakfast_burritos.vitamin_c())
print('          vitamin d: ',breakfast_burritos.vitamin_d())
print('          vitamin e: ',breakfast_burritos.vitamin_e())
print('               zinc: ',breakfast_burritos.zinc())