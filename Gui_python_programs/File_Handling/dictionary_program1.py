inp=input()                       #madam
lcount={}

for letter in inp:
    if letter in lcount:
        lcount[letter]+=1
    else:
        lcount[letter]=1
for k,v in lcount.items():
    print(k,"-",v)
print(sum(lcount.values()))