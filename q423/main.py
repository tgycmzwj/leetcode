# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def originalDigits(self, s: str) -> str:
        dic={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
        dic={3: 'three', 9: 'nine'}
        s=list(s)
        results={}
        for i in range(10):
            results[i]=0
        results[0]=s.count('z')
        results[2]=s.count('w')
        results[6]=s.count('x')
        results[8]=s.count('g')
        results[4]=s.count('u')
        results[1]=s.count('o')-results[0]-results[2]-results[4]
        results[5]=s.count('f')-results[4]
        results[7]=s.count('v')-results[5]
        results[3]=s.count('r')-results[0]-results[4]
        results[9]=s.count('i')-results[5]-results[6]-results[8]
        output=''
        for i in range(10):
            output=output+str(i)*results[i]
        return output







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s = "owoztneoer"
    solution=Solution()
    print(solution.originalDigits(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
