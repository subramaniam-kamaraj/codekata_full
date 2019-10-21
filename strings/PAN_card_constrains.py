'''
Indian PAN card issuing authority have found some fake PAN cards. They have hired you so that you can validate PAN card for them. Your task is to develop a suitable algorithm which could check if pan is valid or not

1)Pan must have uppercase letters only.

2)It must be of 10 character only

3)From index 1 to 5 all must be letters(A-Z),last index must be letter

4)Rest all must be integer Starting from 1

Input Description:
You are given a input string which indicates the PAN number

Output Description:
Print 'pan' if it is valid PAN number, else print 'not pan'

Sample Input :
HXTPS2142R

Sample Output :
pan

Code Editor

1
​

'''

s=input()
alp="ABCDEFGHIJKLMNOPQRSTUVWXYS"
if s.isupper()==True and len(s) is 10:
    for i in s isupper()==True:
        print('yes')
    else:
        print('no')
else:
    print("no")


'''


#3)
first 5 will be alphabets
inp=input()
alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
coun=0
for i in inp:
    if i in alp:
        if inp.index(i)<5:
            coun=coun+1
            if coun is 5:
                print('yes')

'''



'''
#first 5 will be alphabets
inp=input()
alp="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
coun=0
if inp.isupper()==True and len(inp) is 10:
    for i in inp:
        if i in alp:
            if inp.index(i)<5:
                coun=coun+1
                if coun is 5:
                    print('yes')
                    return(1)

'''