# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic={}
        for i in tasks:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]=dic[i]+1
        max_freq=max(dic.items(),key=lambda x:x[1])
        total_job=sum(dic.values())-max_freq[1]
        counter=0
        for k,v in dic.items():
            if v==max_freq[1]:
                counter=counter+1
        capacity=(max_freq[1]-1)*(n+1)
        return max(capacity+counter,len(tasks))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    solution=Solution()
    print(solution.leastInterval(tasks,n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
