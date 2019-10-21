#generate

start=input()
stop=input()


if start.isdigit()==True and stop.isdigit()==True:
    start=int(start)
    stop=int(stop)

    for i in range(start,stop):
        order=len(str(i))
        summ = 0
        temp=i
        while temp>0 :
            digit=temp%10
            summ+=digit**3
            temp//=10

        if i==summ:
            print(i)
else:
    print("invalid")