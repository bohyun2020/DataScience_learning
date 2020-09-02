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
"""
1. 데이터정리

2. ASK HN / SHOW HN 추출
2-1. num_comments 합계 계산 / num_counts 합계 계산 -> avg 구하기

3. created_at 에서 시간만 추출
3-1. num_comments 합계 계산 / num_counts 합계 계산 -> avg 구하기

"""

# 1) Start

import csv

opened_file = open('hacker_news.csv', encoding='ISO-8859-1')
hn = list(csv.reader(opened_file))
hn = hn[1:]


# 2) Extracting Ask HN and Show HN Posts

ask_posts = []
show_posts = []
other_posts = []


for post in hn:
    title = post[1].lower()
    num_comments = int(post[4])

    if title.startswith('ask hn'):
        ask_posts.append(post)
    elif title.startswith('show hn'):
        show_posts.append(post)
    else:
        other_posts.append(post)


# 3) Calculating the Average Number of Comments for Ask HN and Show HN Posts

total_ask_comments = 0

for post in ask_posts:
    num_comments = int(post[4])
    total_ask_comments += num_comments

avg_ask_comments = total_ask_comments / len(ask_posts)

total_show_posts = 0

for post in show_posts:
    total_show_posts += int(post[4])

avg_show_posts = total_show_posts / len(show_posts)


"""
# On average, ask posts in our sample receive approximately 14 comments, 
# whereas show posts receive approximately 10. Since ask posts are more likely 
# to receive comments. we'll focus our remaining analysis just on these posts.

"""
"""
# 4. Finding the Amount of Ask Posts and Comments by Hour Created
    Calculate the amount of ask posts created during each hour of day 
    and the number of comments received.

"""

result_list = []

import datetime as dt

for post in ask_posts:
    result_list.append(
            [post[6], int(post[4])]
        )

# 2개 변수 적용을 위해서 Dict 사용
comments_by_hour = {}
counts_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

for row in result_list:
    date = row[0]
    comment = row[1]
    time = dt.datetime.strptime(date, date_format).strftime("%H")

    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1


# Calculate the average amount of comments 'Ask HN' posts created at each hour of the day receive.
avg_by_hour = []

for hr in comments_by_hour:
    avg_by_hour.append([hr, comments_by_hour[hr] / counts_by_hour[hr]])


"""

5. Sorting and Printing Values from a List of Lists

"""

swap_avg_by_hour = []

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])

sorted_swap = sorted(swap_avg_by_hour, reverse=True)

# Sort the values and print the the 5 hours with the highest average comments.

print("Top 5 Hour for 'Ask HN' Comments")
for avg, hr in sorted_swap[:5]:
    print('{}: {} average comments per post'.format(
        dt.datetime.strptime(hr, "%H").strftime("%H:%M"), avg)
        )

"""
The hour that receives the most comments per post on average is 15:00, with 
an average of 38.59 comments per post. There's about a 60% increase in the 
number of comments between the hours with the highest and second highest 
average number of comments.

According to the data set documentation, the timezone used is Eastern Time in the US.
So, we could also write 15:00 as 3:00 pm est.

"""

