# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def trailingZeroes(self, n: int) -> int:
        counter=0
        for i in range(1,n+1):
            while i%5==0:
                i=i//5
                counter=counter+1
        return counter



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=2009
    solution=Solution()
    print(solution.trailingZeroes(n))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
