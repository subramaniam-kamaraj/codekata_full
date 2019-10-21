'''
Given a date(DD-MM-YYYY), print the month in words.
Sample Testcase :
INPUT
01-01-2018
OUTPUT
January
'''

date = input()
month_one = date[3]
month = date[4]
if month is '1' and month_one is '0':
    print("January")
elif month is '2' and month_one is '0':
    print("February")
elif month is '3' and month_one is '0':
    print("March")
elif month is '4' and month_one is '0':
    print("April")
elif month is '5' and month_one is '0':
    print("May")
elif month is '6' and month_one is '0':
    print("June")
elif month is '7' and month_one is '0':
    print("July")
elif month is '8' and month_one is '0':
    print("August")
elif month is '9' and month_one is '0':
    print("September")
elif month is '0' and month_one is '1':
    print("October")
elif month is '1' and month_one is '1':
    print("November")
elif month is '2' and month_one is '1':
    print("December")

