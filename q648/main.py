# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(' ')
        for i in range(len(sentence)):
            for j in dictionary:
                if sentence[i].startswith(j):
                    sentence[i] = j
        return ' '.join(sentence)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dictionary = ["cat","bat","rat"]
    sentence = "the cattle was rattled by the battery"
    solution=Solution()
    print(solution.replaceWords(dictionary,sentence))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
