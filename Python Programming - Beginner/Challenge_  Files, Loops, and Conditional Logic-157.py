## 3. Read the File Into a String ##

n = open("dq_unisex_names.csv", "r")
names = n.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list=[]
for name in names_list:
    comma_list=name.split(",")
    nested_list.append(comma_list)
print(nested_list)
     

## 6. Convert Numerical Values ##

print(nested_list[0:5])
numerical_list=[]
for x in nested_list:
    name = str(x[0])
    num = float(x[1])
    new_list = [name, num]
    numerical_list.append(new_list)
print(numerical_list[0:5])

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater=[]
for x in numerical_list:
    if x[1]>=1000:
        thousand_or_greater.append(x[0])
print(thousand_or_greater[0:5])