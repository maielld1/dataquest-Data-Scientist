## 1. Introduction ##

import matplotlib.pyplot as plt
import pandas as pd
movie_reviews = pd.read_csv("fandango_score_comparison.csv")
fig = plt.figure(figsize=(5, 12))
els = ['RT_user_norm',
       'Metacritic_user_nom',
       'Fandango_Ratingvalue',
       'IMDB_norm']

for i, el in enumerate(els):
    fig.add_subplot(4, 1, i+1)
    ax = movie_reviews[el].plot(kind='hist')
    ax.set_xlim([0, 5])
    ax.set_ylabel('')
    ax.grid()

plt.show()

## 2. Mean ##

import numpy as np

user_reviews = movie_reviews[['RT_user_norm', 'Metacritic_user_nom', 'Fandango_Ratingvalue', 'IMDB_norm']]
user_reviews_means = user_reviews.apply(lambda x: x.mean())

rt_mean = user_reviews_means['RT_user_norm']
mc_mean = user_reviews_means["Metacritic_user_nom"]
fg_mean = user_reviews_means["Fandango_Ratingvalue"]
id_mean = user_reviews_means["IMDB_norm"]

print("Rotten Tomatoes (mean):", rt_mean)
print("Metacritic (mean):", mc_mean)
print("Fandango (mean):",fg_mean)
print("IMDB (mean):",id_mean)


        

## 3. Variance and standard deviation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(df):
    return sum((df - df.mean()) ** 2) / len(df)

user_reviews_variance = user_reviews.apply(calc_variance)
user_reviews_std_deviation = user_reviews_variance.apply(np.sqrt)

rt_var = user_reviews_variance['RT_user_norm']
rt_stdev = user_reviews_std_deviation['RT_user_norm']

mc_var = user_reviews_variance['Metacritic_user_nom']
mc_stdev = user_reviews_std_deviation['Metacritic_user_nom']

fg_var = user_reviews_variance['Fandango_Ratingvalue']
fg_stdev = user_reviews_std_deviation['Fandango_Ratingvalue']

id_var = user_reviews_variance['IMDB_norm']
id_stdev = user_reviews_std_deviation['IMDB_norm']

print(rt_var, rt_stdev)
print(mc_var, mc_stdev)
print(fg_var, fg_stdev)
print(id_var, id_stdev)

## 4. Scatter plots ##


fig = plt.figure(figsize=(4,8))
ax1 = fig.add_subplot(3,1,1)
ax2 = fig.add_subplot(3,1,2)
ax3 = fig.add_subplot(3,1,3)

ax1.set_xlim(0,5.0)
ax2.set_xlim(0,5.0)
ax3.set_xlim(0,5.0)

ax1.scatter(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
ax2.scatter(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
ax3.scatter(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])
plt.show()

## 5. Covariance ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_covariance(series1, series2):
    x_diffs = series1 - series1.mean()
    y_diffs = series2 - series2.mean()
    return sum(x_diffs * y_diffs) / len(x_diffs)

rt_fg_covar = calc_covariance(movie_reviews['RT_user_norm'], movie_reviews['Fandango_Ratingvalue'])

mc_fg_covar = calc_covariance(movie_reviews['Metacritic_user_nom'], movie_reviews['Fandango_Ratingvalue'])

id_fg_covar = calc_covariance(movie_reviews['IMDB_norm'], movie_reviews['Fandango_Ratingvalue'])

print("Covariance between Rotten Tomatoes and Fandango:", rt_fg_covar)
print("Covariance between Metacritic and Fandango", mc_fg_covar)
print("Covariance between IMDB and Fandango", id_fg_covar)

## 6. Correlation ##

def calc_mean(series):
    vals = series.values
    mean = sum(vals) / len(vals)
    return mean

def calc_variance(series):
    mean = calc_mean(series)
    squared_deviations = (series - mean)**2
    mean_squared_deviations = calc_mean(squared_deviations)
    return mean_squared_deviations

def calc_covariance(series_one, series_two):
    x = series_one.values
    y = series_two.values
    x_mean = calc_mean(series_one)
    y_mean = calc_mean(series_two)
    x_diffs = [i - x_mean for i in x]
    y_diffs = [i - y_mean for i in y]
    codeviates = [x_diffs[i] * y_diffs[i] for i in range(len(x))]
    return sum(codeviates) / len(codeviates)

def calc_correlation(series1, series2):
    variance1 = np.sqrt(calc_variance(series1))
    variance2 = np.sqrt(calc_variance(series2))
    return calc_covariance(series1, series2)/(variance1 * variance2)

rt_fg_corr = calc_correlation(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_corr = calc_correlation(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_corr = calc_correlation(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])

rt_fg_covar = calc_covariance(movie_reviews["RT_user_norm"], movie_reviews["Fandango_Ratingvalue"])
mc_fg_covar = calc_covariance(movie_reviews["Metacritic_user_nom"], movie_reviews["Fandango_Ratingvalue"])
id_fg_covar = calc_covariance(movie_reviews["IMDB_norm"], movie_reviews["Fandango_Ratingvalue"])