from nutrition_calc import *

pork_burritos = recipe('pulled pork burritos')
pork_burritos.servings = 8

pulled_pork = ingredient('pulled pork')
pulled_pork.servings = 3
pulled_pork.calories = 212.92
pulled_pork.fat = 16.75
pulled_pork.saturated_fat = 6.75
pulled_pork.cholesterol = 77.5
pulled_pork.sodium = 298.75
pulled_pork.carbohydrate = 1.08
pulled_pork.protein = 20.12
pulled_pork.calcium = 1.25
pulled_pork.iron = 1.3
pulled_pork.potassium = 366.25

avocado_oil = ingredient('avocado oil')
avocado_oil.servings = 3
avocado_oil.calories = 120
avocado_oil.fat = 14
avocado_oil.saturated_fat = 1.5
avocado_oil.polyunsaturated_fat = 2
avocado_oil.monounsaturated_fat = 10
avocado_oil.product_url = 'https://www.dillons.com/p/simple-truth-organic-refined-avocado-oil-bottle/0001111003441'

green_pepper = ingredient('green pepper')
green_pepper.servings = 1
green_pepper.calories = 24
green_pepper.fat = 0.2
green_pepper.saturated_fat = 0.1
green_pepper.sodium = 3.6
green_pepper.carbohydrate = 5.6
green_pepper.fiber = 2
green_pepper.sugar = 2.9
green_pepper.protein = 1
green_pepper.calcium = 12
green_pepper.iron = 0.4
green_pepper.potassium = 210
green_pepper.nutrition_url = 'https://www.nutritionvalue.org/Pepper%2C_raw%2C_green%2C_sweet_75122100_nutritional_value.html?size=1+regular+%3D+120+g'

onion = ingredient('red onion')
onion.servings = 0.5
onion.calories = 87
onion.fat = 0.2
onion.carbohydrate = 20
onion.fiber = 4.3
onion.protein = 1.9
onion.calcium = 33
onion.iron = 0.5
onion.potassium = 388
onion.nutrition_url = 'https://www.nutritionvalue.org/Onions%2C_raw%2C_red_790577_nutritional_value.html'

garlic = ingredient('garlic')
garlic.servings = 2
garlic.calories = 4.5
garlic.sodium = 0.5
garlic.carbohydrate = 1
garlic.fiber = 0.1
garlic.protein = 0.2
garlic.calcium = 5.4
garlic.iron = 0.1
garlic.potassium = 12
garlic.nutrition_url = 'https://www.nutritionvalue.org/Garlic%2C_raw_nutritional_value.html?size=1+clove+%3D+3+g'

cauliflower = ingredient('cauliflower rice')
cauliflower.servings = 283.5/85
cauliflower.calories = 20
cauliflower.sodium = 20
cauliflower.carbohydrate = 4
cauliflower.fiber = 2
cauliflower.sugar = 2
cauliflower.protein = 2
cauliflower.calcium = 19
cauliflower.potassium = 164
cauliflower.vitamin_c = 41
cauliflower.product_url = 'https://www.dillons.com/p/green-giant-gluten-free-cauliflower-riced-veggies/0019056912310'

cilantro = ingredient('cilantro')
cilantro.servings = 3
cilantro.calories = 0.2
cilantro.sodium = 0.5
cilantro.calcium = 0.7
cilantro.potassium = 5.2
cilantro.nutrition_url = 'https://www.nutritionvalue.org/Cilantro%2C_raw_75109550_nutritional_value.html?size=1+g'

beans = ingredient('black beans')
beans.servings = 3.5
beans.calories = 110
beans.sodium = 400
beans.carbohydrate = 2
beans.fiber = 5
beans.sugar = 1
beans.protein = 7
beans.calcium = 60
beans.iron = 2
beans.potassium = 490
beans.product_url = 'https://www.dillons.com/p/kroger-black-beans/0001111072567'

salt = ingredient('salt')
salt.servings = 2
salt.sodium = 2325
salt.calcium = 1.4
salt.potassium = 0.5
salt.nutrition_url = 'https://www.nutritionvalue.org/Salt%2C_table_nutritional_value.html?size=1+tsp+%3D+6+g'

pepper = ingredient('black pepper')
pepper.servings = 1
pepper.calories = 5.8
pepper.fat = 0.1
pepper.sodium = 0.5
pepper.carbohydrate = 1.5
pepper.fiber = 0.6
pepper.protein = 0.2
pepper.calcium = 10
pepper.iron = 0.2
pepper.potassium = 31
pepper.nutrition_url = 'https://www.nutritionvalue.org/Spices%2C_black%2C_pepper_nutritional_value.html'

lime = ingredient('lime')
lime.servings = 0.5
lime.calories = 20
lime.fat = 0.1
lime.sodium = 1.3
lime.carbohydrate = 6.9
lime.fiber = 1.8
lime.sugar = 1.1
lime.protein = 0.5
lime.calcium = 21
lime.iron = 0.4
lime.potassium = 66
lime.nutrition_url = 'https://www.nutritionvalue.org/Lime%2C_raw_61116010_nutritional_value.html?size=1+fruit+%3D+65+g'

tortilla = ingredient('tortilla')
tortilla.servings = 8
tortilla.calories = 80
tortilla.fat = 2
tortilla.sodium = 440
tortilla.carbohydrate = 24
tortilla.fiber = 17
tortilla.protein = 8
tortilla.calcium = 103
tortilla.potassium = 2

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
cheese.product_url = 'https://www.dillons.com/p/kroger-shredded-mexican-style-cheese-blend/0001111050204'

pork_burritos.add_ingredient(pulled_pork)
pork_burritos.add_ingredient(avocado_oil)
pork_burritos.add_ingredient(green_pepper)
pork_burritos.add_ingredient(onion)
pork_burritos.add_ingredient(garlic)
pork_burritos.add_ingredient(cauliflower)
pork_burritos.add_ingredient(cilantro)
pork_burritos.add_ingredient(beans)
pork_burritos.add_ingredient(salt)
pork_burritos.add_ingredient(pepper)
pork_burritos.add_ingredient(lime)
pork_burritos.add_ingredient(tortilla)
pork_burritos.add_ingredient(cheese)


pork_burritos.latex_nutrition_label()