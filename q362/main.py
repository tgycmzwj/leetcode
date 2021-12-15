# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class HitCounter:
    def __init__(self):
        self.dic={}
    def hit(self, timestamp: int) -> None:
        if timestamp not in self.dic:
            self.dic[timestamp]=1
        else:
            self.dic[timestamp]=self.dic[timestamp]+1
    def getHits(self, timestamp: int) -> int:
        num=0
        for k,v in self.dic.items():
            if k<=timestamp and k+300>timestamp:
                num=num+v
        return num

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cmds=["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
    vals=[[], [1], [2], [3], [4], [300], [300], [301]]
    results=[]
    for i in range(len(cmds)):
        cmd,val=cmds[i],vals[i]
        if cmd=='HitCounter':
            obj=HitCounter()
            results.append(None)
        elif cmd=='hit':
            results.append(obj.hit(val[0]))
        elif cmd=='getHits':
            results.append(obj.getHits(val[0]))
    print(results)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
