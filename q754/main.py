# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import math
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        n = math.ceil(math.sqrt(2*target)-1) # n = 1 gives O(sqrt(target)) solution
        while True:
            upper = n * (n+1) // 2
            if upper >= target and (upper - target) % 2 == 0:
                break
            n += 1
        return n

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    target=11
    solution=Solution()
    print(solution.reachNumber(target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
