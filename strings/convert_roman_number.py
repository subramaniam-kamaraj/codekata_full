'''
Given a roman numeral N, convert it into integer.If it is not a valid roman numeral print '-1'
Input Size : N <= 20
Sample Testcase :
INPUT
VI
OUTPUT
6
INPUT
Y
OUTPUT
-1

'''



inp=input()
if inp is 'I':
	print("1")
elif inp == 'II':
    print("2")
elif inp == 'III':
	print("3")
elif inp == 'IV':
	print("4")
elif inp == 'V':
	print("5")
elif inp == 'VI':
	print("6")
elif inp == 'VII':
	print("7")
elif inp == 'VIII':
	print("8")
elif inp == 'IX':
	print("9")
elif inp == 'X':
	print("10")
elif inp == 'XI':
	print("11")
elif inp == 'XII':
	print("12")
elif inp == 'XIII':
	print("13")
elif inp == 'XIV':
	print("14")
elif inp == 'XV':
	print("15")
elif inp == 'XVI':
	print("16")
elif inp == 'XVII':
	print("17")
elif inp == 'XVIII':
	print("18")
elif inp == 'XIX':
	print("19")
elif inp == 'XX':
	print("20")
else:
	print("-1")