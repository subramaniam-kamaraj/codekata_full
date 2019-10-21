'''
Rampal is a number in which the sum of last two digits of 
 that number is multiple of 4. 
 Your teacher has given you the task to make a list of rampal numbers.
   Your task is to tell whether the number is rampal or not.

Note : if the number is negative than rampal 
  is a number which has sum of first and last digit as multiple of 4  

Input Description:
First line contains an input n

Output Description:
Print Yes or No 

Sample Input :
20
Sample Output :
No

'''

n = int(input())
res = 'No'
if abs(n) >=10 and n > 0 :
    a = n%100
    if a%4==0 :
        res = 'Yes'
elif abs(n) >=10 and n < 0 :
    s = str(abs(n))
    a = int(s[0]) + int(s[-1])
    if a%4==0 :
        res = 'Yes'
print(res,end='')