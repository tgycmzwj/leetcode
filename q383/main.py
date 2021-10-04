

class Solution:
    def to_dict(self,nums:str):
        results_dict={}
        for i in nums:
            if i not in results_dict.keys():
                results_dict[i]=1
            else:
                results_dict[i]=results_dict[i]+1
        return results_dict
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1,dict2=self.to_dict(ransomNote),self.to_dict(magazine)
        for key in dict1:
            if key not in dict2.keys():
                return False
            elif dict2[key]<dict1[key]:
                return False
        return True



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ransomNote = "aa"
    magazine = "aab"
    solution=Solution()
    print(solution.canConstruct(ransomNote,magazine))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
