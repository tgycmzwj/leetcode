# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class RecentCounter:
    def __init__(self):
        self.counter=[]
    def ping(self, t: int) -> int:
        while self.counter and self.counter[0]+3000<t:
            self.counter.pop(0)
        self.counter.append(t)
        return len(self.counter)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["RecentCounter", "ping", "ping", "ping", "ping"]
    vals=[[], [1], [100], [3001], [3002]]


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
