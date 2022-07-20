class Bill:
    def __init__(self, amountt):
        if amountt < 0:
            raise ValueError("Error")
        if not isinstance(amountt, int):
            raise TypeError("Error")
        self.amount = amountt

    def __str__(self) -> str:
        my_str = "A " + str(self.amount) + "$ bill"
        return my_str

    def __repr__(self) -> str:
        return str(self.amount)

    def __int__(self):
        return int(self.amount)

    def __eq__(self, bill) -> bool:
        return self.amount == bill.amount

    def __hash__(self) -> int:
        return hash(self.amount)


a, b, c = Bill(10), Bill(5), Bill(10)
"""
print(int(a))
print(a)
print(str(a))
print(a==b)
print(a==c)
print(hash(c))
"""
