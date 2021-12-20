# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def simplify(self,expre):
        if expre[0]!='+' and expre[0]!='-':
            expre='+'+expre
        expre=expre+'+'
        cons,var=0,0
        cur_exp=''
        for i in range(len(expre)):
            if expre[i]=='+' or expre[i]=='-':
                if len(cur_exp)>0:
                    if cur_exp[-1]=='x':
                        if len(cur_exp)==2:
                            var=var+eval(cur_exp[:-1]+'1')
                        else:
                            var=var+eval(cur_exp[:-1])
                    else:
                        cons=cons+eval(cur_exp)
                cur_exp=expre[i]
            else:
                cur_exp=cur_exp+expre[i]
        return cons,var

    def solveEquation(self, equation: str) -> str:
        parts=equation.split('=')
        parts=[self.simplify(i) for i in parts]
        var=parts[0][1]-parts[1][1]
        cons=parts[1][0]-parts[0][0]
        if var==0 and cons!=0:
            return 'No solution'
        if var==0 and cons==0:
            return 'Infinite solutions'
        else:
            return cons/var


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    equation = "x+5-3+3x=6+x-2"
    solution=Solution()
    print(solution.solveEquation(equation))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
