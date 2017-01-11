## 1. Introduction ##

import sqlite3
conn = sqlite3.connect("factbook.db")
pop_avg = conn.execute("Select avg(population) from facts").fetchall()[0][0]
pop_growth_avg = conn.execute("Select avg(population_growth) from facts").fetchall()[0][0]
birth_rate_avg = conn.execute("Select avg(birth_rate) from facts").fetchall()[0][0]
death_rate_avg = conn.execute("Select avg(death_rate) from facts").fetchall()[0][0]
conn.close()

## 2. Ranges ##

conn = sqlite3.connect("factbook.db")

averages = "select avg(population), avg(population_growth), avg(birth_rate), avg(death_rate), avg(migration_rate) from facts;"
avg_results = conn.execute(averages).fetchall()
pop_avg = avg_results[0][0]
pop_growth_avg = avg_results[0][1]
birth_rate_avg = avg_results[0][2]
death_rate_avg = avg_results[0][3]
mig_rate_avg = avg_results[0][4]

mins = "select min(population), min(population_growth), min(birth_rate), min(death_rate), min(migration_rate) from facts;"
min_results = conn.execute(mins).fetchall()
pop_min = min_results[0][0]
pop_growth_min = min_results[0][1]
birth_rate_min = min_results[0][2]
death_rate_min = min_results[0][3]
mig_rate_min = min_results[0][4]

maxs = "select max(population), max(population_growth), max(birth_rate), max(death_rate), max(migration_rate) from facts;"
max_results = conn.execute(maxs).fetchall()
pop_max = max_results[0][0]
pop_growth_max = max_results[0][1]
birth_rate_max = max_results[0][2]
death_rate_max = max_results[0][3]
mig_rate_max = max_results[0][4]

## 3. Filtering ##

conn = sqlite3.connect("factbook.db")
mins = "select min(population), min(population_growth), min(birth_rate), min(death_rate), min(migration_rate) from facts where population < 2000000000 and population > 0;"
min_results = conn.execute(mins).fetchall()
pop_min = min_results[0][0]
pop_growth_min = min_results[0][1]
birth_rate_min = min_results[0][2]
death_rate_min = min_results[0][3]
mig_rate_min = min_results[0][4]

maxs = "select max(population), max(population_growth), max(birth_rate), max(death_rate), max(migration_rate) from facts where population < 2000000000 and population > 0;"
max_results = conn.execute(maxs).fetchall()
pop_max = max_results[0][0]
pop_growth_max = max_results[0][1]
birth_rate_max = max_results[0][2]
death_rate_max = max_results[0][3]
mig_rate_max = max_results[0][4]

## 4. Predicting future population growth ##

import sqlite3
conn = sqlite3.connect("factbook.db")
projected_population_query = '''
select round(population + population * (population_growth/100), 0) from facts
where population > 0 and population < 7000000000 
and population is not null and population_growth is not null;
'''

projected_population = conn.execute(projected_population_query).fetchall()

print(projected_population[0:10])

## 5. Exploring projected population ##

import sqlite3
conn = sqlite3.connect("factbook.db")

proj_pop_query = '''
select round(min(population + population * (population_growth/100)), 0), 
round(max(population + population * (population_growth/100)), 0), 
round(avg(population + population * (population_growth/100)), 0)
from facts 
where population > 0 and population < 7000000000 and 
population is not null and population_growth is not null;
'''

proj_results = conn.execute(proj_pop_query).fetchall()

pop_proj_min = proj_results[0][0]
pop_proj_max = proj_results[0][1]
pop_proj_avg = proj_results[0][2]

print("Projected Population,", "Minimum: ", pop_proj_min)
print("Projected Population,", "Maximum: ", pop_proj_max)
print("Projected Population,", "Average: ", pop_proj_avg)