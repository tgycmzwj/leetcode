# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import math
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        #ax + by = c
        if (jug1Capacity + jug2Capacity < targetCapacity):
            return False
        if ((jug1Capacity == targetCapacity) or (jug2Capacity == targetCapacity) or (jug1Capacity + jug2Capacity == targetCapacity) or
                (0 == (targetCapacity % math.gcd(jug1Capacity, jug2Capacity)))):
            return True

        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    jug1Capacity = 2
    jug2Capacity = 6
    targetCapacity = 5
    solution=Solution()
    print(solution.canMeasureWater(jug1Capacity,jug2Capacity,targetCapacity))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
