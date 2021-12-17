# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def frequencySort(self, s: str) -> str:
        dic={}
        all=[]
        for i in s:
            if i in dic:
                dic[i]=dic[i]+1
            elif i not in dic:
                dic[i]=1
                all.append(i)
        all=sorted(all,key=lambda x:dic[x],reverse=True)
        results=''
        for i in all:
            results=results+i*dic[i]
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s="tree"
    solution=Solution()
    print(solution.frequencySort(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
