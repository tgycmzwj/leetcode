# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[1] = 0
        divisors = []
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                divisors.append(i)
        for j in divisors:
            dp[j]+=1 #click copy
            for i in range(j+1,n+1):
                if i%j==0:
                    dp[i]=min(dp[i],dp[i-j]+1)
        return dp[-1]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=18
    solution=Solution()
    print(solution.minSteps(n))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
