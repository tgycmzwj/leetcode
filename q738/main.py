# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        n=[int(i) for i in list(str(n))]
        i=0
        for i in range(1,len(n)):
            if n[i]<n[i-1]:
                while i>=1 and n[i]<=n[i-1]:   #where to decrease one
                    i-=1
                n[i]=n[i]-1
                break
        for j in range(i+1,len(n)):
            n[j]=9
        n=int(''.join([str(i) for i in n]))
        return n

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=100
    solution=Solution()
    print(solution.monotoneIncreasingDigits(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
