# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def transform(self,stri):
        results=[]
        counter=0
        for i in range(1,len(stri)):
            if stri[i]!=stri[i-1]:
                results.append([stri[i-1],counter])
                counter=1
            else:
                counter=counter+1
        return results
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name,typed='$'+name+'$','$'+typed+'$'
        name,typed=self.transform(name),self.transform(typed)
        if len(name)!=len(typed):return False
        for i in range(len(name)):
            if name[i][0]==typed[i][0] and name[i][1]<=typed[i][1]:
                continue
            else:
                return False
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = "alex"
    typed = "aaleex"
    solution=Solution()
    print(solution.isLongPressedName(name,typed))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
