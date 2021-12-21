# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def validPalindrome(self, s: str) -> bool:
        s=list(s)
        if s==s[::-1]:return True
        i=0
        for i in range(len(s)//2+1):
            if s[i]!=s[len(s)-1-i]:
                break
        option1=s[:i]+s[i+1:]
        option2=s[:len(s)-1-i]+s[len(s)-i:]
        if option1==option1[::-1] or option2==option2[::-1]:
            return True
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "abca"
    solution=Solution()
    print(solution.validPalindrome(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
