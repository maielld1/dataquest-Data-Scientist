## 2. Introduction To The Data ##

import pandas as pd
unrate = pd.read_csv("unrate.csv")
unrate['DATE'] = pd.to_datetime(unrate['DATE'])
unrate.head(12)

## 6. Introduction to Matplotlib ##

import matplotlib.pyplot as plt
plt.plot()
plt.show()

## 7. Adding Data ##

x_values = unrate['DATE'][:12]
y_values = unrate['VALUE'][:12]
plt.plot(x_values, y_values)
plt.show()

## 8. Fixing Axis Ticks ##

x_values = unrate['DATE'][:12]
y_values = unrate['VALUE'][:12]
plt.plot(x_values, y_values)
plt.xticks(rotation=90)
plt.show()

## 9. Adding Axis Labels And A Title ##

x_values = unrate['DATE'][:12]
y_values = unrate['VALUE'][:12]
plt.plot(x_values, y_values)
plt.xticks(rotation=90)
plt.xlabel("Month")
plt.ylabel("Unemployment Rate")
plt.title("Monthly Unemployment Trends, 1948")
plt.show()