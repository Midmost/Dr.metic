# -*- coding: utf-8 -*-
"""Ingredient to Dataset Reference.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/tishagrove/Sephora_Clean_Ingredients/blob/main/Ingredient%20to%20Dataset%20Reference.ipynb
"""

# TODO: Import the required libaries
import pandas as pd

# TODO: Read the required dataset
sephora_data = pd.read_csv("sephora_website_dataset.csv")

# TODO: Preview the data
sephora_data.head()

"""# REMOVE/DROP UNNCESSARY COLUMNS"""

#Remove Unnecessary Columns PT 1
sephora_data = sephora_data.drop(columns=['size','MarketingFlags','MarketingFlags_content','options','details','online_only','exclusive'])

#Remove Unnecessary Columns PT 2
sephora_data = sephora_data.drop(columns=['URL','value_price','limited_edition','limited_time_offer'])

sephora_data.head()

"""# SPLIT INGREDIENTS

## It's only running the "-" split, how do we capture : and - maybe explore regex
"""

ingredient_split = sephora_data['ingredients'].str.split(':', expand=True)

ingredient_split.head()

ingredient_split_2 = ingredient_split[1].str.split('-', expand=True)

ingredient_split_2.head()

"""# CLEAN UP INGREDIENT LIST DF"""

#Instead of dropping >500 columns, reselect columns to be kept for ingredient DF
ingredient_list = ingredient_split[[1,2,3,4,5,6,7]]

ingredient_list.head()

#Rename Ingredient List
ingredient_list.rename(columns={1: "Ingredient 1", 2: "Ingredient 2",3: "Ingredient 3", 4: "Ingredient 4",5: "Ingredient 5", 6: "Ingredient 6",7: "Ingredient 7"})

