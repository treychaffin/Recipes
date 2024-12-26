from nutrition_calc import *

oatmeal = recipe('lower carb carrot cake oatmeal')
oatmeal.servings = 6

eggs = ingredient('eggs')
eggs.servings = 2 # 2 eggs
eggs.nutrition_url = 'https://www.nutritionvalue.org/Egg%2C_fresh%2C_raw%2C_whole_nutritional_value.html'
eggs.calories = 72
eggs.fat = 4.8
eggs.saturated_fat = 1.6
eggs.cholesterol = 186
eggs.sodium = 71
eggs.carbohydrate = 0.4
eggs.fiber = 0
eggs.sugar = 0.2
eggs.protein = 6.3
eggs.vitamin_d = 40 # 1 mcg = 40 IU https://www.omnicalculator.com/health/mcg-to-iu-converter
eggs.calcium = 28
eggs.iron = 0.9
eggs.potassium = 69

swerve_brown_sugar = ingredient('swerve brown sugar') #serving size is 1 tsp
swerve_brown_sugar.servings = (1/3)*48 # 1/3 cup, 48 tsp/cup
swerve_brown_sugar.product_url = 'https://www.dillons.com/p/swerve-brown-sugar-replacement/0085270030037'
swerve_brown_sugar.calories = 0
swerve_brown_sugar.fat = 0
swerve_brown_sugar.sodium = 0
swerve_brown_sugar.carbohydrate = 4
swerve_brown_sugar.sugar = 0
swerve_brown_sugar.sugar_alcohols = 4
swerve_brown_sugar.protein = 0

cinnamon = ingredient('cinnamon')
cinnamon.servings = 1/2 # 1/2 tsp
cinnamon.nutrition_url = 'https://www.nutritionvalue.org/Spices%2C_ground%2C_cinnamon_nutritional_value.html'
cinnamon.calories = 6.4
cinnamon.fat = 0
cinnamon.sodium = 0.3
cinnamon.carbohydrate = 2.1
cinnamon.fiber = 1.4
cinnamon.sugar = 0.1
cinnamon.protein = 0.1
cinnamon.vitamin_d = 0
cinnamon.calcium = 26
cinnamon.iron = 0.2
cinnamon.potassium = 11

nutmeg = ingredient('nutmeg')
nutmeg.servings = 1/4 # 1/4 tsp
nutmeg.nutrition_url = 'https://www.nutritionvalue.org/Spices%2C_ground%2C_nutmeg_nutritional_value.html'
nutmeg.calories = 12
nutmeg.fat = 0.8
nutmeg.saturated_fat = 0.6
nutmeg.sodium = 0.4
nutmeg.carbohydrate = 1.1
nutmeg.fiber = 0.4
nutmeg.sugar = 0.1
nutmeg.protein = 0.1
nutmeg.vitamin_d = 0
nutmeg.calcium = 4.1
nutmeg.iron = 0.1
nutmeg.potassium = 16

baking_powder = ingredient('baking powder') #serving size is 1/8 tsp
baking_powder.servings = 8 # 1 tsp = 8 servings
baking_powder.product_url = 'https://www.nutritionvalue.org/Baking_powder_by_The_Kroger_Co._391680_nutritional_value.html'
baking_powder.calories = 0
baking_powder.fat = 0
baking_powder.sodium = 65
baking_powder.carbohydrate = 0
baking_powder.protein = 0
baking_powder.calcium = 20

salt = ingredient('salt') # servings size is 1 tsp
salt.servings = 1/2 # 1/2 tsp
salt.nutrition_url = 'https://www.nutritionvalue.org/Salt%2C_table_nutritional_value.html'
salt.calories = 0
salt.fat = 0
salt.sodium = 2325
salt.carbohydrate = 0
salt.protein = 0
salt.vitamin_d = 0
salt.calcium = 1.4
salt.iron = 0.1
salt.potassium = 0.5

carbmaster_skim_milk = ingredient('carbmaster skim milk') #serving size is 8 fl oz (1 cup)
carbmaster_skim_milk.servings = 2 # 2 cups
carbmaster_skim_milk.product_url = 'https://www.dillons.com/p/kroger-carbmaster-ultra-filtered-skim-milk/0001111008303'
carbmaster_skim_milk.calories = 60
carbmaster_skim_milk.fat = 0
carbmaster_skim_milk.saturated_fat = 0
carbmaster_skim_milk.trans_fat = 0
carbmaster_skim_milk.cholesterol = 10 #10mg
carbmaster_skim_milk.sodium = 95 #95mg
carbmaster_skim_milk.carbohydrate = 3 #3g
carbmaster_skim_milk.sugar = 3 #3g
carbmaster_skim_milk.fibers = 0
carbmaster_skim_milk.protein = 11 #11g
carbmaster_skim_milk.calcium = 370 #370mg
carbmaster_skim_milk.iron = 0
carbmaster_skim_milk.potassium = 300 #300mg
carbmaster_skim_milk.vitamin_a = 218.16 #150mcg = 500IU (retinol) https://www.omnicalculator.com/health/mcg-to-iu-converter
carbmaster_skim_milk.vitamin_d = 100 #2.5mcg = 100IU https://www.omnicalculator.com/health/mcg-to-iu-converter

oats = ingredient('oats') #serving size is 1/2 cup
oats.servings = 6 # 3 cups = 6 servings
oats.nutrition_url = 'https://www.nutritionvalue.org/Oats_by_The_Quaker_Oats_Company_538678_nutritional_value.html'
oats.calories = 150
oats.fat = 3
oats.saturated_fat = 0.5
oats.carbohydrate = 27
oats.fiber = 4
oats.sugar = 1
oats.protein = 5
oats.calcium = 0
oats.iron = 1.4

