# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class MapSum:
    def __init__(self):
        self.map = {}
    def insert(self, key: str, val: int) -> None:
        self.map[key] = val
    def sum(self, prefix: str) -> int:
        s, l = 0, len(prefix)
        for k in self.map.keys():
            if l > len(k):
                continue
            elif prefix == k[0:l]:
                s += self.map[k]
        return s

    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["MapSum", "insert", "sum", "insert", "sum"]
    vals=[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
