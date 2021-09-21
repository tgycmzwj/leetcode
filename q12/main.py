# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def intToRoman(self, num: int) -> str:
        output=''
        while num>0:
            if num>=1000:
                output=output+'M'
                num=num-1000
            elif num>=900:
                output=output+'CM'
                num=num-900
            elif num>=500:
                output=output+'D'
                num=num-500
            elif num>=400:
                output=output+'CD'
                num=num-400
            elif num>=100:
                output=output+'C'
                num=num-100
            elif num>=90:
                output=output+'XC'
                num=num-90
            elif num>=50:
                output=output+'L'
                num=num-50
            elif num>=40:
                output=output+'XL'
                num=num-40
            elif num>=10:
                output=output+'X'
                num=num-10
            elif num>=9:
                output=output+'IX'
                num=num-9
            elif num>=5:
                output=output+'V'
                num=num-5
            elif num>=4:
                output=output+'IV'
                num=num-4
            else:
                output=output+'I'
                num=num-1
        return output




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    num=3
    print(solution.intToRoman(num))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
