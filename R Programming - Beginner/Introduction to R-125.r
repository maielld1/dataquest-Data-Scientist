## 3. Assignment ##

# This is a comment, and so is any line that starts with a #
# Comments help provide information about the code.

# Assign the value 10 to the variable bearAwesomeness.
bearAwesomeness <- 10

# Assign the value 1.5 to the variable guineaPigAwesomeness.
guineaPigAwesomeness <- 1.5

dogAwesomeness <- 10
catAwesomeness <- 9.5

## 4. Print ##

# We can print out values
print(10)

# We can also assign a value to a variable, then print the variable
lifeSavings <- 9999
print(lifeSavings)

## 5. Types of variables ##

# Assign the value 800 to the variable runDistance.
runDistance <- 800

# This is of type "numeric".
print(class(runDistance))

# Assign the value "Peanut Butter Cup" to favoriteDessert
favoriteDessert <- "Peanut Butter Cup"

# This is of type "character", because it contains text.
print(class(favoriteDessert))

biggestDog <- "Mastiff"
mastiffCount <- 50
biggestDogType <- class(biggestDog)
mastiffCountType <- class(mastiffCount)

## 6. Vectors ##

# Store a vector of Russian presidents.
russianPresidents <- c("Mikhail Gorbachev", "Boris Yeltsin", "Vladimir Putin")

# Store a vector of stock prices on consecutive days.
applePrices <- c(113, 114, 115)

fibonacci <- c(0, 1, 1, 2)

## 8. Indexing vectors ##

# Print the first element in salaries.
print(salaries[1])

# Print the 50th element in salaries
print(salaries[50])

salary10 <- salaries[10]

## 9. Vector length ##

# Initialize the runDistances vector
runDistances <- c(20, 10.5, 30)

# Print the length of the vector.
print(length(runDistances))

# The salaries variable has been loaded in.
salariesLength <- length(salaries)

## 10. Vector math ##

# Create a vector of stock prices.
stockPrices <- c(10, 9, 11, 15)

# This results in a new vector.  See how every element has had 2 added to it.
# Every time you do math on a vector, it will change all the elements of the vector.
print(stockPrices + 2)

# But stockPrices is unaffected.
print(stockPrices)

lowerSalaries <- salaries/3

## 11. Overwriting variables ##

# Initialize our list of stock prices again.
stockPrices <- c(10, 9, 11, 15)

# Multiply every stock price by two, and overwrite the variable.
stockPrices <- stockPrices * 2
print(stockPrices)

salaries <- salaries - 5000

## 13. Getting help ##

# Enter your code here.
help(class)