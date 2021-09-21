# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def isInterleave_recursive(self,s1:str,s2:str,s3:str)->bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        return self.isInterleave_helper(s1,s2,s3)==1
    def isInterleave_recursive_helper(self, s1: str, s2: str, s3: str) -> int:
        print(len(s3))
        if s1+s2==s3:
            return 1
        if s1=="":
            if s2!=s3:
                return 0
        if s2=="":
            if s1!=s3:
                return 0
        if s1[0]==s3[0] and s2[0]!=s3[0]:
            return self.isInterleave(s1[1:],s2,s3[1:])
        elif s1[0]!=s3[0] and s2[0]==s3[0]:
            return self.isInterleave(s1,s2[1:],s3[1:])
        elif s1[0]!=s3[0] and s2[0]!=s3[0]:
            return 0
        else:
            return max(self.isInterleave(s1[1:],s2,s3[1:]),self.isInterleave(s1,s2[1:],s3[1:]))

    def isInterleave(self,s1:str,s2:str,s3:str)->bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        if len(s1)==len(s3):
            return s1==s3
        if len(s2)==len(s3):
            return s2==s3
        matrix = [[0 for j in range(len(s1) + 1)] for i in range(len(s2) + 1)]
        matrix[0][0]=1
        for i in range(len(matrix[0])):
            if s1[i-1]==s3[i-1] and matrix[0][i-1]==1:
                matrix[0][i]=1
        for j in range(len(matrix)):
            if s2[j-1]==s3[j-1] and matrix[j-1][0]==1:
                matrix[j][0]=1
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):
                if s3[i+j-1]==s1[j-1] and s3[i+j-1]!=s2[i-1]:
                    if matrix[i][j-1]==1:
                        matrix[i][j]=1
                elif s3[i+j-1]==s2[i-1] and s3[i+j-1]!=s1[j-1]:
                    if matrix[i-1][j]==1:
                        matrix[i][j]=1
                elif s3[i+j-1]!=s2[i-1] and s3[i+j-1]!=s1[j-1]:
                    matrix[i][j]=0
                else:
                    if matrix[i][j-1]==1 or matrix[i-1][j]==1:
                        matrix[i][j]=1
        return matrix[i][j]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s1="cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc"
    s2="abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb"
    s3="abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb"
    solution=Solution()
    print('start')
    print(solution.isInterleave(s1,s2,s3))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
