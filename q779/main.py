# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        if N == 1:
            return 0
        else:
            if K % 2 == 0:
                # even index of current level is opposite of parent level's [(K+1)//2]
                return 1 - self.kthGrammar(N-1, (K+1)//2)
            else:
                # odd index of current level is the same as parent level's [(K+1)//2]
                return self.kthGrammar(N-1, (K+1)//2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 2
    k = 1
    solution=Solution()
    print(solution.kthGrammar(n,k))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
