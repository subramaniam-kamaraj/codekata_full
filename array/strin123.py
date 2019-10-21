s=input()
vo='aeiouAEIOU'
c=''
d=''
for i in s:
    if i in vo:
        c=c+i
    else:
        d=d+i

print(c+d)