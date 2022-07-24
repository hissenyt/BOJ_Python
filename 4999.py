#fibonacci(30) = 832040

f=[0,1,1,2]
for i in range(4,32):
    f.append(f[i-1]+f[i-2])

n=int(input())
l=[0,1,-1,-1,1,-1,1,2,-1,1,2,3,1,-1,1,2,3,1,5,1,2]
tmp=100000000
j=6

for i in range(21,n+1):
    if i>f[j+1]:
        j+=1
    if i-f[j] in f:
        l.append(i-f[j])
    else:
        l.append(l[i-f[j]])
if n in f:
    print(-1)
else:
    print(l[n])