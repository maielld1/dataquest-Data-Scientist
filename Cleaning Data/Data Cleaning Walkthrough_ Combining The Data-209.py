## 2. Condensing class size ##

class_size = data['class_size']
class_size = class_size[class_size['GRADE ']=='09-12']
class_size = class_size[class_size['PROGRAM TYPE']=='GEN ED']
class_size.head()

## 3. Computing average class sizes ##

import numpy as np
class_size = class_size.groupby('DBN').agg(np.mean)
class_size.reset_index(inplace=True)
data["class_size"] = class_size
data["class_size"].head()

## 4. Condensing demographics ##

demographics = data['demographics']
demographics = demographics[demographics['schoolyear']==20112012]
data['demographics'] = demographics
data['demographics'].head()

## 5. Condensing graduation ##

graduation = data['graduation']
graduation = graduation[(graduation['Demographic']=='Total Cohort')&(graduation['Cohort']=='2006')]
data['graduation'] = graduation
data['graduation'].head()

## 6. Converting AP test scores ##

ap_2010 = data['ap_2010']
cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
for col in cols:
    ap_2010[col]=pd.to_numeric(ap_2010[col],errors='coerce')
    
ap_2010.head()

## 8. Performing the left joins ##

combined = data["sat_results"]
combined = combined.merge(ap_2010,how='left', on='DBN')
combined = combined.merge(graduation,how='left', on='DBN')
combined.shape
combined.head()

## 9. Performing the inner joins ##

survey = data['survey']
hs_directory = data['hs_directory']
combined = combined.merge(class_size,how='inner', on='DBN')
combined = combined.merge(demographics,how='inner', on='DBN')
combined = combined.merge(survey,how='inner', on='DBN')
combined = combined.merge(hs_directory,how='inner', on='DBN')
combined.shape
combined.head()

## 10. Filling in missing values ##

means = combined.mean()
combined = combined.fillna(means)
combined = combined.fillna(0)
combined.head()

## 11. Adding a school district column ##

def two_char(string):
    return string[0:2]

combined['school_dist'] = combined['DBN'].apply(two_char)
combined['school_dist'].head()