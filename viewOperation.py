from Controller import *


def show_method():
        """

        show to us all our operation
        :return:

        """
        i = 0
        while i < len(Operation_History):
            print(" Id you'r operation :"+str((i+1)))
            print(" Sign you'r operation :"+Operation_History[i]['sign'])
            Sum = " Summary you'r operation :"
            print(Sum+str(Operation_History[i]['summary']))
            print(" Day you'r operation :"+str(Operation_History[i]['dd']))
            print(" Mounth you'r operation :"+str(Operation_History[i]['mm']))
            print(" Year you'r operation :"+str(Operation_History[i]['yy']))
            Com = " Comment to you'r operation :"
            print(Com+Operation_History[i]['comment']+"\n")
            i += 1

def show_list():
        """

        show to us main menu
        :return:

        """
        shows = ' 1: Show'
        cr_pp = '\n 2:Create Operation'
        d_op = '\n 3:Delete Operation'
        e_op = '\n 4:Edit Operation'
        print(shows, cr_pp, d_op, e_op)
        p_b = " 5:Positive Balance"
        n_b = "\n 6:Negative Balance"
        s_b = "\n 7:Summary Balance"
        e = "\n 8:Exit"
        print(p_b + n_b + s_b + e)

def menu_create():
        """

        create operation menu
        :return:

        """
        sign1 = input("\n Enter you'r sign :")
        summary2 = input(" Enter summary of you'r operation :")
        dd3 = input(" Enter day :")
        mm4 = input(" Enter month :")
        yy5 = input(" Enter year :")
        comment6 = input(" Enter comment of you'r operation :")
        database().create(sign1, summary2, dd3, mm4, yy5, comment6)
        show_method()

def menu_delete():
        """

        delete operation menu
        :return:

        """
        show_method()
        op_id = int(input("\n Enter number of operation what you want to delete :"))
        database().delete(op_id)
        show_method()

def menu_edit():
        """

        edit operation menu
        :return:

        """
        show_method()
        op_ch = " Enter number of operation what you want to change:"
        op_id = int(input(op_ch))
        sign1 = input(" Enter you'r new sign :")
        summary2 = int(input(" Enter summary of you'r  new operation :"))
        dd3 = int(input(" Enter new day :"))
        mm4 = int(input(" Enter new month :"))
        yy5 = int(input(" Enter new year :"))
        comment6 = input(" Enter new comment of you'r operation :")
        database().edit_all(op_id, sign1, summary2, dd3, mm4, yy5, comment6)
        show_method()

def menu_balance_plus(self):
        """

        income of all operation menu
        :return:

        """
        op_balance = operation().balance_plus()
        print("You'r income =" + str(op_balance))

def menu_balance_minus():
        """

        expenses of all operation menu
        :return:

        """
        op_balance = operation().balance_minus()
        print("You'r expenses =" + str(op_balance))

def menu_balance_all():
        """

        balance of all operation menu
        :return:

        """
        op_balance = operation().difference()
        print("You'r balance = " + str(op_balance))