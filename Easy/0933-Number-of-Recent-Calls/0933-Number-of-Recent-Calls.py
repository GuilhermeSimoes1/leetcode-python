class RecentCounter:

    def __init__(self):
        self.aux = []
        self.count = 0

    def ping(self, t: int) -> int:
        self.count = 0
        self.aux.append(t)

        while self.aux and self.aux[0] < t - 3000:
            self.aux.pop(0)

        return len(self.aux)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)