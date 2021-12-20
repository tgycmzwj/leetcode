# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def magicalString(self, n: int) -> int:
        s=['1','2','2']
        pt_c=2
        pt_s=2
        old_s='2'
        while len(s)<n:
            new_s='1' if old_s=='2' else '2'
            if s[pt_c]=='1':
                s.append(new_s)
                pt_s=pt_s+1
            else:
                s.append(new_s)
                s.append(new_s)
                pt_s=pt_s+2
            pt_c=pt_c+1
            old_s=s[-1]
        return s[:n].count('1')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 6
    n=89999
    solution=Solution()
    print(solution.magicalString(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
