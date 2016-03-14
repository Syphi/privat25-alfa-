from Controller import *


class main:

    def show_list(self):
        show = ' 1: Show'
        cr_pp = '\n 2:Create Operation'
        d_op = '\n 3:Delete Operation'
        e_op = '\n 4:Edit Operation'
        print(show, cr_pp, d_op, e_op)
        p_b = " 5:Positive Balance"
        n_b = "\n 6:Negative Balance"
        s_b = "\n 7:Summary Balance"
        e = "\n 8:Exit"
        print(p_b + n_b + s_b + e)

    def menu_create(self):
        sign1 = input("\n Enter you'r sign :")
        summary2 = input(" Enter summary of you'r operation :")
        dd3 = input(" Enter day :")
        mm4 = input(" Enter mounth :")
        yy5 = input(" Enter year :")
        comment6 = input(" Enter comment of you'r operation :")
        create_method().create(sign1, summary2, dd3, mm4, yy5, comment6)
        show().show_method()

    def menu_delete(self):
        show().show_method()
        op_id = input("\n Enter number of operation what you want to delete :")
        delete().delete_operation(int(op_id))
        show().show_method()

    def menu_edit(self):
        show().show_method()
        op_ch = " Enter number of operation what you want to chenge:"
        op_id = int(input(op_ch))
        sign1 = input(" Enter you'r new sign :")
        summary2 = int(input(" Enter summary of you'r  new operation :"))
        dd3 = int(input(" Enter new day :"))
        mm4 = int(input(" Enter new mounth :"))
        yy5 = int(input(" Enter new year :"))
        comment6 = input(" Enter new comment of you'r operation :")
        edit().edit_all(op_id, sign1, summary2, dd3, mm4, yy5, comment6)
        show().show_method()

    def menu_balance_plus(self):
        op_balance = balance().balance_plus()
        print("You'r income =" + str(op_balance))

    def menu_balance_minus(self):
        op_balance = balance().balance_minus()
        print("You'r expenses =" + str(op_balance))

    def menu_balance_all(self):
        op_balance = balance().balance_difference()
        print("You'r balance = " + str(op_balance))

    def menu(self):
        self.show_list()
        op = int(input("\n Enter menu numder :"))
        if op == 1:
            show().show_method()
            self.menu()
        elif op == 2:
            self.menu_create()
            self.menu()
        elif op == 3:
            self.menu_delete()
            self.menu()
        elif op == 4:
            self.menu_edit()
            self.menu()
        elif op == 5:
            self.menu_balance_plus()
            self.menu()
        elif op == 6:
            self.menu_balance_minus()
            self.menu()
        elif op == 7:
            self.menu_balance_all()
            self.menu()
        elif op == 8:
            exit()
        else:
            print("\n Not right number!!")
            self.menu()

main().menu()
