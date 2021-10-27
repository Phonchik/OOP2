class Account:
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    def __set_amount(self,amount):
        if amount >= 0:
            self.__amount = amount

    def transfer(self, other, to_transfer):
        if self.__amount - to_transfer >= 0:
            self.__amount -= to_transfer
            other.__amount += to_transfer

    #@amount.setter
    #def amount(self):
    #   self.__amount = amount


nick = Account(50)
mike = Account(150)

nick.transfer(mike, 50)

print(nick.amount, mike.amount)
