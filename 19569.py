import sys
input=sys.stdin.readline
tst=True
n=int(input())
if n%5!=1 and n%5 != 4:
    print("NO")
    exit()
else:
    print("YES")
    sys.stdout.flush()
    print(1)
    sys.stdout.flush()
    n-=1
    if n%5==0:
        while True:
            a=int(input())
            n-=a
            if n<=a+1:
                print(n)
                sys.stdout.flush()
                break
            else:
                if a==1:
                    print(1)
                    n-=1
                    sys.stdout.flush()
                    b=int(input())
                    if n<=b+1:
                        print(n)
                        exit()
                    n-=b
                    if b==1:
                        print(2)
                        n-=2
                        sys.stdout.flush()
                    else:
                        print(1)
                        n-=1
                        sys.stdout.flush()
                else:
                    print(5-a)
                    n-=5-a
                    sys.stdout.flush()
    else:
        a=int(input())
        n-=a
        if n<=a+1:
            print(n)
            sys.stdout.flush()
            exit()
        elif a==1:
            print(2)
            n-=2
            sys.stdout.flush()
        else:
            print(1)
            n-=1
            sys.stdout.flush()
        while True:
            b=int(input())
            n-=b
            if n<=b+1:
                print(n)
                exit()
            else:
                if b==1:
                    print(1)
                    n-=1
                    sys.stdout.flush()
                    d=int(input())
                    n-=d
                    if n<=d+1:
                        print(n)
                        exit()
                    if d==1:
                        print(2)
                        n-=2
                        sys.stdout.flush()
                    else:
                        print(1)
                        n-=1
                        sys.stdout.flush()
                else:
                    print(5-b)
                    n-=5-b
                    sys.stdout.flush()