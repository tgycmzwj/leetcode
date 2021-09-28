# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(' ','')
        if len(s)==0:
            return 0
        delimiter=[]
        for i in s:
            if i.isdigit()==False:
                delimiter.append(i)
        s=s.replace('-','+')
        s=s.replace('*','+')
        s=s.replace('/','+')
        s=s.split('+')
        new_s=[]
        for i in range(len(delimiter)):
            new_s.append(s[i])
            new_s.append(delimiter[i])
        new_s.append(s[-1])
        s=new_s
        results=0
        stack=[]
        while len(s)!=0:
            cur_ele=s.pop(0)
            if cur_ele=='*':
                temp=stack.pop(-1)
                stack.append(int(temp)*int(s.pop(0)))
            elif cur_ele=='/':
                temp=stack.pop(-1)
                stack.append(int(int(temp)/int(s.pop(0))))
            else:
                stack.append(cur_ele)
        results=float(stack[0])
        for i in range(2,len(stack),2):
            if stack[i-1]=='+':
                results=results+int(stack[i])
            else:
                results=results-int(stack[i])
        return int(results)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = " 3+5 / 2 "
    s = "3+2*2"
    #s = " 32/2 "
    solution=Solution()
    print(solution.calculate(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
