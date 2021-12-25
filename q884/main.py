# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
import collections
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        return [k for k, v in collections.Counter(A.split() + B.split()).items() if v == 1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s1 = "this apple is sweet"
    s2 = "this apple is sour"
    solution=Solution()
    print(solution.uncommonFromSentences(s1,s2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
