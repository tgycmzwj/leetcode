# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s=list(s)
        order=list(order)
        for i in 'abcedfghijklmnopqrstuvwxyz':
            if i not in order:
                order.append(i)
        s=sorted(s,key=lambda x: order.index(x))
        return ''.join(s)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    order = "cba"
    s = "abcd"
    solution=Solution()
    print(solution.customSortString(order,s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
