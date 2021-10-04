# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull_collector=[]
        secret,guess=list(secret),list(guess)
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bull_collector.append(i)
        secret,guess=[secret[i] for i in range(len(secret)) if i not in bull_collector],[guess[i] for i in range(len(secret)) if i not in bull_collector]
        cow_dict={}
        for i in secret:
            if i not in cow_dict.keys():
                cow_dict[i]=[1,0]
            else:
                cow_dict[i][0]=cow_dict[i][0]+1
        for i in guess:
            if i not in cow_dict.keys():
                cow_dict[i]=[0,1]
            else:
                cow_dict[i][1]=cow_dict[i][1]+1
        cow_counter=0
        for key in cow_dict.keys():
            cow_counter=cow_counter+min(cow_dict[key])
        return str(len(bull_collector))+'A'+str(cow_counter)+'B'




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    secret = "1"
    guess = "0"
    # secret = "1123"
    # guess = "0111"
    secret = "1"
    guess = "1"
    secret = "1807"
    guess = "7810"
    solution=Solution()
    print(solution.getHint(secret,guess))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
