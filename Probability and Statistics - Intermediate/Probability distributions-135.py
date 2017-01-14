## 3. Bikesharing distribution ##

import pandas
bikes = pandas.read_csv("bike_rental_day.csv")
prob_over_5000 = bikes[bikes['cnt']>5000].shape[0]/bikes.shape[0]

## 4. Computing the distribution ##

import math

# Each item in this list represents one k, starting from 0 and going up to and including 30.
outcome_counts = list(range(31))
def prob(k, N, p, q):
    a = (p**k)*(q**(N-k))
    b = math.factorial(N)/(math.factorial(k)*math.factorial(N-k))
    return a * b

outcome_probs = []

outcome_probs = [prob(x, 30, 0.39, 0.61) for x in outcome_counts]
    

## 6. Simplifying the computation ##

import scipy
from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,30,31)

outcome_probs = binom.pmf(outcome_counts,30,0.39)

plt.bar(outcome_counts, outcome_probs)
plt.show()

## 8. Computing the mean of a probability distribution ##

dist_mean = 30*0.39

## 9. Computing the standard deviation ##

dist_stdev = (30*0.39*0.61)**0.5

## 10. A different plot ##

# Enter your answer here.
import scipy
from scipy import linspace
from scipy.stats import binom

# Create a range of numbers from 0 to 30, with 31 elements (each number has one entry).
outcome_counts = linspace(0,10,11)

outcome_probs = binom.pmf(outcome_counts,10,0.39)

plt.bar(outcome_counts, outcome_probs)
plt.show()

outcome_counts = linspace(0,100,101)

outcome_probs = binom.pmf(outcome_counts,100,0.39)

plt.bar(outcome_counts, outcome_probs)
plt.show()

## 12. Cumulative density function ##

outcome_counts = linspace(0,30,31)
dist = binom.cdf(outcome_counts,30,0.39)
plt.plot(outcome_counts, dist)
plt.show()

## 14. Faster way to calculate likelihood ##

left_16 = None
right_16 = None
# The sum of all the probabilities to the left of k, including k.
left_16 = binom.cdf(16,30,0.39)

# The sum of all probabilities to the right of k.
right_16 = 1 - left_16