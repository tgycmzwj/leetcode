# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def maximumSwap(self, num: int) -> int:
        num=list(str(num))
        num=[int(i) for i in num]
        for i in range(len(num)):
            if num[i]!=max(num[i:]):
                max_index=[j for j in range(i,len(num)) if num[j]==max(num[i:])][-1]
                num[i],num[max_index]=num[max_index],num[i]
                break
        return int(''.join([str(i) for i in num]))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num = 927367
    solution=Solution()
    print(solution.maximumSwap(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
