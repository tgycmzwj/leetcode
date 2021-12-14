# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
import itertools
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        results=[]
        dic = {}
        for i in s:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        counter=0
        mid='NA'
        candi=''
        for k,v in dic.items():
            if v%2==1:
                counter+=1
                mid=k
                candi=candi+(k*((v-1)//2))
            else:
                candi=candi+(k*(v//2))
            if counter>1:
                return []
        results=[]
        for i in itertools.permutations(candi):
            results.append(''.join(i))
        for i in range(len(results)):
            if mid!='NA':
                results[i]=results[i]+mid+results[i][::-1]
            else:
                results[i] = results[i]+ results[i][::-1]
        return list(set(results))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s="aabb"
    solution=Solution()
    print(solution.generatePalindromes(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
