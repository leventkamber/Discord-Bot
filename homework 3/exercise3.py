from exercise2 import Bill, BatchBill


class CashDesk:
    def __init__(self):
        self.dic_of_batches = {}

    def take_money(self, money):
        if isinstance(money, BatchBill):
            for bill in money:
                if self.dic_of_batches.get(int(bill)) is None:
                    self.dic_of_batches[int(bill)] = 0
                self.dic_of_batches[int(bill)] += 1
        else:
            if self.dic_of_batches.get(int(money)) is None:
                self.dic_of_batches[int(money)] = 0
            self.dic_of_batches[int(money)] += 1

    def total(self):
        total = 0
        for key, value in self.dic_of_batches.items():
            total += key * value
        return total

    def inspect(self):
        for key, value in self.dic_of_batches.items():
            print(f"{key}$ bills - {value}")

    def draw_amount(self, amount):
        total_amount = self.total()
        if amount > total_amount:
            print("Negative balance")

#    def draw_bills(self, dic):


values = [10, 20, 50, 100, 100, 100]

bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()
desk.take_money(batch)
desk.take_money(Bill(10))
print(desk.total())
desk.inspect()
print(desk.draw_amount(30))
