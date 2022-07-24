dp=[0]*1000001
for i in range(1000001):
    dp[1]=0
    if i==1:
        pass
    dp[i]=dp[i-1]+1
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
print(dp[int(input())])