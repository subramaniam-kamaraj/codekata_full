'''
Given an arraylist A of string type which
 has name#mark1#mark2#mark3 format.
 Retrieve the name of the student who has scored max marks(total of three).

for eg: input: {'arun#12#12#12','deepak#13#12#12'}
output: Deepak
Input Size : A <= 100000
Sample Testcase :
INPUT
arun#12#12#12
deepak#13#12#12
OUTPUT
deepak
'''

'''
a=input()
#b=input()
a1=[]
a2=[]


for i in a:
    if i.isdigit()==True:
        a1.append(i)
        if i=='#':
            break

for j in a1:
    if a1.index(j)%2==0:
        a2.append(int(j)*10)
    else:
        a2.append(int(j))

print(a2)
print(sum(a2))

#print(a1)
#print(a2)
'''

def numsum(a):
    a1=[]
    a2=[]
    for i in a:
        if i.isdigit() == True:
            a1.append(i)
            if i == '#':
                break

    for j in a1:
        if a1.index(j) % 2 == 0:
            a2.append(int(j) * 10)
        else:
            a2.append(int(j))
    return sum(a2)

a=input()
b=input()
res=numsum(a)
res2=numsum(b)
print(res)
print(res2)

if res>res2:
    x=''
    for i in a:
        if i=='#':
            break
        else:
            x=x+i
    print(x)
else:
    x = ''
    for i in b:
        if i == '#':
            break
        else:
            x = x + i
    print(x)
