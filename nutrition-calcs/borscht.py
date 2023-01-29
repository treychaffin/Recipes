from nutrition_calc import *

borscht = recipe('borscht')
borscht.servings = 4

oil = ingredient('avocado oil')
oil.servings = 2
oil.calories = 120
oil.fat = 14
oil.saturated_fat = 1.5
oil.polyunsaturated_fat = 2
oil.monounsaturated_fat = 10
oil.product_url = 'https://www.dillons.com/p/simple-truth-organic-refined-avocado-oil-bottle/0001111003441'

onion = ingredient('yellow onion')
onion.servings = 1
onion.calories = 54
onion.fat = 0.1
onion.sodium = 1.4
onion.carbohydrate = 12
onion.fiber = 2.7
onion.protein = 1.2
onion.calcium = 21
onion.iron = 0.4
onion.potassium = 260
onion.nutrition_url = 'https://www.nutritionvalue.org/Onions%2C_raw%2C_yellow_790646_nutritional_value.html'

celery_root = ingredient('celery')
celery_root.servings = 1
celery_root.calories = 288
celery_root.fat = 2.2
celery_root.sodium = 340
celery_root.carbohydrate = 31
celery_root.fiber = 6.1
celery_root.sugar = 5.5
celery_root.protein = 4.8
celery_root.nutrition_url = 'https://www.nutritionvalue.org/public_ingredient_8111.html?size=12+oz+%3D+340.19+g'

turnip = ingredient('turnip')
turnip.servings = 1
turnip.calories = 34
turnip.fat = 0.1
turnip.sodium = 80
turnip.carbohydrate = 7.7
turnip.fiber = 2.2
turnip.sugar = 4.6
turnip.protein = 1.1
turnip.calcium = 36
turnip.iron = 0.4
turnip.potassium = 229
turnip.nutrition_url = 'https://www.nutritionvalue.org/Turnip%2C_raw_75129000_nutritional_value.html?size=1+whole+%3D+120+g'

salt = ingredient('salt')
salt.servings = 1
salt.sodium = 2325
salt.calcium = 1.4
salt.potassium = 0.5
salt.nutrition_url = 'https://www.nutritionvalue.org/Salt%2C_table_nutritional_value.html?size=1+tsp+%3D+6+g'


beets = ingredient('beets')
beets.servings = 1
beets.calories = 183
beets.fat = 0.7
beets.saturated_fat = 0.1
beets.sodium = 332
beets.carbohydrate = 41
beets.fiber = 12
beets.sugar = 29
beets.protein = 6.9
beets.calcium = 68
beets.iron = 3.4
beets.potassium = 1382
beets.nutrition_url = 'https://www.nutritionvalue.org/Beets%2C_raw_nutritional_value.html?size=15+oz+%3D+425.24+g'

tomato = ingredient('tomatoes')
tomato.servings = 1
tomato.calories = 77
tomato.fat = 0.9
tomato.saturated_fat = 0.1
tomato.sodium = 21
tomato.carbohydrate = 17
tomato.fiber = 5.1
tomato.sugar = 11
tomato.protein = 3.7
tomato.calcium = 43
tomato.iron = 1.2
tomato.potassium = 1008
tomato.nutrition_url = 'https://www.nutritionvalue.org/Tomatoes%2C_raw_74101000_nutritional_value.html?size=15+oz+%3D+425.24+g'

stock = ingredient('beef stock')
stock.servings = 3.5
stock.calories = 20
stock.sodium = 510
stock.carbohydrate = 2
stock.sugar = 1
stock.protein = 3
stock.nutrition_url = 'https://www.nutritionvalue.org/Beef_cooking_stock_by_Hy-Vee%2C_Inc._528807_nutritional_value.html'

pepper = ingredient('black pepper')
pepper.servings = 1/4
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

kielbasa = ingredient('kielbasa')
kielbasa.servings = 12/2
kielbasa.calories = 180
kielbasa.fat = 16
kielbasa.saturated_fat = 5
kielbasa.cholesterol = 30
kielbasa.sodium = 320
kielbasa.carbohydrate = 4
kielbasa.sugar = 2
kielbasa.protein = 6
kielbasa.calcium = 20
kielbasa.iron = 0.36
kielbasa.product_url = 'https://www.dillons.com/p/kroger-polska-kielbasa-sausage/0001111096788'


dill = ingredient('fresh dill')
dill.servings = 1
dill.calories = 1.8
dill.sodium = 2.6
dill.carbohydrate = 0.3
dill.fiber = 0.1
dill.protein = 0.2
dill.calcium = 8.8
dill.iron = 0.3
dill.potassium = 31
dill.nutrition_url = 'https://www.nutritionvalue.org/Dill_weed%2C_fresh_nutritional_value.html?size=4.25+g'

sour_cream = ingredient('sour cream')
sour_cream.servings = 1/4
sour_cream.calories = 475
sour_cream.fat = 46
sour_cream.saturated_fat = 24
sour_cream.cholesterol = 142
sour_cream.sodium = 74
sour_cream.carbohydrate = 11
sour_cream.sugar = 8.2
sour_cream.protein = 5.9
sour_cream.calcium = 242
sour_cream.iron = 0.2
sour_cream.potassium = 300
sour_cream.nutrition_url = 'https://www.nutritionvalue.org/Sour_cream%2C_regular_12310100_nutritional_value.html'

borscht.add_ingredient(oil)
borscht.add_ingredient(onion)
borscht.add_ingredient(celery_root)
borscht.add_ingredient(turnip)
borscht.add_ingredient(salt)
borscht.add_ingredient(beets)
borscht.add_ingredient(tomato)
borscht.add_ingredient(stock)
borscht.add_ingredient(pepper)
borscht.add_ingredient(kielbasa)
borscht.add_ingredient(dill)
borscht.add_ingredient(sour_cream)

borscht.latex_nutrition_label()