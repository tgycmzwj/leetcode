# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pos=0
        longest=int(0)
        for i in range(len(s)):
            for j in range(len(s),i+longest,-1):
                if s[i:j]==s[i:j][::-1]:
                    longest=j-i
                    pos=i
                    break
        return s[pos:pos+longest]



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    s = "ac"
    print(solution.longestPalindrome(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
