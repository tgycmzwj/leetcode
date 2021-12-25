# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class LogSystem(object):
    def __init__(self):
        self.logs = []
    def put(self, tid, timestamp):
        self.logs.append((tid, timestamp))
    def retrieve(self, s, e, gra):
        index = {'Year': 5, 'Month': 8, 'Day': 11,
                 'Hour': 14, 'Minute': 17, 'Second': 20}[gra]
        start = s[:index]
        end = e[:index]
        return sorted(tid for tid, timestamp in self.logs if start <= timestamp[:index] <= end)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["LogSystem", "put", "put", "put", "retrieve", "retrieve"]
    vals=[[], [1, "2017:01:01:23:59:59"], [2, "2017:01:01:22:59:59"], [3, "2016:01:01:00:00:00"],
     ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"], ["2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
