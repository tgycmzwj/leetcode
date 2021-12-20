# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        s, banned = set(), [False] * n
        ban_d = ban_r = 0
        while len(s) != 1:
            s = set()
            for i, p in enumerate(senate):
                if banned[i]: continue
                if p == 'R':
                    if ban_r > 0:
                        ban_r -= 1
                        banned[i] = True
                    else:
                        ban_d += 1
                        s.add('R')
                else:
                    if ban_d > 0:
                        ban_d -= 1
                        banned[i] = True
                    else:
                        ban_r += 1
                        s.add('D')
        return 'Radiant' if s.pop() == 'R' else 'Dire'
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    senate = "RDDRDRRDDRRDRRRDDR"
    solution=Solution()
    print(solution.predictPartyVictory(senate))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
