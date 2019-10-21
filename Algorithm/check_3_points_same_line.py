x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())
#x2=input()
#x3=input()

#x1,y1,x2,y2,x3,y3=A[0],A[1],B[0],B[1],C[0],C[1]
'''slop_AB=(y2-y1)//(x2-x1)
slop_BC=(y3-y2)//(x3-x2)
slop_AC=(y3-y1)//(x3-x1)
'''

if (x1 is x2 is x3) or (y1 is y2 is y3) or ((x1 is y1) and (x2 is y2) and (x3 is y3)):
    print("yes")
else:
    print("NO")