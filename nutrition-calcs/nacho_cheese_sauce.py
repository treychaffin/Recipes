from nutrition_calc import *

sauce = recipe('nacho cheese sauce')
sauce.servings = 8

butter = ingredient('butter')
butter.servings = 3
butter.calories = 102
butter.fat = 12
butter.saturated_fat = 7.2
butter.cholesterol = 31
butter.sodium = 1.6
butter.calcium = 3.4
butter.potassium = 3.4
butter.nutrition_url = 'https://www.nutritionvalue.org/Butter%2C_without_salt_nutritional_value.html?size=1+tbsp+%3D+14.2+g'

cream_cheese = ingredient('cream cheese')
cream_cheese.servings = 2
cream_cheese.calories = 99
cream_cheese.fat = 9.8
cream_cheese.saturated_fat = 5.7
cream_cheese.cholesterol = 29
cream_cheese.sodium = 89
cream_cheese.carbohydrate = 1.6
cream_cheese.sugar = 1.1
cream_cheese.protein = 1.7
cream_cheese.calcium = 28
cream_cheese.potassium = 37
cream_cheese.nutrition_url = 'https://www.nutritionvalue.org/Cheese%2C_cream_nutritional_value.html?size=1+ounce+%3D+28.3495+g'

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

cream = ingredient('heavy cream')
cream.servings = 1
cream.calories = 816
cream.fat = 87
cream.saturated_fat = 55
cream.cholesterol = 271
cream.sodium = 65
cream.carbohydrate = 6.8
cream.sugar = 7
cream.protein = 6.8
cream.vitamin_d = 3.8/0.025
cream.calcium = 158
cream.iron = 0.2
cream.potassium = 228

sauce.add_ingredient(butter)
sauce.add_ingredient(cream_cheese)
sauce.add_ingredient(cheese)
sauce.add_ingredient(cream)

sauce.latex_nutrition_label()