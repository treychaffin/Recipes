# Recipes

A personal collection of recipes written in LaTeX using the LaTeX package cuisine.

Inspired by and used this repository as a template: [https://github.com/m-voit/recipes](https://github.com/m-voit/recipes)

## Recipe collections

Link to PDF compiling all of the recipes:

- [Cooking](./recipes-pdf/cooking.pdf)

## Nutrition Calculator

In the folder "nutrition-calcs", python scripts are used to calculate nutrition
facts and generate LaTex nutrition tables

### Calculating Nutrition Facts

To calculate nutrition facts for a given recipe, create a new file in the 
nutrition-calcs folder, naming it after the recipe with a .py extension.

Start by importing the nutrition_calc.py file to have access to the 
ingredient and recipe class

`from nutrition_calc import *`

#### Create Recipe Object

Start by creating a recipe object. Define the name of recipe when calling the 
recipe class.

`breakfast_burritos = recipe('breakfast burritos')`

Define the number of servings

`breakfast_burritos.servings = 8`

#### Define Ingredients

Define an ingredient by creating a ingredient object. Define the name of the 
ingredient when calling the ingredient class

`eggs = ingredient('eggs')`

Define the number of servings of the given ingredient used in the recipe

`eggs.servings = 12`

Define the nutrition facts per serving of the ingredient. All nutrients default to
zero, so it isn't necessary to explicity define the nutrients if the quantity per
serving is zero. 

Available nutrients to define and their units:

- `calories` (kcal)
- `fat` (grams)
- `saturated_fat` (grams)
- `trans_fat` (grams)
- `polyunsaturated_fat` (grams)
- `monounsaturated_fat` (grams)
- `carbohydrate` (grams)
- `sugar` (grams)
- `fiber` (grams)
- `protein` (grams)
- `sodium` (milligrams)
- `cholesterol` (milligrams)
- `calcium` (milligrams)
- `iron` (milligrams)
- `phosphorus` (milligrams)
- `potassium` (milligrams)
- `riboflavin` (milligrams)
- `vitamin_a` (International Units)
- `vitamin_c` (milligrams)
- `vitamin_d` (International Units)
- `vitamin_e` (International Units)
- `zinc` (milligrams)

Example:

```
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
```

Product URLs and Nutrition URLs can be added for documentation purpose, although
they are not neccesary to calculate the nutrition facts.

Example:

```
russet_potato.product_url = 'https://www.dillons.com/p/russet-potato/0000000004072'
russet_potato.nutrition_url = 'https://www.nutritionix.com/food/russet-potato'
```

#### Add ingredient to the recipe

Add the ingredients to the recipe object by utilizing the `add_ingredient` 
function within the recipe class.

Example:

```
breakfast_burritos.add_ingredient(avocado_oil)
breakfast_burritos.add_ingredient(russet_potato)
breakfast_burritos.add_ingredient(eggs)
breakfast_burritos.add_ingredient(green_chiles)
breakfast_burritos.add_ingredient(sausage)
breakfast_burritos.add_ingredient(tortilla)
breakfast_burritos.add_ingredient(cheese)
breakfast_burritos.add_ingredient(salt)
breakfast_burritos.add_ingredient(pepper)
```

#### Print the nutrition facts

To view nutrition facts of the recipe, use the `nutrition_facts()` function from 
within the recipe class. 

Example:

`breakfast_burritos.nutrition_facts()`

Output:
```
    Nutrition Facts:  breakfast burritos

           calories:  450.17
                fat:  30.12
      saturated fat:  10.82
          trans fat:  0.0
polyunsaturated fat:  2.26
monounsaturated fat:  6.75
        cholesterol:  317.5
             sodium:  1252.85
       carbohydrate:  37.98
              fiber:  23.57
              sugar:  0.57
            protein:  26.92
            calcium:  341.43
               iron:  2.65
         phosphorus:  150.0
          potassium:  281.27
         riboflavin:  0.39
          vitamin a:  450.0
          vitamin c:  0.0
          vitamin d:  60.0
          vitamin e:  12.0
               zinc:  0.0
```

#### Generate LaTex Nutrition Label

To generate a nutrition label table to be used within a LaTex document, use the 
`latex_nutrition_label()` function from within the recipe class.

Example:

`breakfast_burritos.latex_nutrition_label()`

Output:

```
\begin{tabular}{|lr|}
    \hline
    & \\
    \multicolumn{2}{|l|}{\huge{\textbf{\textrm{Nutrition Facts}}}}
    \\ [0.5ex] \hline
    \multicolumn{2}{|l|}{\textrm{Serving Size: 1}} \\ [0.5ex]
    \multicolumn{2}{|l|}{\textrm{Servings per Recipe:  8 }}
    \\ \noalign{\hrule height 3pt}
    \multicolumn{2}{|l|}{\footnotesize{\textbf{\textrm{Amount per Serving}}}}
    \\
    \textbf{\textrm{Calories (kcal)}}            & \textbf{ 450.17 }
    \\ \noalign{\hrule height 2pt}
    \textbf{\textrm{Fat (g)}}                      & \textrm{ 30.12 }  \\ \hline
    \hspace{2mm} \textrm{Saturated Fat (g)}        & \textrm{ 10.82 }  \\ \hline
    \hspace{2mm} \textrm{Trans Fat (g)}            & \textrm{ 0.0 }      \\ \hline
    \hspace{2mm} \textrm{Polyunsaturated Fat (g)}  & \textrm{ 2.26 }   \\ \hline
    \hspace{2mm} \textrm{Monounsaturated Fat (g)}  & \textrm{ 6.75 }   \\ \hline
    \textbf{\textrm{Cholesterol (mg)}}             & \textrm{ 317.5 }  \\ \hline
    \textbf{\textrm{Sodium (mg)}}                  & \textrm{ 1252.85 } \\ \hline
    \textbf{\textrm{Carbohydrates (g)}}            & \textrm{ 37.98 }  \\ \hline
    \hspace{2mm} \textrm{Sugar (g)}                & \textrm{ 0.57 }   \\ \hline
    \hspace{2mm} \textrm{Fiber (g)}                & \textrm{ 23.57 }  \\ \hline
    \textbf{\textrm{Protein (g)}}                  & \textrm{ 26.92 }
    \\ \noalign{\hrule height 3pt}
    \textbf{Calcium} \textrm{ 341.43  mg}      &
    \multicolumn{1}{|l|}{\textbf{Iron} \textrm{ 2.65  mg}}            \\ \hline
    \textbf{Phosphorus} \textrm{ 150.0  mg}   &
    \multicolumn{1}{|l|}{\textbf{Potassium} \textrm{ 281.27  mg}}     \\ \hline
    \textbf{Riboflavin} \textrm{ 0.39  mg}  &
    \multicolumn{1}{|l|}{\textbf{Vitamin A} \textrm{ 450.0 IU }}        \\ \hline
    \textbf{Vitamin C} \textrm{ 0.0  mg}      &
    \multicolumn{1}{|l|}{\textbf{Vitamin D} \textrm{ 60.0  IU}}         \\ \hline
    \textbf{Vitamin E} \textrm{ 12.0  IU}     &
    \multicolumn{1}{|l|}{\textbf{Zinc} \textrm{ 0.0  mg}}               \\ \hline
\end{tabular}
```

Copy and paste the output to the LaTex document.