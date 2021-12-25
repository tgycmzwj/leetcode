# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter=Counter(s)
        leng=len(s)
        pos=0
        results=['']*leng
        for k in sorted(counter,key=counter.get,reverse=True):
            if counter[k]>leng//2+(leng)%2:
                return ""
            for j in range(counter[k]):
                if pos>=leng:
                    pos=1
                results[pos]=k
                pos=pos+2
        return ''.join(results)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "aab"
    solution=Solution()
    print(solution.reorganizeString(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
