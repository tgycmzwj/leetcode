# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic={}
        for i in range(len(s)):
            if s[i] in dic.keys():
                dic[s[i]]=dic[s[i]]+1
            else:
                dic[s[i]]=1
        leng=0
        flag=0
        for k,v in dic.items():
            if v%2==1:
                flag=1
            if v>=2:
                if v%2==1:
                    leng=leng+v-1
                else:
                    leng=leng+v
        if flag==0:
            return leng
        return leng+1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "abccccdd"
    solution=Solution()
    print(solution.longestPalindrome(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
