'''

:You are given an array of ‘n’ numbers.
 your task is to print the lcm of ‘n’ numbers

Input Description:
An integer ‘n’ denoting the size of array.
  Next line contains ‘n’ space separated numbers

Output Description:
Print the lcm

Sample Input :
4
2 4 6 8

Sample Output :
24

'''

n=int(input())
lis=list(map(int,input().split()))
lis.sort(reverse = True)

x = lis[0]

while 1:
    sum = 0
    for i in lis:
        if x%i == 0:
            sum += 1
    if sum == len(lis):
        break
    else :
        x += 1
print(x)
