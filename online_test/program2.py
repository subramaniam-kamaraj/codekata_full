
'''def get_count(num_list):
    count=0
    i=0

    while(i<(len(num_list)-1)):
        if(num_list[i]==num_list[i+1]):
            count+=1
        i+=1

    return count
'''
alist=list(map(int,input().split()))
coun=0
cpy=[]

for i in alist:
    if alist.count(i)==1:
        print(i)


