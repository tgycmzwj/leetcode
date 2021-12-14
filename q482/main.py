# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def licenseKeyFormatting_other(self, s: str, k: int) -> str:
        all_ele=s.split('-')
        results=[]
        cur=''
        for i in range(len(all_ele)):
            if len(cur+all_ele[i])>k:
                results.append(cur)
                cur=all_ele[i]
            else:
                cur=cur+all_ele[i]
        results.append(cur)
        results=[i.upper() for i in results if i!='']
        return '-'.join(results)

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        keys = "".join(s.split("-")).upper()
        startSize = len(keys) % k
        res = []
        if startSize != 0:
            res.append(keys[:startSize])
        for index in range(startSize, len(keys), k):
            res.append(keys[index:index + k])
        return "-".join(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "5F3Z-2e-9-w"
    k = 4
    solution=Solution()
    print(solution.licenseKeyFormatting(s,k))




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
