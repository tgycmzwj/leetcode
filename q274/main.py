# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
from typing import List
class Solution:
    def helper(self,citations,cite_min,cite_max)->int:
        mid=(cite_min+cite_max)//2
        cur_cut=[citation>=mid for citation in citations]
        if sum(cur_cut)==mid:
            return mid
        elif sum(cur_cut)<mid:
            return self.helper(citations,cite_min,mid-1)
        else:
            if sum([citation>=mid+1 for citation in citations])<mid+1:
                return mid
            return self.helper(citations,mid+1,cite_max)
    def hIndex(self, citations: List[int]) -> int:
        cite_max=max(citations)
        h=self.helper(citations,0,cite_max)
        return h




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    citations = [3,0,6,1,5]
    citations = [1, 3, 1]
    solution=Solution()
    print(solution.hIndex(citations))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
