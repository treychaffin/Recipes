class ingredient:
    def __init__(self, name):
        self.name = name

    # nutrition facts per serving (grams)
    calories = 0

    fat = 0
    saturated_fat = 0
    trans_fat = 0
    polyunsaturated_fat = 0
    monounsaturated_fat = 0

    carbohydrate = 0
    sugar = 0
    fiber = 0

    protein = 0

    # sodium (milligrams)
    sodium = 0

    # cholesterol (milligrams)
    cholesterol = 0

    # calcium (milligrams)
    calcium = 0

    # iron (milligrams)
    iron = 0

    # phosphorus (milligrams)
    phosphorus = 0

    # potassium (milligrams)
    potassium = 0

    # riboflavin (milligrams)
    riboflavin = 0

    # vitamin a (# of internation units)
    vitamin_a = 0

    # vitamin c (milligrams)
    vitamin_c = 0

    # vitamin d (# of internation units)
    vitamin_d = 0

    # vitamin e (# of internation units)
    vitamin_e = 0

    # zinc (milligrams)
    zinc = 0

    # product link
    product_url = ''

    # nutitrition link
    nutrition_url = ''

    # servings per recipe
    servings = 0

class recipe:
    ingredients = []

    # servings per recipe
    servings = 0

    def __init__(self, name):
        self.name = name

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
    
    # calories per serving
    def calories(self):
        calories = 0
        for i in range(len(self.ingredients)):
            calories += self.ingredients[i].calories * self.ingredients[i].servings
        return calories / self.servings
    
    # fat per serving
    def fat(self):
        fat = 0
        for i in range(len(self.ingredients)):
            fat += self.ingredients[i].fat * self.ingredients[i].servings
        return fat / self.servings

    # saturated fat per serving
    def saturated_fat(self):
        saturated_fat = 0
        for i in range(len(self.ingredients)):
            saturated_fat += self.ingredients[i].saturated_fat * self.ingredients[i].servings
        return saturated_fat / self.servings

    # trans fat per serving
    def trans_fat(self):
        trans_fat = 0
        for i in range(len(self.ingredients)):
            trans_fat += self.ingredients[i].trans_fat * self.ingredients[i].servings
        return trans_fat / self.servings

    # polyunsaturated fat per serving
    def polyunsaturated_fat(self):
        polyunsaturated_fat = 0
        for i in range(len(self.ingredients)):
            polyunsaturated_fat += self.ingredients[i].polyunsaturated_fat * self.ingredients[i].servings
        return polyunsaturated_fat / self.servings

    # monounsaturated fat per serving
    def monounsaturated_fat(self):
        monounsaturated_fat = 0
        for i in range(len(self.ingredients)):
            monounsaturated_fat += self.ingredients[i].monounsaturated_fat * self.ingredients[i].servings
        return monounsaturated_fat / self.servings

    # carbohydrate per serving
    def carbohydrate(self):
        carbohydrate = 0
        for i in range(len(self.ingredients)):
            carbohydrate += self.ingredients[i].carbohydrate * self.ingredients[i].servings
        return carbohydrate / self.servings

    # sugar per serving
    def sugar(self):
        sugar = 0
        for i in range(len(self.ingredients)):
            sugar += self.ingredients[i].sugar * self.ingredients[i].servings
        return sugar / self.servings

    # fiber per serving
    def fiber(self):
        fiber = 0
        for i in range(len(self.ingredients)):
            fiber += self.ingredients[i].fiber * self.ingredients[i].servings
        return fiber / self.servings

    # protein per serving
    def protein(self):
        protein = 0
        for i in range(len(self.ingredients)):
            protein += self.ingredients[i].protein * self.ingredients[i].servings
        return protein / self.servings

    # sodium per serving
    def sodium(self):
        sodium = 0
        for i in range(len(self.ingredients)):
            sodium += self.ingredients[i].sodium * self.ingredients[i].servings
        return sodium / self.servings

    # cholesterol per serving
    def cholesterol(self):
        cholesterol = 0
        for i in range(len(self.ingredients)):
            cholesterol += self.ingredients[i].cholesterol * self.ingredients[i].servings
        return cholesterol / self.servings

    # calcium per serving
    def calcium(self):
        calcium = 0
        for i in range(len(self.ingredients)):
            calcium += self.ingredients[i].calcium * self.ingredients[i].servings
        return calcium / self.servings

    # iron per serving
    def iron(self):
        iron = 0
        for i in range(len(self.ingredients)):
            iron += self.ingredients[i].iron * self.ingredients[i].servings
        return iron / self.servings

    # phosphorus per serving
    def phosphorus(self):
        phosphorus = 0
        for i in range(len(self.ingredients)):
            phosphorus += self.ingredients[i].phosphorus * self.ingredients[i].servings
        return phosphorus / self.servings

    # potassium per serving
    def potassium(self):
        potassium = 0
        for i in range(len(self.ingredients)):
            potassium += self.ingredients[i].potassium * self.ingredients[i].servings
        return potassium / self.servings

    # riboflavin per serving
    def riboflavin(self):
        riboflavin = 0
        for i in range(len(self.ingredients)):
            riboflavin += self.ingredients[i].riboflavin * self.ingredients[i].servings
        return riboflavin / self.servings

    # vitamin a per serving
    def vitamin_a(self):
        vitamin_a = 0
        for i in range(len(self.ingredients)):
            vitamin_a += self.ingredients[i].vitamin_a * self.ingredients[i].servings
        return vitamin_a / self.servings

    # vitamin c per serving
    def vitamin_c(self):
        vitamin_c = 0
        for i in range(len(self.ingredients)):
            vitamin_c += self.ingredients[i].vitamin_c * self.ingredients[i].servings
        return vitamin_c / self.servings

    # vitamin d per serving
    def vitamin_d(self):
        vitamin_d = 0
        for i in range(len(self.ingredients)):
            vitamin_d += self.ingredients[i].vitamin_d * self.ingredients[i].servings
        return vitamin_d / self.servings

    # vitamin e per serving
    def vitamin_e(self):
        vitamin_e = 0
        for i in range(len(self.ingredients)):
            vitamin_e += self.ingredients[i].vitamin_e * self.ingredients[i].servings
        return vitamin_e / self.servings

    # zinc per serving
    def zinc(self):
        zinc = 0
        for i in range(len(self.ingredients)):
            zinc += self.ingredients[i].zinc * self.ingredients[i].servings
        return zinc / self.servings