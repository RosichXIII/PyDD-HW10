from atm import Atm

class Menu():

    def __init__(self, atm: Atm):
        self.atm = atm

    def card_menu(self):
        print("Главное меню:")
        while True:
            choise = input("1. Узнать баланс\n2. Пополнить счёт\n3. Снять наличные\n4. Остаток наличных средств в банокате\n0. Завершить сеанс\n")
            if choise == "1":
                print(f"\nТекущий баланс: {self.atm.current_card_balance()}\n")
            elif choise == "2":
                self.atm.refill_account()
            elif choise == "3":
                self.atm.withdraw_cash()
            elif choise == "4":
                print(f"\nОстаток наличных в банкомате: {self.atm.get_atm_balance()}\n")                
            elif choise == "0":
                print("\nСпасибо что воспользовались нашими услугами.\n")
                self.atm.end_session()
            else:
                print("\nВыыбраy ошибочный пункт. Попробуйте снова\n")