## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
for i, ship in enumerate(ships):
    print(ship)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
for i, thing in enumerate(things):
    thing.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [price*2 for price in apple_prices]
apple_prices_lowered = [price-100 for price in apple_prices]

## 5. Counting Female Names ##

name_counts = {}
for row in legislators:
    if row[3]=='F' and row[7]>1940:
        name = row[1]
        if name in name_counts:
            name_counts[name] = name_counts[name] + 1
        else:
            name_counts[name] = 1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []
for x in values:
    checks.append(x is not None and x>30)

## 8. Highest Female Name Count ##

max_value = None
for key in name_counts:
    count = name_counts[key]
    if max_value is None or count>max_value:
        max_value = count

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for plant, types in plant_types.items():
    print(plant)
    print(types)

## 10. Finding the Most Common Female Names ##

top_female_names = []
for name, count in name_counts.items():
    if count==2:
        top_female_names.append(name)

## 11. Finding the Most Common Male Names ##

top_male_names = []
male_name_counts = {}
for row in legislators:
    if row[3]=='M' and row[7]>1940:
        name = row[1]
        if name in male_name_counts:
            male_name_counts[name] = male_name_counts[name] + 1
        else:
            male_name_counts[name] = 1

highest_male_count = 0
for name, count in male_name_counts.items():
    if count>highest_male_count:
        highest_male_count=count
        
for name, count in male_name_counts.items():
    if count==highest_male_count:
        top_male_names.append(name)