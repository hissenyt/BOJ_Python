def eulerphi2(n):
    if n in [1,2]:return 1
    elif n in [3,4]:return 2
    ans=n
    ret=True
    for i in range(2,int(n**.5)+2):
        if n%i==0:
            ret=False
            exp=1
            n//=i
            while n%i==0:
                n//=i
                exp+=1
            return i**(exp-1)*(i-1)*eulerphi2(n)
    if ret:return n-1

n=int(input())
l=list()

if n==1:print(1);
elif n==2:print(2);
elif n%2==1:print(-1);
else:
    for i in range(3,int(n**0.5+1)):
        if n%i==0:
            l.append(i)

    for j in range(len(l)):
        l.append(n//l[j])
    dev = False
    for i in l:
        if eulerphi2(i)*i==n:
            print(i)
            dev=True
            break
    if dev == False:
        print(-1)