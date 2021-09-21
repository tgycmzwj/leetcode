# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Solution:
    def binary_search(self,x,left,right):
        med=(left+right)/2
        if med*med>x:
            return self.binary_search(x,left,int(med))
        elif (int(med)+1)*(int(med)+1)>x:
            return int(med)
        else:
            return self.binary_search(x,int(med)+1,right)
    def mySqrt(self, x: int) -> int:
        return self.binary_search(x,0,x)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    x=99
    print(solution.mySqrt(x))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
