# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        result, last_seen,count = [], {}, 0
        for i in range(len(s)):
            last_seen[s[i]]=i
        string_last_seen=0
        for i in range(len(s)):
            string_last_seen=max(string_last_seen,last_seen[s[i]])
            if i==string_last_seen:
                result.append(i+1)
        for i in range(len(result)-1,0,-1):
            result[i]=result[i]-result[i-1]
        return result



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "ababcbacadefegdehijhklij"
    solution=Solution()
    print(solution.partitionLabels(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
