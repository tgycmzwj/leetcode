# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def largeGroupPositions(self, s):
        s += " "
        ret = []
        c = 1
        for i, x in enumerate(s[1:], 1):
            if x == s[i-c]:
                c += 1
            else:
                if c >= 3:
                    ret.append([i-c, i-1])
                c = 1
        return ret

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "abbxxxxzzy"
    solution=Solution()
    print(solution.largeGroupPositions(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
