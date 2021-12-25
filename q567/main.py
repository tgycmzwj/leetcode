# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):return False
        counter_s1,counter_s2=[0]*26,[0]*26
        for i in range(len(s1)):
            counter_s1[ord(s1[i])-ord('a')]+=1
            counter_s2[ord(s2[i])-ord('a')]+=1
        results=False
        if counter_s1==counter_s2:
            return True
        for i in range(len(s1),len(s2)):
            counter_s2[ord(s2[i])-ord('a')]+=1
            counter_s2[ord(s2[i-len(s1)])-ord('a')]-=1
            if counter_s1==counter_s2:
                return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    solution=Solution()
    print(solution.checkInclusion(s1,s2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
