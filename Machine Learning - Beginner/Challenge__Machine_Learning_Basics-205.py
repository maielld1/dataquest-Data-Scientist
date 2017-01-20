## 2. Data cleaning ##

import pandas as pd
columns = ["mpg", "cylinders", "displacement", "horsepower", "weight", "acceleration", "model year", "origin", "car name"]
cars = pd.read_table("auto-mpg.data", delim_whitespace=True, names=columns)
filtered_cars = cars[cars['horsepower']!='?']
filtered_cars['horsepower'] = filtered_cars['horsepower'].astype(float)

## 3. Data Exploration ##

import matplotlib.pyplot as plt
#fig = plt.figure()
filtered_cars.plot('horsepower', 'mpg', kind='scatter')
filtered_cars.plot('weight', 'mpg', kind='scatter')
plt.show()

## 4. Fitting a model ##

import sklearn
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(filtered_cars[["horsepower"]], filtered_cars["mpg"])
predictions = lr.predict(filtered_cars[["horsepower"]])
print(predictions[:5])
print(filtered_cars['mpg'][:5])

## 5. Plotting the predictions ##


plt.scatter(filtered_cars['horsepower'],predictions, c='b')
plt.scatter(filtered_cars['horsepower'],filtered_cars['mpg'], c='r')

## 6. Error metrics ##

from sklearn.metrics import mean_squared_error
lr = LinearRegression()
lr.fit(filtered_cars[["horsepower"]], filtered_cars["mpg"])
predictions = lr.predict(filtered_cars[["horsepower"]])
mse = mean_squared_error(filtered_cars["mpg"], predictions)
rmse = mse**0.5
print(mse, rmse)