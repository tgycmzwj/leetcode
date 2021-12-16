# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars)==1:
            return chars
        results=[]
        cur_char=chars[0]
        counter=1
        for i in range(1,len(chars)):
            if chars[i]==cur_char:
                counter=counter+1
            else:
                results.append(cur_char)
                if counter>1:
                    results.append(str(counter))
                cur_char=chars[i]
                counter=1
        results.append(cur_char)
        if counter>1:
            results.append(str(counter))
        return len(''.join(results))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chars = ["a","a","a","b","b","a","a"]
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    chars = ["a"]
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    solution=Solution()
    print(solution.compress(chars))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
