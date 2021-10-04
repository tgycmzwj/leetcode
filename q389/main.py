# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def to_dict(self,nums:str):
        results_dict={}
        for i in nums:
            if i not in results_dict.keys():
                results_dict[i]=1
            else:
                results_dict[i]=results_dict[i]+1
        return results_dict
    def findTheDifference(self, s: str, t: str) -> str:
        s,t=self.to_dict(s),self.to_dict(t)
        for key in t.keys():
            if key not in s:
                return key
            elif s[key]<t[key]:
                return key


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    solution=Solution()
    print(solution.findTheDifference(s,t))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
