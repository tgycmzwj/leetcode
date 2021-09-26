# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1=[int(i) for i in version1.split('.')]
        version2=[int(i) for i in version2.split('.')]
        if len(version1)<len(version2):
            while len(version1)<len(version2):
                version1.append(0)
        if len(version1)>len(version2):
            while len(version1)>len(version2):
                version2.append(0)
        for i in range(len(version1)):
            if version1[i]>version2[i]:
                return 1
            elif version1[i]<version2[i]:
                return -1
        return 0



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    version1 = "1.01"
    version2 = "1.001"
    version1 = "1.0"
    version2 = "1.0.0"
    version1 = "0.1"
    version2 = "1.1"
    version1 = "1.0.1"
    version2 = "1"
    version1 = "7.5.2.4"
    version2 = "7.5.3"
    solution=Solution()
    print(solution.compareVersion(version1,version2))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
