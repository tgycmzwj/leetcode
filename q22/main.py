# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def str_to_list(self,str_input: str)->List[str]:
        str_list=[]
        for i in range(len(str_input)):
            str_list.append(str_input[i])
        return str_list

    def one_more_parenthesis(self,cur_list: List[str])->List[str]:
        results=[]
        for item in cur_list:
            str_to_list=self.str_to_list(item)
            for loc1 in range(len(str_to_list)+1):
                str_to_list_copy1=str_to_list.copy()
                str_to_list_copy1.insert(loc1,'(')
                for loc2 in range(loc1+1,len(str_to_list_copy1)+1):
                    str_to_list_copy2=str_to_list_copy1.copy()
                    str_to_list_copy2.insert(loc2,')')
                    if str_to_list_copy2 not in results:
                        results.append(str_to_list_copy2)
        return results



    def generateParenthesis(self, n: int) -> List[str]:
        if n==0:
            return [""]
        if n==1:
            return ["()"]
        else:
            results=["()"]
            for i in range(n-1):
                results=self.one_more_parenthesis(results)
            return [''.join(item) for item in results]
        


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    n=8
    print(solution.generateParenthesis(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
