## 2. Reading in data ##

congress <- read.csv("114_congress.csv")
whiteHouse <- read.csv("2015_white_house.csv")

## 4. Creating a matrix ##

# Create a simple matrix with 3 rows and 2 columns.
B <- matrix(c(1,2,3,4,5,6), 3, 2)
print(B)
C <- matrix(c("Rambo", "Chuck Norris", "Arnold", "Steven Seagal", "John Wayne", "Steve McQueen"), 2, 3)

## 5. Getting a matrix element ##

# Print the first column of the second row.
print(C[2,1])

# Print the third column of the second row.
print(C[2,3])
c22 <- C[2,2]
c13 <- C[1,3]

## 6. Getting rows and columns ##

# The first row of C.
print(C[1,])

# The first column of C.
print(C[,1])

c20 <- C[2,]
c03 <- C[,3]

## 8. Data frame columns ##

# Get the salary column from the whitehouse data
salary <- whiteHouse["Salary"]

# Get the salary of the first employee in our data (salary column of the first row)
firstSalary <- whiteHouse[1,"Salary"]

whiteHouseNames <- whiteHouse['Name']
status5 <-whiteHouse[5, 'Status']

## 9. Finding average salary ##

# Enter your code here.
sum <- sum(whiteHouse['Salary'])
rows <- nrow(whiteHouse)
averageSalary <- sum/rows 

## 10. Finding the highest/lowest salary ##

# Enter your code here.
highestSalary <- max(whiteHouse['Salary'])
lowestSalary <- min(whiteHouse['Salary'])
                     

## 11. Subtle differences ##

# Returns a data frame.
salaryFrame <- whiteHouse["Salary"]

# Returns a vector
salaryVector <- whiteHouse[,"Salary"]

whiteHouseNames <- whiteHouse['Name']
whiteHouseNamesVector <- whiteHouse[,'Name']

## 12. Minimum/maximum index ##

# Find the index of the person with the lowest salary.
# This is where knowing what kind of indexing returns what value comes in handy!  We need a vector.
minimumIndex <- which.min(whiteHouse[,"Salary"])
# Extract the row of the lowest salary.
minimumSalaryRow <- whiteHouse[minimumIndex,]
# Get the name column from that row.
lowestEarner <- minimumSalaryRow["Name"]
# Print the name of the white house employee who earned the least.
print(lowestEarner)

maxIndex <- which.max(whiteHouse[,"Salary"])
# Extract the row of the lowest salary.
maxSalaryRow <- whiteHouse[maxIndex,]
# Get the name column from that row.
highestEarner <- maxSalaryRow["Name"]