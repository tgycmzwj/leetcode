# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        original_color=image[sr][sc]
        processing=[(sr,sc)]
        processed=[]
        while len(processing)>0:
            cur_ele=processing.pop(0)
            processed.append(cur_ele)
            directions=[(-1,0),(1,0),(0,1),(0,-1)]
            for direc in directions:
                new_x,new_y=cur_ele[0]+direc[0],cur_ele[1]+direc[1]
                if 0<=new_x<len(image) and 0<=new_y<len(image[0]) and (new_x,new_y) not in processed and image[new_x][new_y]==original_color:
                    processing.append((new_x,new_y))
        for item in processed:
            image[item[0]][item[1]]=newColor
        return image

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    solution=Solution()
    print(solution.floodFill(image,sr,sc,newColor))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
