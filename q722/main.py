# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from typing import List

class Solution(object):
    def removeComments(self, source):
        res,buffer,flag=[],'',False
        for line in source:
            i = 0
            while i<len(line):
                char=line[i]
                # "//" -> Line comment.
                if char=='/' and (i+1)<len(line) and line[i+1]=='/' and not flag:
                    i=len(line) # Advance pointer to end of current line.
                # "/*" -> Start of block comment.
                elif char=='/' and (i+1)<len(line) and line[i+1]=='*' and not flag:
                    flag=True
                    i+=1
                # "*/" -> End of block comment.
                elif char=='*' and (i+1)<len(line) and line[i+1]=='/' and flag:
                    flag=False
                    i+=1
                # Normal character. Append to buffer if not in block comment.
                elif not flag:
                    buffer+=char
                i+=1
            if buffer and not flag:
                res.append(buffer)
                buffer=''
        return res


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
    solution=Solution()
    print(solution.removeComments(source))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
