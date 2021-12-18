# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class TwoSum:
    def __init__(self):
        self.num = []
        self.num_set = set()
        self.results = set()
    def add(self, number: int) -> None:
        if number not in self.num_set:
            for i in self.num:
                self.results.add(i + number)
            self.num.append(number)
        else:
            set.results.add(number + number)

    def find(self, value: int) -> bool:
        return value in self.results


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["TwoSum", "add", "add", "add", "find", "find"]
    vals=[[], [1], [3], [5], [4], [7]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
