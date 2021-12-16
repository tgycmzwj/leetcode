# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        sentence_len=sum(len(w) for w in sentence)+len(sentence)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sentence = ["hello","world"]
    rows = 2
    cols = 8
    solution=Solution()
    print(solution.wordsTyping(sentence,rows,cols))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
