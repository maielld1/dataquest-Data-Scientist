## 3. The Math Module ##

import math
a = math.sqrt(16.0)
b = math.ceil(111.3)
c = math.floor(89.9)

## 4. Variables Within Modules ##

import math
a = math.sqrt(math.pi)
b = math.ceil(math.pi)
c = math.floor(math.pi)
print(math.pi)

## 5. The CSV Module ##

import csv
f = open("nfl.csv")
csvread = csv.reader(f)
nfl = list(csvread)


## 6. Counting How Many Times a Team Won ##

import csv
f = open("nfl.csv")
csvread = csv.reader(f)
nfl = list(csvread)
patriots_wins=0
for x in nfl:
    if x[2] == "New England Patriots":
        patriots_wins=patriots_wins+1
    

## 7. Making a Function that Counts Wins ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.
def nfl_wins(team_name):
    wins=0
    for x in nfl:
        if x[2] == team_name:
            wins=wins+1
    return wins

cowboys_wins = nfl_wins("Dallas Cowboys")
falcons_wins = nfl_wins("Atlanta Falcons")
    

## 10. Working with Boolean Operators ##

a = 5
b = 10
# a == 5
result1 = True

# a < 5 or b > a
result2 = True

# a < 5 and b > a
result3 = False

# a == 5 or b == 5
result4 = True

# a > b or a == 10
result5 = False

## 11. Counting Wins in a Given Year ##

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

def nfl_wins_in_a_year(team, year):
    count = 0
    for row in nfl:
        if row[2] == team and row[0]==year:
            count = count + 1
    return count

browns_2010_wins = nfl_wins_in_a_year("Cleveland Browns", "2010")
eagles_2011_wins = nfl_wins_in_a_year("Philadelphia Eagles", "2011")