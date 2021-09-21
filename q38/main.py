class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        number=self.countAndSay(n-1)
        results=''
        cur_element=number[0]
        count=1
        for j in range(1,len(number)):
            if number[j]==cur_element:
                count=count+1
            else:
                results=results+str(count)+str(cur_element)
                count = 1
                cur_element=number[j]
        results += str(count) + cur_element
        return results

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    example=4
    print(solution.countAndSay(example))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
