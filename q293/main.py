# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        results=[]
        for i in range(len(currentState)-1):
            if currentState[i]=='+' and currentState[i+1]=='+':
                results.append(currentState[:i]+'--'+currentState[i+2:])
        return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    currentState = "++++"
    solution=Solution()
    print(solution.generatePossibleNextMoves(currentState))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
