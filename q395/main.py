# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
class Solution:
    def longestSubstring(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "aaabb"
    k = 3
    s = "ababbc"
    k = 2
    s="aaabasklsadgjaijisgdjaswieojsjfdkhsdhjfgajsgjshdfaub"
    k=3
    s="aaabbb"
    k=3
    s="weitong"
    k=2
    solution=Solution()
    print(solution.longestSubstring(s,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
