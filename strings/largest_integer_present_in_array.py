'''
You are given with a string which comprises of some numbers.
  Your task is to find the largest integer present in the string.

Input Description:
First line contains n denoting number of Test Cases.
  The first and only Line of testcase has the string

Output Description:
Print the largest number

Sample Input :
I was born on 12 october 1998.

Sample Output :
1998

'''

s=input()
cpy=[]
for i in s.split():
    if i.isdigit()==True:
        cpy.append(int(i))
print(max(cpy))

