# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def isNumber(self, s: str) -> bool:
        if 'inf' in s.lower():return False
        try: float(s)
        except ValueError:
            return False
        else:
            return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "."
    solution=Solution()
    print(solution.isNumber(s))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
