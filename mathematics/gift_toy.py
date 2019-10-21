'''
Assume you are john. John has one younger sister ‘jenny’.
He wants to gift her some toys.
He has a price list of toys and he has some amount on hand.
Your task is to tell him how many toys john will be able to buy for her sister

Input Description:
First line contains two integer ‘n’ and ‘k’ ,n denotes the number
 of toys and k denotes total money he has.
Next line contains n space separated integers denoting price of each toy

Output Description:
Print the max number of toys he can buy.

Sample Input :
7 50
1 12 5 111 200 1000 10

Sample Output :

4
'''

n,k=map(int,input().split())
toys=list(map(int,input().split()))[:n]
sor=sorted(toys)
summ=0
coun=0
for i in sor:
    if i<=k:
        summ=summ+i
        coun=coun+1
        if (summ >k) or (i>k):
            break

print(coun)


