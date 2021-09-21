class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_loc=0
        max_length=0
        cur_length=0
        cur_string=''
        for i in range(len(s)):
            cur_string=s[i]
            for j in range(i+1,len(s)):
                if cur_string.find(s[j])==-1:
                    cur_string=cur_string+s[j]
                else:
                    break
            cur_length=len(cur_string)
            if max_length<cur_length:
                max_length=cur_length
                max_loc=i
        return max_length

if __name__=='__main__':
    solution=Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))