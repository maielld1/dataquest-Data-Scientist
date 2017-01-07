## 1. Programming And Data Science ##

england = 135
china = 123
india = 124
united_states = 134

## 2. Display Values Using The Print Function ##

china = 123
india = 124
united_states = 134
print(china)
print(india)
print(united_states)

## 3. Data Types ##

china_name = "China"
china_rounded = 123
china_exact = 122.5
print(china_name, china_rounded, china_exact)

## 4. The Type Function ##

china_name = "China"
china_exact = 122.5
print(type(china_exact))

## 5. Converting Types ##

china_rounded = 123
int_to_str = str(china_rounded)
str_to_int = int(int_to_str)

## 6. Comments ##

#china
china = 123
#india
india = 124
#US
united_states = 134

## 7. Arithmetic Operators ##

china_plus_10 = china + 10
us_times_100 = united_states * 100
print(china_plus_10, us_times_100)

## 8. Order Of Operations ##

china = 123
india = 124
united_states = 134
china_celsius = (china-32)*0.56
india_celsius = (india-32)*0.56
us_celsius = (united_states-32)*0.56

## 10. Using A List To Store Multiple Values ##

countries = []
temperatures = []
countries.append("China")
countries.append("India")
countries.append("United States")
temperatures.append(122.5)
temperatures.append(124.0)
temperatures.append(134.1)
print(countries, temperatures)

## 11. Creating Lists With Values ##

temps = ["China", 122.5, "India", 124.0, "United States", 134.1]

## 12. Accessing Elements In A List ##

countries = []
temperatures = []

countries.append("China")
countries.append("India")
countries.append("United States")

temperatures.append(122.5)
temperatures.append(124.0)
temperatures.append(134.1)

# Add your code here.
china = countries[0]
china_temperature = temperatures[0]

## 13. Retrieving The Length Of A List ##

countries = ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan"]
temperatures = [122.5, 124.0, 134.1, 103.1, 112.5, 128.3]
two_sum = len(countries)+len(temperatures)

## 14. Slicing Lists ##

countries = ["China", "India", "United States", "Indonesia", "Brazil", "Pakistan"]
temperatures = [122.5, 124.0, 134.1, 103.1, 112.5, 128.3]
countries_slice = countries[1:4]
temperatures_slice = temperatures[-3:]