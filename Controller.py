from module import *
from operation import *
from viewOperation import *

class operation:

    def balance_plus(self):
        return balance().balance_plus()

    def balance_minus(self):
       return balance().balance_minus()

    def difference(self):
       return balance().balance_difference()

class view:

    def show_list(self):
        show_list()

    def show_method(self):
        show_method()

    def create(self):
        menu_create()

    def delete(self):
        menu_delete()

    def edit(self):
        menu_edit()

    def balancePlus(self):
        menu_balance_plus()

    def balanceMinus(self):
        menu_balance_minus()

    def balanceAll(self):
        menu_balance_all()

class database():

    def edit_all(self, op_id, sign, summary, dd, mm, yy, comment):
        """

        edit our operation
        :return:

        """
        edit_method().edit_sign(op_id, sign)
        edit_method().edit_summary(op_id, summary)
        edit_method().edit_dd(op_id, dd)
        edit_method().edit_mm(op_id, mm)
        edit_method().edit_yy(op_id, yy)
        edit_method().edit_comment(op_id, comment)

    def create(self, sign1, summary2, dd3, mm4, yy5, comment6):
        create_method().create(sign1, summary2, dd3, mm4, yy5, comment6)

    def delete(self, op_id):
        delete().delete_operation(op_id)