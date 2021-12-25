# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def search(self, reader, target):
        l, r = 0, 10000
        while l <= r:
            mid = (l + r) // 2
            val = reader.get(mid)
            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    secret = [-1, 0, 3, 5, 9, 12]
    target = 9
    solution=Solution()
    print(solution.search(secret,target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
