# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alphabet=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        results=[]
        for item in words:
            cur_results=''
            for i in item:
                cur_results=cur_results+alphabet[int(ord(i)-ord('a'))]
            if cur_results not in results:
                results.append(cur_results)
        return len(results)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = ["gin","zen","gig","msg"]
    solution=Solution()
    print(solution.uniqueMorseRepresentations(words))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
