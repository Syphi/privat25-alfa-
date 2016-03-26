from Controller import *

class main:

    def menu(self):
        """

        interface menu
        :return:

        """
        view().show_list()
        op = int(input("\n Enter menu number :"))
        if op == 1:
            view().show_method()
            self.menu()
        elif op == 2:
            view().create()
            self.menu()
        elif op == 3:
            view().delete()
            self.menu()
        elif op == 4:
            view().edit()
            self.menu()
        elif op == 5:
            view().balancePlus()
            self.menu()
        elif op == 6:
            view().balanceMinus()
            self.menu()
        elif op == 7:
            view().balanceAll()
            self.menu()
        elif op == 8:
            exit()
        else:
            print("\n Not right number!!")
            self.menu()

main().menu()
