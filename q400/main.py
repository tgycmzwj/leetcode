class Solution:
    def findNthDigit(self, n: int) -> int:
        digit=1
        base=0
        while n>base+9*10**(digit-1)*digit:
            base=base+9*10**(digit-1)*digit
            digit=digit+1

        number=(10**(digit-1)-1)+(n-base)//digit
        reminder=(n-base)%digit
        if reminder == 0:
            return int(str(number)[-1])
        else:
            return int(str(number+1)[reminder-1])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=11134
    solution=Solution()
    print(solution.findNthDigit(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
