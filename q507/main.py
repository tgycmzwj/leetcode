# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def checkPerfectNumber(self,num:int)->bool:
        divisor=[1]
        for i in range(2,int(pow(num,0.5))+1):
            if num%i==0:
                divisor.append(i)
                if num/i!=i:
                    divisor.append(num/i)
        return sum(divisor)==num


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    num=28
    solution=Solution()
    print(solution.checkPerfectNumber(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
