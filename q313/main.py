# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
import heapq
class Solution:
    def nthSuperUglyNumber_slow(self, n: int, primes: List[int]) -> int:
        factors_pos=[0]*len(primes)
        results=[1]+primes.copy()
        len_counter=0
        while len_counter<n:
            cur_min=float('inf')
            min_pos=-1
            other_to_be_add=[]
            for i in range(len(primes)):
                while primes[i]*results[factors_pos[i]] in results:
                    factors_pos[i]=factors_pos[i]+1
                if primes[i]*results[factors_pos[i]]<cur_min:
                    cur_min=primes[i]*results[factors_pos[i]]
                    min_pos=i
            results.append(cur_min)
            if cur_min<primes[-1]:
                print('heheda')
                results.sort()
            len_counter=len_counter+1

        return results[n-1]

    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = primes.copy()  # do a deep copy
        heapq.heapify(nums)  # create a heap
        p = 1
        for i in range(n - 1):
            p = heapq.heappop(nums)  # take the smallest element
            for prime in primes:
                heapq.heappush(nums, p * prime)  # add all those multiples with the smallest number
                if p % prime == 0:
                    break
        return p


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 1200
    primes = [2,7,13,19]
    # n=1
    # primes=[2,3,5]
    # n=4
    # primes=[2,3,5]
    n=100000
    primes=[7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131, 137, 139, 157, 167, 179, 181, 199, 211,
     229, 233, 239, 241, 251]
    solution=Solution()
    print(solution.nthSuperUglyNumber(n,primes))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
