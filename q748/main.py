# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        plate = {}
        for i in licensePlate:
            if i.isalpha():
                if i.lower() not in plate:
                    plate[i.lower()] = 1
                else:
                    plate[i.lower()] = plate[i.lower()] + 1
        words.sort(key=len)
        for i in words:
            x = 1
            for j in plate.keys():
                if (j not in i) or (plate[j] > i.count(j)):
                    x = 0
                    break

            if (x == 1):
                return (i)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    licensePlate = "1s3 PSt"
    words = ["step","steps","stripe","stepple"]
    solution=Solution()
    print(solution.shortestCompletingWord(licensePlate,words))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
