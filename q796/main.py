# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):return False
        for i in range(len(goal)):
            if goal[i]==s[0]:
                if goal[i:]+goal[:i]==s:
                    return True
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "abcde"
    goal = "cdeab"
    solution=Solution()
    print(solution.rotateString(s,goal))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
