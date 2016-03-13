from Controller import *

class Main:

    def show_list(self):
        print (" 1: Show" + "\n 2:Create Operation" + "\n 3:Delete Operation" + "\n 4:Edit Operation")
        print (" 5:Positive Balance" + "\n 6:Negative Balance" + "\n 7:Summary Balance" + "\n 8:Exit")

    def menu_create(self):
        sign1=raw_input("\n Enter you'r sign :")
        summary2=raw_input(" Enter summary of you'r operation :")
        dd3=raw_input(" Enter day :")
        mm4=raw_input(" Enter mounth :")
        yy5=raw_input(" Enter year :")
        comment6=raw_input(" Enter comment of you'r operation :")
        Create_Method().Create(sign1,summary2,dd3,mm4,yy5,comment6)
        Show().Show_method()

    def menu_delete(self):
        Show().Show_method()
        op_id=raw_input("\n Enter number of operation what you want to delete :")
        Delete().Delete_operation(int(op_id))
        Show().Show_method()

    def menu_edit(self):
        Show().Show_method()
        op_id=int(raw_input(" Enter number of operation what you want to chenge:"))
        sign1=raw_input(" Enter you'r new sign :")
        summary2=int(raw_input(" Enter summary of you'r  new operation :"))
        dd3=int(raw_input(" Enter new day :"))
        mm4=int(raw_input(" Enter new mounth :"))
        yy5=int(raw_input(" Enter new year :"))
        comment6=raw_input(" Enter new comment of you'r operation :")
        Edit().Edit_all(op_id,sign1,summary2,dd3,mm4,yy5,comment6)
        Show().Show_method()

    def menu_balance_plus(self):
        op_balance=Balance().balance_plus()
        print ("You'r income =" + str(op_balance))

    def menu_balance_minus(self):
        op_balance=Balance().balance_minus()
        print ("You'r expenses =" + str(op_balance))

    def menu_balance_all(self):
        op_balance=Balance().Balance_Difference()
        print ("You'r balance = " + str(op_balance))



    def Menu(self):
        self.show_list()
        op=int(raw_input("\n Enter menu numder :"))
        if op==1 :
            Show().Show_method()
            self.Menu()
        elif op==2 :
            self.menu_create()
            self.Menu()
        elif op==3 :
            self.menu_delete()
            self.Menu()
        elif op==4 :
            self.menu_edit()
            self.Menu()
        elif op==5 :
            self.menu_balance_plus()
            self.Menu()
        elif op==6 :
            self.menu_balance_minus()
            self.Menu()
        elif op==7 :
            self.menu_balance_all()
            self.Menu()
        elif op==8 :
            exit()
        else:
            print("\n NOT RIGHT NUMBER!")
            self.Menu()

Main().Menu()



