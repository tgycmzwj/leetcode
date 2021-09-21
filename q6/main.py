# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        cur_row=0
        cur_col=0
        if numRows==1:
            return s
        cur_direction='down'
        wordlist=[[''] * len(s) for i in range(numRows)]
        for i in range(len(s)):
            wordlist[cur_row][cur_col] = s[i]
            if cur_direction=='down':
                if cur_row<=numRows-2:
                    cur_row=cur_row+1
                else:
                    cur_row=cur_row-1
                    cur_col=cur_col+1
                    cur_direction='up'
            else:
                if cur_row>=1:
                    cur_row=cur_row-1
                    cur_col=cur_col+1
                else:
                    cur_row=cur_row+1
                    cur_direction='down'
        output=''
        for row in range(numRows):
            output=output+''.join(wordlist[row][:cur_col+1])
        return output





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    s = "ABC"
    numRows = 1
    print(solution.convert(s,numRows))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
