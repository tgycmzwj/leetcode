

class Solution:
    def to_dict(self,nums:str):
        results_dict={}
        for i in range(len(nums)):
            if nums[i] not in results_dict.keys():
                results_dict[nums[i]]=[i]
            else:
                results_dict[nums[i]].append(i)
        return results_dict
    def firstUniqChar(self, s: str) -> int:
        index=len(s)
        s_dict=self.to_dict(s)
        for key in s_dict.keys():
            if len(s_dict[key])==1:
                index=min(index,s_dict[key][0])
        return index if index!=len(s) else -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s='leetcode'
    solution=Solution()
    print(solution.firstUniqChar(s))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
