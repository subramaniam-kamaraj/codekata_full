'''You are given a number ‘n’.
Your task is to develop an algorithm to tell whether the number
is ‘ajs’ or not.An ‘ajs’ number is a number
whose sum of first two digits is present in given number ‘n’

Sample Input :
9817

Sample Output :
1 '''

def isajs(num):
    strconvert=str(num)
    first=int(strconvert[0])
    second=int(strconvert[1])
    #add=sum(int(first) ,int(second))
    add=first+second
    return add
num=int(input())


'''
check=isajs(num)
#print(check)
convert_check=str(check)
convert_num=str(num)
chek_list=list(convert_check)
num_list=list(convert_num)
#print(chek_list)
#print(num_list)

if chek_list[0] in num_list:
    ind=num_list.index(chek_list[0])
    if chek_list[1]==num_list[ind+1]:
        print(1)
    #print(num_list.index(chek_list[0]))


'''