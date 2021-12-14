# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        dic_strobo={'0':'0','1':'1','2':'000','3':'000','4':'000',
                    '5':'000','6':'9','7':'000','8':'8','9':'6'}
        results=''
        for i in num:
            results=dic_strobo[i]+results
        return results==num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num = "69"
    num = "88"
    num="962"
    solution=Solution()
    print(solution.isStrobogrammatic(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
