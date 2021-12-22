# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Solution:
    def geClosest(self,s):
        return min(['00','11','22','33','44','55','66','77','88','99','aa','bb','cc','dd','ee','ff'], key=lambda x: abs(int(s,16)-int(x,16)))
    def similarRGB(self, color):
        res = [self.geClosest(color[i:i + 2]) for i in range(1, len(color), 2)]
        return '#' + ''.join(res)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    color = "#09f166"
    solution=Solution()
    print(solution.similarRGB(color))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
