## 4. Filter out the bad years ##

import matplotlib.pyplot as plt
true_avengers = pd.DataFrame(avengers[avengers['Year']>1960])

avengers['Year'].hist()

## 5. Consolidating deaths ##

deaths = ['Death1', 'Death2', 'Death3', 'Death4', 'Death5']
def count_deaths(row):
  count = 0
  for death in deaths:
    if row[death] == 'YES':
      count += 1;
  return(count)
true_avengers['Deaths'] = true_avengers.apply(lambda row: count_deaths(row), axis=1)
true_avengers.head()

## 6. Years since joining ##

joined_accuracy_count  = int()
correct_joined_years = true_avengers[true_avengers['Years since joining'] == (2015 - true_avengers['Year'])]
joined_accuracy_count = len(correct_joined_years)
joined_accuracy_count