# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def romanToInt(self, s: str) -> int:
        s=s+'$$'
        results=0
        while len(s)>=2:
            if s[0]=='I':
                if s[1]=='V':
                    results=results+4
                    s=s[2:]
                elif s[1]=='X':
                    results=results+9
                    s=s[2:]
                else:
                    results=results+1
                    s=s[1:]
            elif s[0]=='X':
                if s[1]=='L':
                    results=results+40
                    s=s[2:]
                elif s[1]=='C':
                    results=results+90
                    s=s[2:]
                else:
                    results=results+10
                    s=s[1:]
            elif s[0]=='C':
                if s[1]=='D':
                    results=results+400
                    s=s[2:]
                elif s[1]=='M':
                    results=results+900
                    s=s[2:]
                else:
                    results=results+100
                    s=s[1:]
            elif s[0]=='V':
                results=results+5
                s=s[1:]
            elif s[0]=='L':
                results=results+50
                s=s[1:]
            elif s[0]=='D':
                results=results+500
                s=s[1:]
            elif s[0]=='M':
                results=results+1000
                s=s[1:]
            else:
                break
        return results




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    s= "DCXXI"
    print(solution.romanToInt(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
