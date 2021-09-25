# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import collections
class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    # @return an integer
    def get(self, key):
        if not key in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds_name=["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    cmds_value=[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    return_list=[]
    for i in range(len(cmds_name)):
        cmd_name,cmd_value=cmds_name[i],cmds_value[i]
        if cmd_name=='LRUCache':
            obj=LRUCache(cmd_value[0])
            return_list.append(None)
        elif cmd_name=='put':
            return_list.append(obj.put(cmd_value[0],cmd_value[1]))
        elif cmd_name=='get':
            return_list.append(obj.get(cmd_value[0]))
    print(return_list)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
