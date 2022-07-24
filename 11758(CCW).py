x_1,y_1=map(int,input().split())
x_2,y_2=map(int,input().split())
x_3,y_3=map(int,input().split())
a_1,b_1=x_2-x_1,y_2-y_1
a_2,b_2=x_3-x_2,y_3-y_2
if a_1*b_2-b_1*a_2>0:
    print(1)
elif a_1*b_2-b_1*a_2==0:
    print(0)
else:
    print(-1)