# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import time
class Solution_old:
    def NOTPrime(self,n):
        if n>1:
            for i in range(2,int(n**0.5)+1):
                if (n%i==0):
                    return True
            return False
        return False
    def countPrimes(self, n: int) -> int:
        if n<3:
            return 0
        prime=[0]*2+[2]*(n-2)
        i=2
        while (i<n):
            if prime[i]==2:
                if self.NOTPrime(i)==False:
                    prime[i]=1
                for j in range(2,n//i):
                    if prime[i*j]==2:
                        prime[i*j]=0
            i=i+1
        return prime.count(1)
    def countPrimes_old(self, n: int) -> int:
        if n<=2:
            return 0
        num_primes=1
        for i in range(3,n,2):
            if self.NOTPrime(i)==False:
                num_primes=num_primes+1
        return num_primes


class Solution:
    def countPrimes(self, n: int) -> int:
        isPrime = [False, False] + [True] * (n - 2)
        i = 2
        while (i * i < n):
            if (isPrime[i]):
                j = i*2
                while (j < n):
                    isPrime[j] = False
                    j += i
            i += 1
        return sum(isPrime)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   n=10

   solution=Solution()
   a=time.time()
   print(solution.countPrimes(n))
   print(time.time()-a)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
