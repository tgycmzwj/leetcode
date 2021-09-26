# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def isHappy(self, n: int) -> bool:
        residual=[n]
        n_str=list(str(n))
        n=sum([int(i)**2 for i in n_str])
        if n==1:
            return True
        while n not in residual:
            residual.append(n)
            if n==1:
                return True
            n_str=list(str(n))
            n=sum([int(i)**2 for i in n_str])

        return False



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    n=2
    print(solution.isHappy(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
