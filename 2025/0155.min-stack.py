"""
设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

"""


class MinStack:

    def __init__(self):
        self.orig_arr = []
        self.size = 0
        self.heap_arr = []

    def push(self, val: int) -> None:
        self.orig_arr.append(val)
        self.size += 1

        if not self.heap_arr or val <= self.heap_arr[-1]:
            self.heap_arr.append(val)

    def pop(self) -> None:
        val = self.orig_arr.pop()
        self.size -= 1
        if val == self.heap_arr[-1]:
            return self.heap_arr.pop()
        return val

    def top(self) -> int:
        return self.orig_arr[-1]

    def getMin(self) -> int:
        return self.heap_arr[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(7)
    obj.push(9)
    obj.push(8)
    obj.push(1)
    obj.push(5)
    obj.push(4)
    obj.push(3)
    obj.push(2)
    obj.push(9)
    obj.push(8)
    print(obj)
