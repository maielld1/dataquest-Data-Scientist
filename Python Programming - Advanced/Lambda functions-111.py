## 1. String Manipulation ##

hello = "hello world"[0:5]
foo = "some string"
password = "password"

print(foo[5:11])

# Your code goes here
fifth = password[4]
last_four = password[-4:]

## 2. Omitting starting or ending indices ##

hello = "hello world"[:5]
foo = "some string"
print(foo[5:])

my_string = "string slicing is fun!"
# Your code goes here
first_nine = my_string[:9]
remainder = my_string[9:]

## 3. Slicing with a step ##

hlo = "hello world"[:5:2]

my_string = "string slicing is fun!"
# Your code goes here
gibberish = my_string[::2]
worse_gibberish = my_string[7::3]

## 4. Negative Indexing ##

olleh = "hello world"[4::-1]
able_string = "able was I ere I saw elba"

# Your code goes here
def is_palindrome(my_string):
    return my_string == my_string[-1::-1]
    
phrase_palindrome = is_palindrome(able_string)

## 6. Checking for Substrings ##

theres_no = "I" in "team"

# Your code goes here
def easy_patterns(string):
    count=0
    for x in passwords:
        if string in x:
            count+=1
    return count

countup_passwords = easy_patterns("1234")

## 7. First-Class Functions ##

ints = list(map(int, [1.5, 2.4, 199.7, 56.0]))
print(ints)

# Your code goes here
floats = list(map(float, not_floats))

## 8. Average Password Length ##

# Your code goes here
password_lengths = list(map(len, passwords))
avg_password_length = sum(password_lengths)/len(passwords)

## 9. More Uses For First-Class Functions ##

def is_palindrome(my_string):
    return my_string == my_string[::-1]

# Your code goes here
palindrome_passwords = list(filter(is_palindrome, passwords))

## 10. Lambda Functions ##

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x : x % 2 == 0, numbers))
print(evens)

# Your code goes here
palindrome_passwords = list(filter(lambda x: x==x[-1::-1], passwords))

## 11. Password Strengths ##

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x : x % 2 == 0, numbers))
print(evens)

# Your code goes here
weak_passwords = list(filter(lambda x: len(x)<6, passwords))
medium_passwords = list(filter(lambda x: len(x)>=6 and len(x)<=10, passwords))
strong_passwords = list(filter(lambda x: len(x)>10, passwords))