'''
    A dish in Alphabet Land is made up of lower case English alphabets.

You are given a source dish. Each alphabet from the source dish can be used as an ingredient at most once. The ingredients can be combined later to prepare a new dish.



Your task is to determine if a given dish can be prepared from the
    ingredients of the source dish.

Input Description:
The first line is a string S denoting the source dish.
    The next line is an integer N denoting the number of dishes
     that have to be prepared. N lines follow.
       Each line consists of a string A representing a dish.

Output Description:
Print N lines. A line should contain ‘YES’ if the dish can be prepared
    from the source dish or ‘NO’ if the dish cannot be prepared from the
        source dish.

Sample Input :
abbbcc
4
ab
abccc
abbcc
abd

Sample Output :
YES
NO
YES
NO

'''

lis=input()
n=int(input())
cpy=[]
for i in range(1,n+1):
    cpy.append(input())

for j in cpy:
    if j in lis:
        print("YES")
    else:
        print("NO")
