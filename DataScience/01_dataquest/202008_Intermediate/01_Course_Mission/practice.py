class MyBankBalance():

    def __init__(self, total_amount):
        self.bank_balance = total_amount
        self.string_format()

    def string_format(self):
        self.balance_format = "${:,.2f}".format(self.bank_balance) 


    def add_value(self, value):
        self.bank_balance += value
        self.string_format()

balance = MyBankBalance(5000)
print(balance.balance_format)