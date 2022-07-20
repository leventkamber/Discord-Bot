from exercise1 import Bill


class BatchBill:
    def __init__(self, list_of_bills):
        self.list_of_bills = list_of_bills

    def __len__(self):
        return len(self.list_of_bills)

    def total(self):
        total = 0
        for bill in self.list_of_bills:
            total += bill.amount
        return total

    def __getitem__(self, index):
        return self.list_of_bills[index]


values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

# print(f"Total: {batch.total()}\n")

# for i in range(len(batch)):
#    print(batch[i])
