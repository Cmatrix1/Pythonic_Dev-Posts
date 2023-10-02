

class Stock:
    def __init__(self, symbol, date, open, high, low, close, volume):
        self.symbol = symbol
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
    
    def __repr__(self) -> str:
        return f"Stock({self.symbol})"

class Trade:
    def __init__(self, symbol, timestamp, order, price, commission, volume):
        self.symbol = symbol
        self.timestamp = timestamp
        self.order = order
        self.price = price
        self.commission = commission
        self.volume = volume

    def __repr__(self) -> str:
        return f"Trade({self.symbol})"

