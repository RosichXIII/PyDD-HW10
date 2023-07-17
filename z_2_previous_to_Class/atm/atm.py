from card import Card

class Atm():

    def __init__(self, card: Card):
        self.__balance_atm = 1_000_000
        self.card = card
        self.__password = int(input("Введите ПИН-код: "))
        if card.get_password() != self.__password:
            print("Введён неверный ПИН-код.")
            exit()

    def refill_account(self):
        refill_amount = int(input("Сумма пополнения счёта: "))
        if refill_amount % 50 == 0:
            self.card.card_balance += refill_amount
            self.__balance_atm += refill_amount
            print("Пополнение прошло успешно.\n")
            self.card.operations_count += 1
            if self.card.operations_count % 3 == 0:
                self.card.card_balance += (refill_amount / 100)*3
                self.__balance_atm -= (refill_amount / 100)*3
        else:
            print("Сумма внесённых денежных средств должна быть кратна 50\n")

    def withdraw_cash(self):
        withdraw_amount = int(input("Сумма снятия наличных: "))
        if withdraw_amount % 50 == 0:
            if withdraw_amount > self.card.card_balance:
                print("На данном счёте недостаточно средств.\n")
            elif withdraw_amount > self.__balance_atm:
                print("Превышен остаток денежных средств в банкомате\n")
                self.card.card_balance -= withdraw_amount
                self.__balance_atm -= withdraw_amount
            elif withdraw_amount > 5_000_000:
                self.card.card_balance -= (withdraw_amount + ((withdraw_amount/100)*10))
                self.__balance_atm -= (withdraw_amount - ((withdraw_amount/100)*10))
                print("Снятие денежных средств прошло успешно\n")
                print(f"Вычтена сумма налога на богатство (10%) : {(withdraw_amount/100)*10}")
                self.card.operations_count += 1
                if self.card.operations_count % 3 == 0:
                    self.card.card_balance += ((withdraw_amount / 100) * 3)
                    self.__balance_atm -= ((withdraw_amount / 100) * 3)
            else:
                if (withdraw_amount / 100) * 1.5 > 30 and (withdraw_amount / 100) * 1.5 < 600:
                    self.card.card_balance -= (withdraw_amount + ((withdraw_amount / 100) * 1.5))
                    self.__balance_atm -= (withdraw_amount - ((withdraw_amount / 100) * 1.5))
                    print(f"Rомиссия за снятие наличных (1.5%): {(withdraw_amount / 100) * 1.5}")
                elif (withdraw_amount / 100) * 1.5 < 30:
                    self.card.card_balance -= (withdraw_amount + 30)
                    self.__balance_atm -= (withdraw_amount - 30)
                    print("Rомиссия за снятие наличных = 30")
                elif (withdraw_amount / 100) * 1.5 > 600:
                    self.card.card_balance -= (withdraw_amount + 600)
                    self.__balance_atm -= (withdraw_amount - 600)
                    print("Комиссия за снятие наличных = 600")
                print("Снятие денежных средств прошло успешно\n")
                self.card.operations_count += 1
        else:
            print("Сумма снятия наличных должна быть кратна 50")

    def current_card_balance(self):
        return self.card.card_balance

    def get_atm_balance(self):
        return self.__balance_atm

    def end_session(self):
        exit()