# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def sorting_key(self,log):
        if log[-1].isnumeric():return (1,)
        identifier,content=log.split(" ", 1)
        return (0,content,identifier)
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key=self.sorting_key)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    solution=Solution()
    print(solution.reorderLogFiles(logs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
