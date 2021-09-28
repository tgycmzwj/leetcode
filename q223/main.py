# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        size1=(ax2-ax1)*(ay2-ay1)
        size2=(bx2-bx1)*(by2-by1)
        x_intersect=min(ax2,bx2)-max(ax1,bx1)
        y_intersect=min(ay2,by2)-max(ay1,by1)
        overlap=x_intersect*y_intersect if x_intersect>0 and y_intersect>0 else 0
        return size1+size2-overlap

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ax1,ay1,ax2,ay2,bx1,by1,bx2,by2=-3,0,3,4,0,-1,9,2
    ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = -2,-2,2,2,-2,-2,2,2
    solution=Solution()
    print(solution.computeArea(ax1,ay1,ax2,ay2,bx1,by1,bx2,by2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
