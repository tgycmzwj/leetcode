# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s==goal and len(s)!=len(set(s)):
            return True
        diffs = [i for i in range(len(s)) if s[i]!=goal[i]]
        return len(s)==len(goal) and len(diffs)==2 and s[diffs[0]]==goal[diffs[1]] and s[diffs[1]]==goal[diffs[0]]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "ab"
    goal = "ba"
    solution=Solution()
    print(solution.buddyStrings(s,goal))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