walnuts = ingredient('walnuts')
walnuts.servings = 1/3 # 1/3 cup
walnuts.nutrition_url = 'https://www.nutritionvalue.org/Nuts%2C_english%2C_walnuts_nutritional_value.html'
walnuts.calories = 765
walnuts.fat = 76
walnuts.saturated_fat = 7.2
walnuts.sodium = 2.3
walnuts.carbohydrate = 16
walnuts.fiber = 7.8
walnuts.sugar = 3.1
walnuts.protein = 18
walnuts.vitamin_d = 0
walnuts.calcium = 115
walnuts.iron = 3.4
walnuts.potassium = 516

raisins = ingredient('raisins')
raisins.servings = 1/3 # 1/3 cup
raisins.nutrition_url = 'https://www.nutritionvalue.org/Raisins%2C_seedless%2C_dark_nutritional_value.html'
raisins.calories = 493
raisins.fat = 0.4
raisins.saturated_fat = 0.2
raisins.sodium = 43
raisins.carbohydrate = 131
raisins.fiber = 7.4
raisins.sugar = 108
raisins.protein = 5.5
raisins.vitamin_d = 0
raisins.calcium = 102
raisins.iron = 3
raisins.potassium = 1228

creamcheese = ingredient('cream cheese')
creamcheese.servings = 4 # 4 oz
creamcheese.nutrition_url = 'https://www.nutritionvalue.org/Cheese%2C_cream_nutritional_value.html'
creamcheese.calories = 51
creamcheese.fat = 5
creamcheese.saturated_fat = 2.9
creamcheese.cholesterol = 15
creamcheese.sodium = 46
creamcheese.carbohydrate = 0.8
creamcheese.fiber = 0
creamcheese.sugar = 0.6
creamcheese.protein = 0.9
creamcheese.vitamin_d = 0
creamcheese.calcium = 14
creamcheese.iron = 0
creamcheese.potassium = 19

egg_yolk = ingredient('egg yolk')
egg_yolk.servings = 1 # 1 egg yolk
egg_yolk.nutrition_url = 'https://www.nutritionvalue.org/Egg%2C_fresh%2C_raw%2C_yolk_nutritional_value.html'
egg_yolk.calories = 55
egg_yolk.fat = 4.5
egg_yolk.saturated_fat = 1.6
egg_yolk.cholesterol = 184
egg_yolk.sodium = 8.2
egg_yolk.carbohydrate = 0.6
egg_yolk.fiber = 0
egg_yolk.sugar = 0.1
egg_yolk.protein = 2.7
egg_yolk.vitamin_d = 36 # 0.9mcg = 36IU https://www.omnicalculator.com/health/mcg-to-iu-converter
egg_yolk.calcium = 22
egg_yolk.iron = 0.5
egg_yolk.potassium = 19

vanilla_extract = ingredient('vanilla extract')
vanilla_extract.servings = 1/4 # 1/4 tsp
vanilla_extract.nutrition_url = 'https://www.nutritionvalue.org/Vanilla_extract_nutritional_value.html'
vanilla_extract.calories = 12
vanilla_extract.fat = 0
vanilla_extract.sodium = 0
vanilla_extract.carbohydrate = 0.5
vanilla_extract.fiber = 0
vanilla_extract.sugar = 0.5
vanilla_extract.protein = 0
vanilla_extract.vitamin_d = 0
vanilla_extract.calcium = 0.5
vanilla_extract.iron = 0
vanilla_extract.potassium = 6.2

lemon_juice = ingredient('lemon juice') #serving size is 1 cup
lemon_juice.servings = 1/48 # 1 tsp = 1/48 cup
lemon_juice.nutrition_url = 'https://www.nutritionvalue.org/Lemon_juice%2C_raw_nutritional_value.html'
lemon_juice.calories = 54
lemon_juice.fat = 0.6
lemon_juice.saturated_fat = 0.1
lemon_juice.sodium = 2.4
lemon_juice.carbohydrate = 17
lemon_juice.fiber = 0.7
lemon_juice.sugar = 6.2
lemon_juice.protein = 0.9
lemon_juice.vitamin_d = 0
lemon_juice.calcium = 15
lemon_juice.iron = 0.2
lemon_juice.potassium = 251

swerve_sugar = ingredient('swerve sugar') #serving size is 2 tsp
swerve_sugar.servings = 6 # 2 tbsp = 6 tsp
swerve_sugar.product_url = 'https://www.dillons.com/p/swerve-granular-zero-calorie-sweetener/0085270030017'
swerve_sugar.calories = 0
swerve_sugar.fat = 0
swerve_sugar.sodium = 0
swerve_sugar.carbohydrate = 8
swerve_sugar.sugar_alcohols = 8
swerve_sugar.protein = 0

oatmeal.add_ingredient(eggs)
oatmeal.add_ingredient(swerve_brown_sugar)
oatmeal.add_ingredient(cinnamon)
oatmeal.add_ingredient(nutmeg)
oatmeal.add_ingredient(baking_powder)
oatmeal.add_ingredient(salt)
oatmeal.add_ingredient(carbmaster_skim_milk)
oatmeal.add_ingredient(oats)
oatmeal.add_ingredient(walnuts)
oatmeal.add_ingredient(raisins)
oatmeal.add_ingredient(creamcheese)
oatmeal.add_ingredient(egg_yolk)
oatmeal.add_ingredient(vanilla_extract)
oatmeal.add_ingredient(lemon_juice)
oatmeal.add_ingredient(swerve_sugar)

oatmeal.latex_nutrition_label()