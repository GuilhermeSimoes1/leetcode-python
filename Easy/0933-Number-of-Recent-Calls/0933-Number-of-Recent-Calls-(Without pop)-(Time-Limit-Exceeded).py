class RecentCounter:

    def __init__(self):
        self.aux = []
        self.count = 0

    def ping(self, t: int) -> int:

        self.count = 0
        self.aux.append(t)

        for i in range(len(self.aux)):
            if t - 3000 <= self.aux[i] <= t:
                self.count += 1
        return self.count

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)