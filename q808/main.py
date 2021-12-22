# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def sup(self,na,nb,mem):
        if (na,nb) in mem:
            return mem[(na,nb)]
        if na<=0 and nb>0:return 1
        if na>0 and nb<=0:return 0
        if na<=0 and nb<=0:return 0.5
        if na>0 and nb>0:
            result=0.25*(self.sup(na-100,nb,mem)+self.sup(na-75,nb-25,mem)+self.sup(na-50,nb-50,mem)+self.sup(na-25,nb-75,mem))
            mem[(na,nb)]=result
            return result
    def soupServings(self, n: int) -> float:
        mem={}
        return self.sup(n,n,mem)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 500
    solution=Solution()
    print(solution.soupServings(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
