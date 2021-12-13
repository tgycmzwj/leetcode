# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        max_len=max(len(num1),len(num2))
        num1,num2=num1.zfill(max_len),num2.zfill(max_len)
        results=''
        flag=0
        for i in range(max_len-1,-1,-1):
            if int(num1[i])+int(num2[i])+flag>=10:
                results=str(int(num1[i])+int(num2[i])+flag)[-1]+results
                flag=1
            else:
                results=str(int(num1[i])+int(num2[i])+flag)+results
                flag=0
        if flag==1:
            results='1'+results
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num1 = "456"
    num2 = "77"
    num1="123456789"
    num2="987654321"
    num1="584"
    num2="18"
    solution=Solution()
    print(solution.addStrings(num1,num2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
