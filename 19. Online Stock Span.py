class StockSpanner:
    # [100, 80, 60, 70, 60, 75, 85]
    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price: int) -> int:
        i = len(self.prices) - 1
        while i >= 0 and self.prices[i] <= price:
            span = self.spans[i]
            i = i - span
        self.prices.append(price)
        span = len(self.prices) - 1 - i
        self.spans.append(span)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
