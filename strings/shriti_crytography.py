'''
Shriti was going through some cryptographic concept.
 She just got stuck at some place .
  She needs your help to sort out the situation.
   Your task is to help her in writing the decrypted string.

Input Description:
You are given with the strings.

Output Description:
Print the decrypted string

Sample Input :
3[aa]

Sample Output :
aaaaaa

'''


'''
s=input()
n=int(s[0])
a=[s[2],s[3]]
combine=a*n
combine=''.join(combine)
print(combine)
'''

s = input()
n = int(s[0])
a = []
for i in s:
    if i=='[':
        i=s.index(i)
        a.append(i)
    if i==']':
        break

print(a)
#combine = a * n
#combine = ''.join(combine)
#print(combine, end="")
