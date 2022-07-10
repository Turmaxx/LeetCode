class MyHashMap:

    def __init__(self):
        self._values = {}

    def put(self, key: int, value: int) -> None:
        self._values[key] = value

    def get(self, key: int) -> int:
        if key in self._values: return self._values[key]
        return -1

    def remove(self, key: int) -> None:
        if key in self._values: del self._values[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)