"""

3. Extracting Ask HN and Show HN Posts
    To find the posts that begin with either Ask HN or Show HN, 
    we'll use the string method startswith.

"""
"""
# 1) Sample
string1 = 'dataquest'
print(string1.startswith('Data'))
print(string1.startswith('data'))
print('dataquest'.startswith('data'))

"""
"""

# 2) Sample 
    # If we wish to control for case, we can use the lower method

print('DataQuest'.lower())

"""
"""
# 3) Exercise

ask_posts = []
show_posts = []
other_posts = []

for post in hn:
    title = post[1]
    if title.lower().startswith('ask hn'):
        ask_posts.append(post)
    elif title.lower().startswith('show hn'):
        show_posts.append(post)
    else:
        other_posts.append(post)
"""
"""

4. Calculating the Average Number of Comments for Ask HN and Show HN Posts


"""
"""
for post in ask_posts:
    num_comments = post[4]
    total_ask_comments += int(num_comments)
avr_ask_comments = total_ask_comments / len(ask_posts)
print(avr_ask_comments)
"""
"""
# Calculate the amount of ask posts created during each hour of day and the number of comments received.
import datetime as dt

result_list = []

for post in hn:
    result_list.append([post[6], int(post[4])])

comments_by_hour = {}
counts_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

for each_row in result_list:
    date = each_row[0]
    comment = each_row[1]
    time = dt.datetime.strptime(date, date_format).strftime("%H")
    if time not in counts_by_hour:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1
    else:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1

comments_by_hour
"""
"""

6. Calculating the Average Number of Comments for Ask HN Posts by Hour

    
counts_by_hour: contains the number of ask posts created during each hour of the day.
comments_by_hour: contains the corresponding number of comments ask posts 
                  created at each hour received.
Next, we'll use these two dictionaries to calculate the average number of comments 
for posts created during each hour of the day.

"""
"""

# 1) Sample

sample_dict = {
                'apple': 2, 
                'banana': 4, 
                'orange': 6
               }

fruits = []

for fruit in sample_dict:
    fruits.append([fruit, 10*sample_dict[fruit]])
print(fruits)
"""