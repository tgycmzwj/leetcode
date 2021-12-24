# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class MyCalendarTwo(object):
    def __init__(self):
        self.calendar =[]
        self.overlap =[]
    def book (self, start, end):
        for i, j in self.overlap:
            if start < j and end > i:
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlap.append((max(start, i), min(end, j)))
        self.calendar.append((start, end))
        return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
    vals=[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
