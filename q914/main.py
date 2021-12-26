# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import math
import collections
from typing import List
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        f = collections.Counter(deck)
        u = list(f.values())
        g = u[0]
        for j in range(1, len(u)):
            g = math.gcd(g, u[j])
        return g != 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    deck = [1,2,3,4,4,3,2,1]
    solution=Solution()
    print(solution.hasGroupsSizeX(deck))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
