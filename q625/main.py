# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def smallestFactorization(self, num: int) -> int:
        factors=[]
        for i in range(9,1,-1):
            while num%i==0:
                factors.append(str(i))
                num=num//i
        if num!=1:
            return 0
        results=int(''.join(factors[::-1]))
        if results>pow(2,31)-1:
            return 0
        return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num = 48
    solution=Solution()
    print(solution.smallestFactorization(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
