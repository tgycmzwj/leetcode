# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Iterator:
    def __init__(self, nums):
        self.i=0
        self.nums=nums
        self.length=len(nums)
    def hasNext(self):
        if self.i<self.length-1:
            return True
        return False
    def next(self):
        self.i=self.i+1
        return self.nums[self.i]

class PeekingIterator(object):
    def __init__(self, iterator):
        self.iter = iterator
        self.temp = self.iter.next() if self.iter.hasNext() else None
    def peek(self):
        return self.temp
    def next(self):
        ret = self.temp
        self.temp = self.iter.next() if self.iter.hasNext() else None
        return ret
    def hasNext(self):
        return self.temp is not None
