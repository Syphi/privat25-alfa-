from module import *


class balance:

    def balance_plus(self):
        """
        >>> dp = balance()
        >>> dp.balance_plus()

        """
        plus = 0
        i = 0
        for i in range(len(Operation_History)):
            if Operation_History[i]['sign'] == '+':
                plus += Operation_History[i]['summary']
        return plus

    def balance_minus(self):
        """
        >>> dp = balance()
        >>> dp.balance_minus()

        """
        minus = 0
        for i in range(len(Operation_History)):
            if Operation_History[i]['sign'] == '-':
                minus += Operation_History[i]['summary']
        return minus

    def balance_difference(self):
        """
        >>> dp = balance()
        >>> dp.balance_difference()

        """
        return self.balance_plus()-self.balance_minus()


class edit:

    def edit_all(self, op_id, sign, summary, dd, mm, yy, comment):
        edit_method().edit_sign(op_id, sign)
        edit_method().edit_summary(op_id, summary)
        edit_method().edit_dd(op_id, dd)
        edit_method().edit_mm(op_id, mm)
        edit_method().edit_yy(op_id, yy)
        edit_method().edit_comment(op_id, comment)


class show:

    def show_method(self):
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
