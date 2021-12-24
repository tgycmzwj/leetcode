# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import collections
class NestedIterator(object):
    def __init__(self, nestedList):
        self.queue = collections.deque(nestedList)
    def next(self):
        return self.queue.popleft().getInteger()
    def hasNext(self):
        while self.queue:
            if self.queue[0].isInteger():
                return True
            first = self.queue.popleft()
            self.queue.extendleft(first.getList()[::-1])
        return False

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nestedList = [1,[4,[6]]]
    solution=NestedIterator()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
