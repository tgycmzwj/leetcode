# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class MyCalendar:
    def __init__(self):
        self.intervals = []
    def book(self, start, end):
        for s, e in self.intervals:
            if start < e and end > s: return False
        self.intervals.append((start, end))
        return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["MyCalendar", "book", "book", "book"]
    vals=[[], [10, 20], [15, 25], [20, 30]]
    results=[]
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
