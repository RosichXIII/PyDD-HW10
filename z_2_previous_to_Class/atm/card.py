class Card:

    def __init__(self, name, password):
        self.name = name
        self.__password = password
        self.card_balance = 0
        self.operations_count = 0

    def get_password(self):
        return self.__password