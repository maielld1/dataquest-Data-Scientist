## 2. Holdout validation ##

import numpy as np
np.random.seed(8)
admissions = pd.read_csv("admissions.csv")
admissions["actual_label"] = admissions["admit"]
admissions = admissions.drop("admit", axis=1)
shuffled_index = np.random.permutation(admissions.index)
shuffled_admissions = admissions.loc[shuffled_index]

train = shuffled_admissions.iloc[0:515]
test = shuffled_admissions.iloc[515:len(shuffled_admissions)]

print(shuffled_admissions.head())

## 3. Accuracy ##

import numpy as np
from sklearn.linear_model import LogisticRegression
np.random.seed(8)

shuffled_index = np.random.permutation(admissions.index)
shuffled_admissions = admissions.loc[shuffled_index]
train = shuffled_admissions.iloc[0:515]
test = shuffled_admissions.iloc[515:len(shuffled_admissions)]
model = LogisticRegression()
model.fit(train[["gpa"]], train["actual_label"])
test['predicted_label'] = model.predict(test[["gpa"]])
match = test['predicted_label']==test['actual_label']
accuracy=len(test[match==True])/len(test['actual_label'])

## 4. Sensitivity and specificity ##

model = LogisticRegression()
model.fit(train[["gpa"]], train["actual_label"])
labels = model.predict(test[["gpa"]])
test["predicted_label"] = labels
matches = test["predicted_label"] == test["actual_label"]
correct_predictions = test[matches]
accuracy = len(correct_predictions) / len(test)

true_positive_filter = (test["predicted_label"] == 1) & (test["actual_label"] == 1)
true_positives = len(test[true_positive_filter])
false_negative_filter = (test["predicted_label"] == 0) & (test["actual_label"] == 1)
false_negatives = len(test[false_negative_filter])
sensitivity = true_positives/(true_positives + false_negatives)

true_negative_filter = (test["predicted_label"] == 0) & (test["actual_label"] == 0)
true_negatives = len(test[true_negative_filter])
false_positive_filter = (test["predicted_label"] == 1) & (test["actual_label"] == 0)
false_positives = len(test[false_positive_filter])
specificity = true_negatives/(true_negatives + false_positives)

## 6. ROC curve ##

import matplotlib.pyplot as plt
from sklearn import metrics

probabilities = model.predict_proba(test[["gpa"]])
fpr, tpr, thresholds = metrics.roc_curve(test["actual_label"], probabilities[:,1])
plt.plot(fpr, tpr)

## 7. Area under the curve ##

# Note the different import style!
from sklearn.metrics import roc_auc_score

auc_score = metrics.roc_auc_score(test["actual_label"], probabilities[:,1])

print(auc_score)