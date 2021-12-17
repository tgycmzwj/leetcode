# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans, prev, cur = 0, 0, 1
        for i in range(1,len(s)):
            if s[i]!=s[i-1]:
                ans+=min(prev,cur)
                prev=cur
                cur=1
            else:
                cur+=1
        ans+=min(prev, cur)
        return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "00110011"
    solution=Solution()
    print(solution.countBinarySubstrings(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
