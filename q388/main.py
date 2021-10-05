# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        max_length=0
        broke_input=re.split('\\n',input)
        if len(broke_input)==1 and '.' not in broke_input[0]:
            return 0
        build=[broke_input[0]]
        for i in range(1,len(broke_input)):
            cur_level=broke_input[i].count('\t')
            if cur_level==len(build):
                build.append(broke_input[i])
            else:
                cur_str=re.sub(',+',',',''.join(build).replace('\n','').replace('\t',','))
                if '.' in cur_str:
                    max_length=max(max_length,len(cur_str))
                build=build[:cur_level]+[broke_input[i]]
        if len(build)>1 or build[0]!='dir':
            cur_str = re.sub(',+', ',', ''.join(build).replace('\n', '').replace('\t', ','))
            max_length = max(max_length, len(cur_str))
        return max_length







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    # input="file1.txt\nfile2.txt\nlongfile.txt"
    # input='filetet\nsfa'
    solution=Solution()
    print(solution.lengthLongestPath(input))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
