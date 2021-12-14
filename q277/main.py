# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def findCelebrity(self, n: int, graph) -> int:
        results=[sum(i) for i in graph]
        for i in range(len(results)):
            if results[i]==1:
                return i
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    graph = [[1,1,0],[0,1,0],[1,1,1]]
    n=3
    solution=Solution()
    print(solution.findCelebrity(n,graph))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
