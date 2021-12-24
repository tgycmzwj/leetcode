# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution(object):
    def repeatedStringMatch(self, A, B):
        times = int(len(B)/len(A))
        for i in range(times,times+5):
            if B in A*i:
                return i
        return -1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = "abcd"
    b = "cdabcdab"
    solution=Solution()
    print(solution.repeatedStringMatch(a,b))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
