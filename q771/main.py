# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels=set(list(jewels))
        counter=0
        for i in stones:
            if i in jewels:
                counter=counter+1
        return counter

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    jewels = "aA"
    stones = "aAAbbbb"
    solution=Solution()
    print(solution.numJewelsInStones(jewels,stones))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
