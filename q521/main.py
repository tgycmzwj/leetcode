# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a==b:
            return -1
        else:
            return max(len(a),len(b))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = "aba"
    b = "cdc"
    solution=Solution()
    print(solution.findLUSlength(a,b))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
