class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        while n>1:
            if n%4==0:
                n=n//4
            else:
                return False
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=16
    solution=Solution()
    print(solution.isPowerOfThree(n))
