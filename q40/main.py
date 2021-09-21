from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results={}
        for i in range(0,target+1):
            results[i]=[]
        results[0].append([])
        candidates.sort()
        for i in range(1,target+1):
            for cand in candidates:
                if i-cand<0:
                    break
                else:
                    for existing_comb in results[i-cand]:
                        if existing_comb.count(cand)+1<=candidates.count(cand):
                            to_be_append=existing_comb+[cand]
                            to_be_append.sort()
                            if to_be_append not in results[i]:
                                results[i].append(to_be_append)
        return results[target]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    candidates = [2,5,2,1,2]
    target = 5
    print(solution.combinationSum2(candidates,target))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
