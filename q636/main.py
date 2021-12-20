# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        results=[0]*n
        prev_start_time=0
        stack=[]
        for i in range(len(logs)):
            job_desc=logs[i].split(':')  #id,start/end,time
            job_desc[0],job_desc[2]=int(job_desc[0]),int(job_desc[2])
            if job_desc[1]=='start':
                if stack:
                    results[stack[-1][0]]=results[stack[-1][0]]+(job_desc[2]-prev_start_time)
                stack.append(job_desc.copy())
                prev_start_time=job_desc[2]
            elif job_desc[1]=='end':
                last_job=stack.pop()
                results[last_job[0]]+=job_desc[2]-prev_start_time+1
                prev_start_time=job_desc[2]+1
        return results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 2
    logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
    solution=Solution()
    print(solution.exclusiveTime(n,logs))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
