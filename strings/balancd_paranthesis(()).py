s = input()

if s[0]==')' :
    cnt = -1
else :
    cnt=1
    for i in range(1,len(s)) :
        if s[i] == '(':
            cnt += 1
        else :
            cnt -= 1
        if cnt < 0 :
            res = 'no'
            break
if cnt==0 :
	res = 'yes'
else :
	res = 'no'

print(res,end='')