from nutrition_calc import *

pork = recipe('smoked mississippi pork roast')
pork.servings = 32

pork_shoulder = ingredient('pork shoulder butt')
pork_shoulder.servings = 32
pork_shoulder.calories = 210
pork_shoulder.fat = 14
pork_shoulder.saturated_fat = 5
pork_shoulder.cholesterol = 70
pork_shoulder.sodium = 70
pork_shoulder.protein = 20
pork_shoulder.iron = 1.3
pork_shoulder.potassium = 360
pork_shoulder.product_url = 'https://www.dillons.com/p/kroger-pork-shoulder-butt/0020799300000'

seasoning = ingredient('all purpose seasoning')
seasoning.servings = 8
seasoning.sodium = 210
seasoning.product_url = 'https://www.dillons.com/p/kinder-s-butcher-s-all-purpose-seasoning/00755795375453'

butter = ingredient('butter')
butter.servings = 8
butter.fat = 11
butter.saturated_fat = 7
butter.cholesterol = 30
butter.product_url = 'https://www.dillons.com/p/kroger-unsalted-butter-sticks/0001111089305'

ranch_mix = ingredient('ranch dip mix')
ranch_mix.servings = 16
ranch_mix.sodium = 210
ranch_mix.carbohydrate = 1
ranch_mix.potassium = 10
ranch_mix.product_url = 'https://www.dillons.com/p/kroger-ranch-dip-mix/0001111070875'

gravy_mix = ingredient('pork gravy mix')
gravy_mix.servings = 4
gravy_mix.calories = 20
gravy_mix.sodium = 350
gravy_mix.carbohydrate = 4
gravy_mix.protein = 1
gravy_mix.calcium = 10
gravy_mix.potassium = 10
gravy_mix.product_url = 'https://www.dillons.com/p/kroger-pork-flavored-gravy-mix/0001111071993'

pepperocini = ingredient('pepperocini')
pepperocini.servings = 8/3
pepperocini.calories = 5
pepperocini.sodium = 330
pepperocini.carbohydrate = 1

pork.add_ingredient(pork_shoulder)
pork.add_ingredient(seasoning)
pork.add_ingredient(butter)
pork.add_ingredient(ranch_mix)
pork.add_ingredient(gravy_mix)
pork.add_ingredient(pepperocini)

pork.latex_nutrition_label()