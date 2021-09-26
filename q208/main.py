# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Trie:

    def __init__(self):
        self.set1 = set()
        self.set2 = set()
    def insert(self, word: str) -> None:
        self.set1.add(word)
        for i in range(len(word)):
            self.set2.add(word[:i+1])
    def search(self, word: str) -> bool:
        if word in self.set1:
            return True
        else:
            return False
    def startsWith(self, prefix: str) -> bool:
        if prefix in self.set2:
            return True
        else:
            return False


if __name__ == '__main__':
    cmds_content=["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    cmds_value=[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    results=[]
    for i in range(len(cmds_content)):
        cmd_content=cmds_content[i]
        cmd_value=cmds_value[i]
        if cmd_content=='Trie':
            obj=Trie()
            results.append(None)
        elif cmd_content=='insert':
            results.append(obj.insert(cmd_value[0]))
        elif cmd_content=='search':
            results.append(obj.search(cmd_value[0]))
        elif cmd_content=='startsWith':
            results.append(obj.startsWith(cmd_value[0]))
    print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
