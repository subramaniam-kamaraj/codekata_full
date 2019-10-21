start=int(input())
stop=int(input())

if start<=100000 and start>0 and stop<=100000 and stop>0:
    for i in range(start+1,stop+1):
        if i%2==0 :
            print(i,end=" ")
else:
    print("invalid")
