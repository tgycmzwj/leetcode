# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        all_results={}
        for i in range(len(s)):
            all_results[i]=[]
            if s[:i+1]==s[:i+1][::-1]:
                all_results[i].append([s[:i+1]])
            for j in range(i):
                if s[j+1:i+1]==s[j+1:i+1][::-1]:
                    for partitions in all_results[j]:
                        new_partition=partitions.copy()
                        new_partition.append(s[j+1:i+1])
                        all_results[i].append(new_partition)
        return all_results[len(s)-1]








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    s = "a"
    print(solution.partition(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
