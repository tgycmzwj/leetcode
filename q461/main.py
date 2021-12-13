# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x,y=str(bin(x))[2:],str(bin(y))[2:]
        x,y=x.zfill(max(len(x),len(y))),y.zfill(max(len(x),len(y)))
        return sum([x[i]!=y[i] for i in range(len(x))])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = 1
    y = 4
    solution=Solution()
    print(solution.hammingDistance(x,y))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
