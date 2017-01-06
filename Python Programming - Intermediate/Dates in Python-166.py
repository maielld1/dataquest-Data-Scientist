## 1. The Time Module ##

import time

current_time = time.time()
print(current_time)

## 2. Converting Timestamps ##

import time
current_time = time.time()
current_struct_time = time.gmtime()
current_hour = current_struct_time.tm_hour
print(current_hour)

## 3. UTC ##

import datetime
current_datetime = datetime.datetime.now()
current_year = current_datetime.year
current_month = current_datetime.month

## 4. Timedelta ##

import datetime

today = datetime.datetime.now()
diff = datetime.timedelta(days = 1)
tomorrow = today + diff
yesterday = today - diff

## 5. Formatting Dates ##

import datetime

mystery_date_formatted_string = mystery_date.strftime('%I:%M%p on %A %B %d, %Y')
print(mystery_date_formatted_string)

## 6. Parsing Dates ##

import datetime

mystery_date = datetime.datetime.strptime(mystery_date_formatted_string, '%I:%M%p on %A %B %d, %Y')

## 8. Reformatting Our Data ##

import datetime

for row in posts:
    row[2] = datetime.datetime.fromtimestamp(float(row[2]))

## 9. Counting Posts from March ##

march_count = 0

for row in posts:
    if row[2].month == 3:
        march_count += 1

## 10. Counting Posts from Any Month ##

march_count = 0

for row in posts:
    if row[2].month == 3:
        march_count += 1
        
def count_posts_in_month(m):
    count = 0
    for row in posts:
        if row[2].month == m:
            count += 1
    return count
feb_count = count_posts_in_month(2)
aug_count = count_posts_in_month(8)