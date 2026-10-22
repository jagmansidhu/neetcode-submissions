from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        self.m = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.m:
            return ""

        inner_dict = self.m.get(key)

        idx = inner_dict.bisect_right(timestamp) - 1

        if idx >= 0:
            # 1 is the value, 0 would be the key/timestamp
            return inner_dict.peekitem(idx)[1]

        return ""

        
