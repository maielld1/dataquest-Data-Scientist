## 2. Calling functions ##

# Define the add function.
add <- function(a, b){
    return(a + b)
}

# Call the add function with the arguments 1 and 2.
print(add(1, 2))

d <- add(5,10)

## 3. Defining a function ##

# Enter your code here.
subtract <- function(a, b){
    return(a - b)
}

d <- subtract(50,10)

## 4. Reading in the data ##

# Enter your code here.
ufos <- read.csv("ufo_sightings.csv")

## 5. Exploring the data frame ##

# Print the first 5 rows in the data frame.
print(head(ufos, 5))

print(tail(ufos, 5))

## 6. UFO sighting years ##

# Enter your code here.
print(str(ufos))

## 7. Converting types ##

dateReported <- as.character(ufos$date.reported)

dateSighted <- as.character(ufos$date.sighted)

## 8. Substring function ##

# This extracts "2004" from our string.
date <- "20040415"
print(substr(date, 1, 4))

# This extracts the year from each string in the vector.
dates <- c("20040415", "20080515")
print(substr(dates, 1, 4))

years <- substr(dateSighted,1,4)

## 9. Making a table ##

# Create a small vector with a few years
selectedYears <- c("2004", "2002", "1992", "2005", "2006", "2005", "2004")

# Create and print a table
print(table(selectedYears))

print(table(years))

## 10. Working with dates ##

dateSighted <- as.character(ufos$date.sighted)
dateSighted <- as.Date(dateSighted, "%Y%m%d")

dateReported <- as.character(ufos$date.reported)
dateReported <- as.Date(dateReported, "%Y%m%d")

## 11. Subtracting vectors ##

# Enter your code here.

delay <- dateReported - dateSighted

## 12. Making a table of delays ##

# Enter your code here.
print(table(delay))

## 13. Cleaning up the data ##

# Enter your code here.
dates <- data.frame(dateReported, dateSighted)

## 14. Booleans ##

a <- c(1,2,3)
b <- c(5,2,5)

# Find when each element in a is greater than the corresponding element in b.
print(a > b)

positiveDelays <- delay>0

## 15. Filtering with booleans ##

filter <- c(FALSE, FALSE, TRUE, TRUE)
bestIceCreamFlavors <- data.frame(c("Peanut Butter Oreo", "Cookie Dough", "Mint Chocolate Chip", "Peanut Butter Cup"))
twoFlavors <- bestIceCreamFlavors[filter,]
print(twoFlavors)

positiveDates <- dates[positiveDelays,]

## 16. Null values ##

# Enter your code here.
cleanDates <-na.omit(positiveDates)

## 17. Remaking our table ##

# Enter your code here
delay <- cleanDates$dateReported - cleanDates$dateSighted
print(table(delay))