# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class MyHashMap:
    def __init__(self):
        self.dic={}
    def put(self, key: int, value: int) -> None:
        self.dic[key]=value
    def get(self, key: int) -> int:
        if key in self.dic:
            return self.dic[key]
        return -1
    def remove(self, key: int) -> None:
        if key in self.dic:
            del self.dic[key]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
    vals=[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
