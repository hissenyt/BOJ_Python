import sys
input=sys.stdin.readline
t=int(input())
s,g=[],[]
for i in range(t):
    s,g=[],[]
    a=int(input())
    for j in range(a):
        b,c=input().split()
        c=int(c)
        s.append(b)
        g.append(c)
    ans=max(g)
    tmp=g.index(ans)
    print(s[tmp])