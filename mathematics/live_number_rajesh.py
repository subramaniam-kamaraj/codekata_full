'''
Rajesh is very fond of numbers.
With the given positive number(‘n’) ,he has to tell whether a number
  is lively or not.
A lively number is a number which has same frequency of all integers present.

Input Description:
A integer ‘n’ will be given

Output Description:
Print 1 if number is lively and 0 if it is not lively.

Sample Input :
1212

Sample Output :
1

'''
'''
N=int(input())
fac=1
for i in range(1,N+1):
    fac=fac*i
print(fac)'''

import math
N=int(input())
print(math.factorial(N))