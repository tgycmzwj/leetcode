# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        max_poss=int(pow(n*2,0.5))+1
        results=1
        for i in range(2,max_poss):
            if i%2==1:
                if n%i==0:
                    results=results+1
            else:
                if n/i-(n//i)==0.5:
                    results=results+1
        return results



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=9
    solution=Solution()
    print(solution.consecutiveNumbersSum(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
