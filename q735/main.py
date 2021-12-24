# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in asteroids:
            stack.append(i)
            while len(stack)>=2:
                if stack[-1]<0 and stack[-2]>=0:
                    if stack[-1]+stack[-2]<0:
                        stack.pop(-2)
                    elif stack[-1]+stack[-2]==0:
                        stack.pop(-1)
                        stack.pop(-1)
                    else:
                        stack.pop(-1)
                else:
                    break
        return stack

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asteroids = [10,2,-5]
    solution=Solution()
    print(solution.asteroidCollision(asteroids))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
