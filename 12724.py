import sys
input=sys.stdin.readline
t=int(input())
for i in range(t):
    a=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    x=sorted(x)
    y=sorted(y,reverse=True)
    ans=0
    for j in range(a):
        ans+=x[j]*y[j]
    print(f"Case #{i+1}: {ans}")