from copy import deepcopy
class MyQueue:

    def __init__(self):
        self._values = []

    def push(self, x: int) -> None:
        self._values.append(x)

    def pop(self) -> int:
        return self._values.pop(0)
    
    def peek(self) -> int:
        return deepcopy(self._values[0])

    def empty(self) -> bool:
        return len(self._values) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()