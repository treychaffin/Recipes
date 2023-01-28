class ingredient:
    def __init__(self, name):
        self.name = name

    # calories
    calories = 0

    # fat (grams)
    fat = 0

    # saturated fat (grams)
    saturated_fat = 0

    # trans fat (grams)
    trans_fat = 0

    # polyunsaturated fat (grams)
    polyunsaturated_fat = 0

    # monounsaturated fat (grams)
    monounsaturated_fat = 0

    # carbohydrate (grams)
    carbohydrate = 0

    # sugar (grams)
    sugar = 0

    # fiber (grams)
    fiber = 0

    # protein (grams)
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

    # print nutrition facts
    def nutrition_facts(self):
        print('    Nutrition Facts: ',self.name)
        print('')
        print('           calories: ',round(self.calories(),2))
        print('                fat: ',round(self.fat(),2))
        print('      saturated fat: ',round(self.saturated_fat(),2))
        print('          trans fat: ',round(self.trans_fat(),2))
        print('polyunsaturated fat: ',round(self.polyunsaturated_fat(),2))
        print('monounsaturated fat: ',round(self.monounsaturated_fat(),2))
        print('        cholesterol: ',round(self.cholesterol(),2))
        print('             sodium: ',round(self.sodium(),2))
        print('       carbohydrate: ',round(self.carbohydrate(),2))
        print('              fiber: ',round(self.fiber(),2))
        print('              sugar: ',round(self.sugar(),2))
        print('            protein: ',round(self.protein(),2))
        print('            calcium: ',round(self.calcium(),2))
        print('               iron: ',round(self.iron(),2))
        print('         phosphorus: ',round(self.phosphorus(),2))
        print('          potassium: ',round(self.potassium(),2))
        print('         riboflavin: ',round(self.riboflavin(),2))
        print('          vitamin a: ',round(self.vitamin_a(),2))
        print('          vitamin c: ',round(self.vitamin_c(),2))
        print('          vitamin d: ',round(self.vitamin_d(),2))
        print('          vitamin e: ',round(self.vitamin_e(),2))
        print('               zinc: ',round(self.zinc(),2))

    def latex_nutrition_label(self):
        print("\\begin{tabular}{|lr|}")
        print('    \hline')
        print('    & \\\\')
        print('    \multicolumn{2}{|l|}{\huge{\\textbf{\\textrm{Nutrition Facts}}}}')
        print('    \\\\ [0.5ex] \hline')
        print('    \multicolumn{2}{|l|}{\\textrm{Serving Size: 1}} \\\\ [0.5ex]') 
        print('    \multicolumn{2}{|l|}{\\textrm{Servings per Recipe: ',self.servings,'}}')
        print('    \\\\ \\noalign{\hrule height 3pt}')
        print('    \multicolumn{2}{|l|}{\\footnotesize{\\textbf{\\textrm{Amount per Serving}}}}')
        print('    \\\\')
        print('    \\textbf{\\textrm{Calories (kcal)}}            & \\textbf{',round(self.calories(),2),'}')
        print('    \\\\ \\noalign{\hrule height 2pt}')
        print('    \\textbf{\\textrm{Fat (g)}}                      & \\textrm{',round(self.fat(),2),'}  \\\\ \hline')
        print('    \hspace{2mm} \\textrm{Saturated Fat (g)}        & \\textrm{',round(self.saturated_fat(),2),'}  \\\\ \hline')
        print('    \hspace{2mm} \\textrm{Trans Fat (g)}            & \\textrm{',round(self.trans_fat(),2),'}      \\\\ \hline')
        print('    \hspace{2mm} \\textrm{Polyunsaturated Fat (g)}  & \\textrm{',round(self.polyunsaturated_fat(),2),'}   \\\\ \hline')
        print('    \hspace{2mm} \\textrm{Monounsaturated Fat (g)}  & \\textrm{',round(self.monounsaturated_fat(),2),'}   \\\\ \hline')
        print('    \\textbf{\\textrm{Cholesterol (mg)}}             & \\textrm{',round(self.cholesterol(),2),'}  \\\\ \hline')
        print('    \\textbf{\\textrm{Sodium (mg)}}                  & \\textrm{',round(self.sodium(),2),'} \\\\ \hline')
        print('    \\textbf{\\textrm{Carbohydrates (g)}}            & \\textrm{',round(self.carbohydrate(),2),'}  \\\\ \hline')
        print('    \hspace{2mm} \\textrm{Sugar (g)}                & \\textrm{',round(self.sugar(),2),'}   \\\\ \hline')
        print('    \hspace{2mm} \\textrm{Fiber (g)}                & \\textrm{',round(self.fiber(),2),'}  \\\\ \hline')
        print('    \\textbf{\\textrm{Protein (g)}}                  & \\textrm{',round(self.protein(),2),'}')
        print('    \\\\ \\noalign{\hrule height 3pt}')
        print('    \\textbf{Calcium} \\textrm{',round(self.calcium(),2),' mg}      &')
        print('    \multicolumn{1}{|l|}{\\textbf{Iron} \\textrm{',round(self.iron(),2),' mg}}            \\\\ \hline')
        print('    \\textbf{Phosphorus} \\textrm{',round(self.phosphorus(),2),' mg}   &')
        print('    \multicolumn{1}{|l|}{\\textbf{Potassium} \\textrm{',round(self.potassium(),2),' mg}}     \\\\ \hline')
        print('    \\textbf{Riboflavin} \\textrm{',round(self.riboflavin(),2),' mg}  &')
        print('    \multicolumn{1}{|l|}{\\textbf{Vitamin A} \\textrm{',round(self.vitamin_a(),2),'IU }}        \\\\ \hline')
        print('    \\textbf{Vitamin C} \\textrm{',round(self.vitamin_c(),2),' mg}      &')
        print('    \multicolumn{1}{|l|}{\\textbf{Vitamin D} \\textrm{',round(self.vitamin_d(),2),' IU}}         \\\\ \hline')
        print('    \\textbf{Vitamin E} \\textrm{',round(self.vitamin_e(),2),' IU}     &')
        print('    \multicolumn{1}{|l|}{\\textbf{Zinc} \\textrm{',round(self.zinc(),2),' mg}}               \\\\ \hline')
        print('\end{tabular}')