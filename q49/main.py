from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)<=1:
            return [strs]
        break_up={}
        for i in range(len(strs)):
            temp=[]
            for j in range(len(strs[i])):
                temp.append(strs[i][j])
            temp.sort()
            if ''.join(temp) not in break_up.keys():
                break_up[''.join(temp)]=[i]
            else:
                break_up[''.join(temp)].append(i)
        results=list(break_up.values())
        for i in range(len(results)):
            for j in range(len(results[i])):
                results[i][j]=strs[results[i][j]]
        return results




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    strs = ["a"]
    print(solution.groupAnagrams(strs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
