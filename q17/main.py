# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def binary_combine(self,number_list: List[str],str)->List[str]:
        if str=='':
            return number_list
        if len(number_list)==0:
            number_list.append(str)
            return number_list
        else:
            new_number_list=[]
            original_length=len(number_list[0])
            for digits in number_list:
                for i in range(original_length+1):
                    digits_copy=digits.copy()
                    digits_copy.insert(i,str)
                    new_number_list.append(digits_copy)
        return new_number_list

    def combine(self,str_to_list):
        results=[[str_to_list[0]]]
        for i in range(1,len(str_to_list)):
            results=self.binary_combine(results,str_to_list[i])
        return results

    def cartesian(self,compount_list: List[List[str]])->List[str]:
        if len(compount_list)==0:
            return compount_list
        if len(compount_list)==1:
            return compount_list[0]
        if len(compount_list)==2:
            results=[]
            for i in compount_list[0]:
                for j in compount_list[1]:
                    results.append(i+j)
            return results
        else:
            temp=self.cartesian(compount_list[:-1])
            results = []
            for i in temp:
                for j in compount_list[-1]:
                    results.append(i + j)
            return results


    def letterCombinations(self, numbers: str) -> List[str]:
        if len(numbers)==0:
            return []
        int_to_char_dict={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        str_to_list=[[]]
        for i in range(len(numbers)):
            str_to_list[0].append(numbers[i])
        #num_combinations=self.combine(str_to_list)

        outputs=[]
        for i in str_to_list:
            number_list=[int_to_char_dict[key] for key in i]
            outputs.append(self.cartesian(number_list))

        return [item for sublist in outputs for item in sublist]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    digits = "234"
    print(solution.letterCombinations(digits))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
