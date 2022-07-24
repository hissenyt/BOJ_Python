a,b,c=map(int,input().split())
if b==28:
    b=0
if c==19:
    c=0
for i in range(28*19+1):
    if b==(i*15+a)%28 and c==(i*15+a)%19 : 
        print(i*15+a)
        break