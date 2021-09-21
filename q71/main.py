# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Solution:
    def simplifyPath(self, path: str) -> str:
        splitted = path.split("/")
        res = []
        skip = [".", "", ".."]
        for p in splitted:
            if p not in skip:
                # add all te folders to the result
                res.append(p)
            if p == "..":
                # go back one level
                if len(res) > 0:
                    # /../ case should always go back to root
                    res.pop()
        return "/" + "/".join(res)


    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution=Solution()
    path = "/a/./b/../../c/"
    print(solution.simplifyPath(path))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
