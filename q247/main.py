# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
import itertools
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        dic_strobo1={'0':'0','1':'1','8':'8','6':'9','9':'6'}
        ext=['0','1','8']
        if n==1:
            return ext
        key=list(dic_strobo1.keys())
        results1=[]
        for i in itertools.combinations_with_replacement(key,n//2):
            for j in itertools.permutations(i):
                results1.append(''.join(j))
        results2=[]
        for i in results1:
            temp=''
            for j in i:
                temp=dic_strobo1[j]+temp
            results2.append(temp)
        results=[]
        if n%2==0:
            results=[results1[i]+results2[i] for i in range(len(results1))]
        else:
            for i in ext:
                for j in range(len(results1)):
                    results.append(results1[j]+i+results2[j])
        results=[i for i in results if not (len(i)!=1 and i[0]=='0')]
        return list(set(results))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=5
    solution=Solution()
    print(solution.findStrobogrammatic(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
