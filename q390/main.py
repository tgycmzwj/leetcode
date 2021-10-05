# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def lastRemaining(self, n: int) -> int:
        L2R = 1  #direction
        head = 1
        remaining = n
        steps = 1
        while remaining > 1:
            # if L2R == 1 or remaining & 1:
            if L2R == 1 or remaining % 2 == 1:
                head += steps
            remaining //= 2
            steps *= 2
            # L2R ^= 1
            L2R = 1 - L2R
        return head

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=9
    solution=Solution()
    print(solution.lastRemaining(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
