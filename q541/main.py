# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        results=''
        counter=0
        while len(s)>k:
            cur_str=s[:k]
            if counter%2==0:
                results=results+cur_str[::-1]
            else:
                results=results+cur_str
            counter=counter+1
            s=s[k:]
        if counter%2==0:
            results=results+s[::-1]
        else:
            results=results+s
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    solution=Solution()
    print(solution.reverseStr(s,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
