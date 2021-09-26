# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
import collections
class Solution:
    # @param s, a string
    # @return a list of strings
    def findRepeatedDnaSequences(self, s):
        sequences = collections.defaultdict(int)
        for i in range(len(s)):
            sequences[s[i:i+10]] += 1
        return [key for key, value in sequences.items() if value > 1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s =  "AAAAAAAAAAA"
    solution=Solution()
    print(solution.findRepeatedDnaSequences(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
