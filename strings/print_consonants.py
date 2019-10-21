'''

You are given a string.Your task is to print only the consonants present in the string.

Input Description:
You are given a string ‘s’.

Output Description:
Print only consonants.

Sample Input :
I am shrey

Sample Output :
m shry
'''
vowels='aeiouAEIOU'
s=input()
cpy=[]
for i in s:
    if i not in vowels:
        cpy.append(i)
        #print(i,end="")
c=cpy[1:]
for i in c:
    print(i,end="")