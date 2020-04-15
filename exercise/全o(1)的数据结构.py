from collections import OrderedDict


class AllOne(OrderedDict):

    def __init__(self):
        pass

    def inc(self, key: str) -> None:
        if key in self:
            self[key] += 1
        else:
            self[key] = 1

    def dec(self, key: str) -> None:
        if key in self:
            if self[key] == 1:
                self.popitem(key)
            else:
                self[key] -= 1

    def getMaxKey(self) -> str:
        self.

    def getMinKey(self) -> str:
        pass


# Your AllOne object will be instantiated and called as such:
obj = AllOne()
# obj.inc(key)
# obj.dec(key)
obj.inc('hello')
param_3 = obj.getMaxKey()
param_4 = obj.getMinKey()
