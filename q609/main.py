# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic={}
        for path in paths:
            path=path.split(' ')
            for i in range(1,len(path)):
                name,cont=path[i].split('(')
                if cont not in dic:
                    dic[cont]=[path[0]+'/'+name]
                else:
                    dic[cont].append(path[0]+'/'+name)
        results=[]
        for k,v in dic.items():
            results.append(v)
        return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
    solution=Solution()
    print(solution.findDuplicate(paths))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
