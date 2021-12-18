# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class StringIterator:
    def __init__(self, csr: str):
        self.numlist = []
        self.charlist = []
        self.charindex = []
        self.pointer = 0
        for i in range(len(csr)):
            if csr[i].isalpha():
                self.charlist.append(csr[i])
                self.charindex.append(i)
        self.charindex.append(len(csr))
        for j in range(len(self.charindex)-1):
            self.numlist.append(int(csr[self.charindex[j]+1:self.charindex[j+1]]))
    def next(self) -> str:
        if self.pointer >= len(self.numlist):
            return " "
        elif self.numlist[self.pointer] > 1:
            self.numlist[self.pointer] -= 1
            return self.charlist[self.pointer]
        else:
            self.pointer += 1
            return self.charlist[self.pointer-1]
    def hasNext(self) -> bool:
        if self.pointer > len(self.numlist) -1:
            return False
        elif self.pointer == len(self.numlist) -1:
            return self.numlist[self.pointer] > 0
        else:
            return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
    vals=[["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
