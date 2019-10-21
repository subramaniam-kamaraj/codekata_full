'''

You are given a string ‘S’ consisting of lowercase Latin Letters.
 Find the first non repeating character in S.
 If you find all the characters are repeating print the answer as -1

Input Description:
You are given a string ‘s’

Output Description:
Print the first non occurring character if possible else -1.

Sample Input :
apple

Sample Output :
a

'''
S=input()
em=[]

if S.islower()==True:
    for i in S:
        if i not in em:
            print(S[0])
        else:
            em.append(i)


else:
    print("-1")