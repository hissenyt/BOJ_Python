import sys
input=sys.stdin.readline
n,k=map(int,input().split())
l=[]
a=k%10
b=(2*k)%10
for i in range(1,n+1):
    if i%10==a or i%10==b:
        pass
    else:
        l.append(i)
print(len(l))
for j in l:
    print(j,end=" ")