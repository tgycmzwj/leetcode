# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def nthUglyNumber(self,n:int)->int:
        results=[1]
        cur_len=1
        i2,i3,i5=0,0,0
        while cur_len<n:
            factor2,factor3,factor5=results[i2]*2,results[i3]*3,results[i5]*5
            cur_min=min(factor2,factor3,factor5)
            if factor2==cur_min:
                results.append(factor2)
                i2=i2+1
            if factor3==cur_min:
                if factor3!=results[-1]:
                    results.append(factor3)
                i3=i3+1
            if factor5==cur_min:
                if factor5!=results[-1]:
                    results.append(factor5)
                i5=i5+1
            cur_len=cur_len+1
        return results[-1]



    def nthUglyNumber_slow(self, n: int) -> int:
        ori_member=[1,2,3,4,5]
        factors=[2,3,5]
        if n<=5:
            return ori_member[n-1]
        cur_length=5
        for i in range(6,2**n):
            print('i=',i)
            print('len=',cur_length)
            if ((i%2==0) and (i//2 in ori_member)):
                cur_length=cur_length+1
                ori_member.append(i)
            elif ((i%3==0) and (i//3 in ori_member)):
                cur_length=cur_length+1
                ori_member.append(i)
            elif ((i%5==0) and (i//5 in ori_member)):
                cur_length=cur_length+1
                ori_member.append(i)

            if cur_length==n:
                return ori_member[n-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n=1690
    solution=Solution()
    print(solution.nthUglyNumber(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
