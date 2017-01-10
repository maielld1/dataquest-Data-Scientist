## 2. Introduction to the data ##

import pandas as pd
reviews = pd.read_csv("fandango_scores.csv")
norm_reviews = reviews[["FILM",
"RT_user_norm",
"Metacritic_user_nom",
"IMDB_norm",
"Fandango_Ratingvalue",
"Fandango_Stars"]]

norm_reviews.head(1)

## 4. Creating Bars ##

import matplotlib.pyplot as plt
from numpy import arange

fig, ax = plt.subplots()
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = norm_reviews.ix[0, num_cols].values
bar_positions = arange(5) + 0.75

ax.bar(bar_positions, bar_heights, 0.5)

plt.show()

## 5. Aligning Axis Ticks And Labels ##

fig, ax = plt.subplots()
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews.ix[0, num_cols].values
bar_positions = arange(5) + 0.75
#tick_positions = range(1,6)
ax.bar(bar_positions, bar_heights, 0.5)
ax.set_xticks(bar_positions+0.25)
ax.set_xticklabels(num_cols, rotation=90)
ax.set_xlabel("Rating Source")
ax.set_ylabel("Average Rating")
ax.set_title("Average User Rating For Avengers: Age of Ultron (2015)")
plt.show()

## 6. Horizontal Bar Plot ##

import matplotlib.pyplot as plt
from numpy import arange

fig, ax = plt.subplots()
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_widths = norm_reviews.ix[0, num_cols].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)
ax.barh(bar_positions, bar_widths, 0.5)
ax.set_yticks(tick_positions)
ax.set_yticklabels(num_cols)
ax.set_ylabel("Rating Source")
ax.set_xlabel("Average Rating")
plt.title("Average User Rating for Avengers: Age of Ultron (2015)")
plt.show()


## 7. Scatter plot ##

fig, ax = plt.subplots()
plt.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
plt.xlabel("Fandango")
plt.ylabel("Rotten Tomatoes")
plt.show()

## 8. Switching axes ##

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
plt.xlabel("Fandango")
plt.ylabel("Rotten Tomatoes")
ax2.scatter(norm_reviews['RT_user_norm'], norm_reviews['Fandango_Ratingvalue'])
plt.ylabel("Fandango")
plt.xlabel("Rotten Tomatoes")
plt.show()

## 9. Benchmarking correlation ##

import matplotlib.pyplot as plt

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)
ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
plt.xlabel("Fandango")
plt.ylabel("Rotten Tomatoes")
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 5)
ax2.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['Metacritic_user_nom'])
plt.xlabel("Fandango")
plt.ylabel("Metacritic")
ax2.set_xlim(0, 5)
ax2.set_ylim(0, 5)
ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['IMDB_norm'])
plt.xlabel("Fandango")
plt.ylabel("IMDB")
ax1.set_xlim(0, 5)
ax1.set_ylim(0, 5)
plt.show()