# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            for j in range(len(image[0]) // 2):
                image[i][j], image[i][len(image[0]) - 1 - j] = image[i][len(image[0]) - 1 - j], image[i][j]
        for i in range(len(image)):
            for j in range(len(image[0])):
                image[i][j] = 1 - image[i][j]
        return image


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    solution=Solution()
    print(solution.flipAndInvertImage(image))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
