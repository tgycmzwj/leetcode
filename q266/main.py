# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dic={}
        for i in s:
            if i in dic.keys():
                dic[i]+=1
            else:
                dic[i]=1
        counter=0
        for k,v in dic.items():
            if v%2==1:
                counter+=1
            if counter>1:
                return False
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "carerac"
    solution=Solution()
    print(solution.canPermutePalindrome(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
