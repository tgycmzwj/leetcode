# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def findContestMatch(self, n: int) -> str:
        results=[]
        for i in range(1,n//2+1):
            results.append((i,n+1-i))
        while len(results)>1:
            length=len(results)//2
            first=results.copy()[:length]
            second=results.copy()[length:][::-1]
            results=[]
            for i in range(length):
                results.append((first[i],second[i]))
        return str(results[0]).replace(' ','')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 4096
    solution=Solution()
    print(solution.findContestMatch(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
