# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def repeatedSubstringPattern(self, s: str)->bool:
        for i in range(1,len(s)//2+1):
            if len(s)%i==0:
                if s==s[:i]*(len(s)//i):
                    return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "a"
    solution=Solution()
    print(solution.repeatedSubstringPattern(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
