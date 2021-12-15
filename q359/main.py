# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Logger:
    def __init__(self):
        self.dic={}
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.dic:
            self.dic[message]=timestamp
            return True
        else:
            if timestamp-self.dic[message]>=10:
                self.dic[message]=timestamp
                return True
            return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["Logger", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage", "shouldPrintMessage","shouldPrintMessage", "shouldPrintMessage"]
    vals=[[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
