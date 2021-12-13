# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        all_ele=[]
        temp=''
        for i in range(len(abbr)):
            if not abbr[i].isdigit():
                if len(temp)>0:
                    if temp[0]=='0':
                        return False
                    all_ele.append(int(temp))
                    temp=''
                all_ele.append(abbr[i])
            else:
                temp=temp+abbr[i]
        if len(temp)>0:
            if temp[0] == '0':
                return False
            all_ele.append(int(temp))
        pos=0
        tot_len=0
        for i in range(len(all_ele)):
            if type(all_ele[i])==str:
                tot_len=tot_len+len(all_ele[i])
            else:
                tot_len=tot_len+all_ele[i]
        if tot_len!=len(word):
            return False
        for i in range(len(all_ele)):
            if type(all_ele[i])==str:
                if all_ele[i]!=word[pos]:
                    return False
                pos = pos+1
            else:
                pos=pos+all_ele[i]
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    word = "internationalization"
    abbr = "i12iz4n"
    word='substitution'
    abbr='s55n'
    print(solution.validWordAbbreviation(word,abbr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
