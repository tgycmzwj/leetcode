# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Solution:
    def nextGreaterElement(self, num) -> None:
        nums=[int(i) for i in list(str(num))]
        problematic_loc=len(nums)+1
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1]>nums[i]:
                problematic_loc=i
                break
        if problematic_loc<len(nums)+1:
            exchange_loc=len(nums)+1
            for i in range(len(nums)-1,problematic_loc,-1):
                if nums[i]>nums[problematic_loc]:
                    exchange_loc=i
                    break
            temp=nums[problematic_loc]
            nums[problematic_loc]=nums[exchange_loc]
            nums[exchange_loc]=temp
            nums[problematic_loc+1:]=nums[problematic_loc+1:][::-1]
        if problematic_loc==len(nums)+1:
            nums.reverse()
        nums=int(''.join([str(i) for i in nums]))
        if nums>num and nums<=pow(2,31)-1:return nums
        return -1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    n = 21
    solution=Solution()
    print(solution.nextGreaterElement(n))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
