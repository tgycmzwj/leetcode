# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def countSegments(self, s: str) -> int:
        if len(s.strip())==0:
            return 0
        s=' '.join(s.strip().split())
        return len(s.strip().split(' '))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "Hello,  my name is John"

    solution=Solution()
    print(solution.countSegments(s))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
