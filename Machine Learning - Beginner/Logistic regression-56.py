## 2. Introduction to the data ##

import pandas as pd
import matplotlib.pyplot as plt

admissions = pd.read_csv("admissions.csv")
plt.scatter(admissions['gpa'], admissions['admit'])
plt.show()

## 5. Training a logistic regression model ##

from sklearn.linear_model import LogisticRegression
logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])
print(admissions[["gpa"]].shape)
print(admissions["gpa"].shape)

## 6. Plotting probabilities ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])
probabilities = logistic_model.predict_proba(admissions[["gpa"]])
# Probability that the row belongs to label `0`.
probabilities[:,0]
# Probabililty that the row belongs to label `1`.
probabilities[:,1]

plt.scatter(admissions['gpa'], probabilities[:,1])

## 7. Predict labels ##

logistic_model = LogisticRegression()
logistic_model.fit(admissions[["gpa"]], admissions["admit"])

fitted_labels = logistic_model.predict(admissions[["gpa"]])
plt.scatter(admissions["gpa"], fitted_labels)
