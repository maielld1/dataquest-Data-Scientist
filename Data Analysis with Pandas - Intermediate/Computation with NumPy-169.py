## 2. Array Comparisons ##

countries_canada = world_alcohol[:,2]=="Canada"
years_1984 = world_alcohol[:,0]=="1984"

## 3. Selecting Elements ##

country_is_algeria = world_alcohol[:,2]=="Algeria"
country_algeria = world_alcohol[country_is_algeria, :]

## 4. Comparisons with Multiple Conditions ##

is_algeria_and_1986 = (world_alcohol[:,0]=="1986") & (world_alcohol[:,2]=="Algeria") 
rows_with_algeria_and_1986 = world_alcohol[is_algeria_and_1986,:]

## 5. Replacing Values ##

world_alcohol[world_alcohol[:,0]=="1986", 0]="2014"
world_alcohol[world_alcohol[:,3]=="Wine", 3]="Grog"

## 6. Replacing Empty Strings ##

is_value_empty = world_alcohol[:,4]==''
world_alcohol[is_value_empty, 4] = "0"

## 7. Converting Data Types ##

alcohol_consumption = world_alcohol[:,4].astype(float)

## 8. Computing with NumPy ##

total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()

## 9. Total Annual Alcohol Consumption ##

canada_1986 = world_alcohol[(world_alcohol[:,0]=='1986')&(world_alcohol[:,2]=='Canada')]
canada_1986[canada_1986[:,4]=='']='0'
canada_alcohol = canada_1986[:,4].astype(float)
total_canadian_drinking = canada_alcohol.sum()

## 10. Calculating Consumption for Each Country ##

totals = {}
year = world_alcohol[world_alcohol[:,0]=='1989']
for country in countries:
    country_consumption = year[year[:,2]==country]
    country_consumption[country_consumption[:,4]=='']='0'
    country_consumption = country_consumption[:,4].astype(float)
    totals[country]=country_consumption[:4].sum()

## 11. Finding the Country that Drinks the Most ##

highest_value = 0
highest_key = None
for item in totals:
    if totals[item]>highest_value:
        highest_value=totals[item]
        highest_key=item