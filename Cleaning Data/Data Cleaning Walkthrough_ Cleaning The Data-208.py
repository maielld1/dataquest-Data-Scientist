## 4. Reading in the data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}
for f in data_files:
    d = pd.read_csv("schools/{0}".format(f))
    key_name = f.replace(".csv", "")
    data[key_name] = d

## 5. Exploring the SAT data ##

data["sat_results"].head(5)

## 6. Exploring the other data ##

for k,v in data.items():
    print("\n" + k + "\n")
    print(v.head(5))

## 7. Reading in the survey data ##

all_survey = pd.read_csv("schools/survey_all.txt", delimiter="\t", encoding="windows-1252")
d75_survey = pd.read_csv("schools/survey_d75.txt", delimiter="\t", encoding="windows-1252")

survey = pd.concat([all_survey, d75_survey], axis=0)
survey.head(3)

## 8. Cleaning up the surveys ##

# Changing case of dbn to make it easier to merge
survey["DBN"] = survey["dbn"]

# Required columns
columns = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", "N_p", "saf_p_11", "com_p_11", "eng_p_11", "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", "aca_s_11", "saf_tot_11", "com_tot_11", "eng_tot_11", "aca_tot_11"]

survey= survey.loc[:,columns]
data["survey"] = survey


## 9. Inserting DBN fields ##

data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]

def padded_csd(num):
    string_num = str(num)
    if len(string_num) > 1:
        return string_num
    else:
        return "0" + string_num
    
data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(padded_csd)
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]

data["class_size"].head(3)

## 10. Combining the SAT scores ##

# Using pandas.to_numeric to convert values to numeric 
courses = ["SAT Math Avg. Score", "SAT Critical Reading Avg. Score", "SAT Writing Avg. Score"]

for c in courses:
    data["sat_results"][c] = pd.to_numeric(data["sat_results"][c], errors="coerce")

data["sat_results"]["sat_score"] = data["sat_results"][courses[0]] + data["sat_results"][courses[1]] + data["sat_results"][courses[2]]

data["sat_results"]["sat_score"].head(3)

## 11. Parsing coordinates for each school ##

import re

def get_latitude(address):
    lat_long =  re.findall("\(.+, .+\)", address)
    return lat_long[0].split(", ")[0].replace("(", "")
    
data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(get_latitude)

def get_longitude(address):
    lat_long =  re.findall("\(.+, .+\)", address)
    return lat_long[0].split(",")[1].replace(")", "").strip()
    
data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(get_longitude)

data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"], errors="coerce")
data["hs_directory"]["lon"] = pd.to_numeric(data["hs_directory"]["lon"], errors="coerce")

data["hs_directory"].head(3)

## 12. Extracting the longitude ##

import re

data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(get_longitude)

data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"], errors="coerce")
data["hs_directory"]["lon"] = pd.to_numeric(data["hs_directory"]["lon"], errors="coerce")

data["hs_directory"].head(3)