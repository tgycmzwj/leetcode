# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def numDecodings_slow(self, s: str) -> int:
        counter_old=[]
        counter_new=[]
        if int(s[0])==0:
            return 0
        counter_new.append([s[0]])
        for i in range(1,len(s)):
            counter_old=counter_new
            if int(s[i])!=0:
                if (int(s[i-1])==1) or (int(s[i-1])==2 and int(s[i])<=6):
                    counter_new = [ele + [s[i]] for ele in counter_old]
                    for item in counter_old:
                        if len(item[-1])==1:
                            temp=[item[id] if id!=len(item)-1 else item[id]+s[i] for id in range(len(item))]
                            counter_new.append(temp)
                else:
                    counter_new=[ele + [s[i]] for ele in counter_old]
            else:
                if int(s[i-1])!=1 and int(s[i-1])!=2:
                    return 0
                else:
                    counter_new=[item for item in counter_old if len(item[-1])==1]
                    for item in counter_new:
                        item[-1]=item[-1]+s[i]
        return len(counter_new)
    def numDecodings(self,s:str)->int:
        count_total=[]
        count_1digit=[]
        if int(s[0])==0:
            return 0
        count_total.append(1)
        count_1digit.append(1)
        for i in range(1, len(s)):
            if int(s[i]) != 0:
                if (int(s[i - 1]) == 1) or (int(s[i - 1]) == 2 and int(s[i]) <= 6):
                    count_total.append(count_total[i-1]+count_total[i-2])
                    count_1digit.append(count_total[i-1])
                else:
                    count_total.append(count_total[i-1])
                    count_1digit.append(count_total[i-1])
            else:
                if int(s[i-1])!=1 and int(s[i-1])!=2:
                    return 0
                else:
                    count_total.append(count_1digit[i-1])
                    count_1digit.append(0)
        return count_total[-1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import numpy as np
    solution=Solution()
    random_array=np.random.randint(low=0,high=10000000000000,size=1000)
    for i in random_array:
        print('the string is '+str(i))
        if solution.numDecodings_slow(str(i))!=solution.numDecodings(str(i)):
            print('wrong')
        # print(solution.numDecodings_slow(str(i)))
        # print(solution.numDecodings(str(i)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
