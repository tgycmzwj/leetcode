# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class MyHashSet:
    def __init__(self):
        self.set=set()
    def add(self, key: int) -> None:
        self.set.add(key)
    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set.remove(key)
    def contains(self, key: int) -> bool:
        return key in self.set


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
    vals=[[], [1], [2], [1], [3], [2], [2], [2], [2]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
