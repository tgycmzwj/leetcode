# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic={}
        for i in range(len(cpdomains)):
            cur_ele=cpdomains[i].split(' ')
            domains=cur_ele[1].split('.')
            for i in range(-len(domains),0):
                cur_domain='.'.join(domains[i:])
                if cur_domain not in dic:
                    dic[cur_domain]=0
                dic[cur_domain]+=int(cur_ele[0])
        results=[]
        for k,v in dic.items():
            results.append(str(v)+' '+k)
        return results



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    solution=Solution()
    print(solution.subdomainVisits(cpdomains))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
