

class Solution:
    def decodeString(self, s: str) -> str:
        string_stack=[]
        i=0
        while i<len(s):
            cur_num=''
            while s[i] in '0123456789' and i<len(s):
                cur_num=cur_num+s[i]
                i=i+1
            if cur_num!='':
                string_stack.append(cur_num)
            if s[i]==']':
                left_bracket_index=len(string_stack) - 1 - string_stack[::-1].index('[')
                num_repeat=left_bracket_index-1
                com_string=''.join(string_stack[left_bracket_index+1:])*int(string_stack[num_repeat])
                string_stack=string_stack[:num_repeat]+[com_string]
                i=i+1
            else:
                string_stack.append(s[i])
                i=i+1
        return ''.join(string_stack)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    s = "3[a2[c]]"
    s = "3[a]2[bc]"
    s = "2[abc]3[cd]ef"
    s = "abc3[cd]xyz"
    s = "11[leetcode]"
    print(solution.decodeString(s))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
