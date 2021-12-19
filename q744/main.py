# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters=set(letters)
        results='abcdefghijklmnopqrstuvwxyz'
        target_index=results.index(target)
        results=results[target_index+1:]+results[:target_index+1]
        for i in results:
            if i in letters:
                return i

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    letters = ["c","f","j"]
    target = "a"
    solution=Solution()
    print(solution.nextGreatestLetter(letters,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
