class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if len(s)==0:
            return 0
        negative_flag=False
        cur_num=0
        if (s[0]=='-'):
            s=s[1:]
            negative_flag=True
        elif (s[0]=='+'):
            s=s[1:]
        for i in s:
            if i.isnumeric()==False:
                break
            else:
                cur_num=cur_num*10+int(i)
        if negative_flag==True:
            cur_num=-cur_num
        if cur_num>2147483647:
            return 2147483647
        if cur_num<-2147483648:
            return -2147483648
        return cur_num

if __name__=='__main__':
    solution=Solution()
    example='42'
    print(solution.myAtoi(example))