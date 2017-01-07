## 2. Introduction to the Data ##

import pandas as pd

all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
all_ages.head(5)
recent_grads.head(5)

## 3. Summarizing Major Categories ##

# Unique values in Major_category column.
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()

def calculate_major_cat_totals(df):
    cats = df['Major_category'].value_counts().index
    counts_dictionary = dict()

    for c in cats:
        major_df = df[df["Major_category"] == c]
        total = major_df["Total"].sum(axis=0)
        counts_dictionary[c] = total
    return counts_dictionary

aa_cat_counts = calculate_major_cat_totals(all_ages)
rg_cat_counts = calculate_major_cat_totals(recent_grads)

## 4. Low-Wage Job Rates ##

low_wage_percent = 0.0
low_wage_percent = (recent_grads['Low_wage_jobs'].sum(axis=0))/(recent_grads['Total'].sum(axis=0))

print(low_wage_percent)

## 5. Comparing Data Sets ##

# All majors, common to both DataFrames
majors = recent_grads['Major'].unique()
rg_lower_count = 0

recent_grads_lower_unemp_count = 0
all_ages_lower_unemp_count = 0
for m in majors:
    recent_grads_row =  recent_grads[recent_grads['Major'] == m]
    all_ages_row = all_ages[all_ages['Major'] == m]
    
    recent_grads_unemp_rate = recent_grads_row['Unemployment_rate'].values[0]
    all_ages_unemp_rate = all_ages_row['Unemployment_rate'].values[0]
    
    if recent_grads_unemp_rate < all_ages_unemp_rate:
        rg_lower_count += 1