start=int(input())
stop=int(input())

if start<=100000 and stop<=100000:
    for i in range(start,stop+1,2):
        print(i,end=" ")
else:
    print("invalid")


