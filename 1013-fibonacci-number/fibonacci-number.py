class Solution:
    def fib(self, n: int) -> int:
        # #recursive solution
        # if n==0:
        #     return 0
        # elif n==1:
        #     return 1
        # else:
        #     return self.fib(n-1)+self.fib(n-2)
        #Top down memorization- O(n), SC-O(n)
        # memo={0:0,1:1}
        # def f(x):
        #     if x in memo:
        #         return memo[x]
        #     else:
        #         memo[x]=f(x-1)+f(x-2)
        #         return memo[x]
        # return f(n)

        #Bottom up Tabulation: TC-O(n), SC-O(n)
        # if n==0:
        #     return 0
        # if n==1:
        #     return 1
        # dp=[0]*(n+1)
        # dp[0]=0
        # dp[1]=1
        # for i in range(2,n+1):
        #     dp[i]=dp[i-1]+dp[i-2]
        # return dp[n]

        #Constant Space solution- TC-O(n),SC-O(1)
        if n==0:
            return 0
        if n==1:
            return 1
        prev=0
        curr=1
        for i in range(2,n+1):
            prev,curr=curr,prev+curr
        return curr