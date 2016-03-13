from module import *

#  Edit_Method.Edit_sign(1,'+')
class Balance:

    def balance_plus(self):
        plus=0
        i= 0
        for i in range(len(Operation_History)):
            if Operation_History[i]['sign']=='+':
                plus+=Operation_History[i]['summary']
        return plus

    def balance_minus(self):
        minus=0
        for i in range(len(Operation_History)):
            if Operation_History[i]['sign']=='-':
                minus+=Operation_History[i]['summary']
        return minus

    def Balance_Difference(self):
        return self.balance_plus()-self.balance_minus()


class Edit:

    def Edit_all(self,op_id,sign,summary,dd,mm,yy,comment):
        Edit_Method().Edit_sign(op_id,sign)
        Edit_Method().Edit_summary(op_id,summary)
        Edit_Method().Edit_dd(op_id,dd)
        Edit_Method().Edit_mm(op_id,mm)
        Edit_Method().Edit_yy(op_id,yy)
        Edit_Method().Edit_comment(op_id,comment)


class Show:

    def Show_method(self):
        i = 0
        while i < len(Operation_History):
            print(" Id you'r operation :"+str((i+1)))
            print(" Sign you'r operation :"+Operation_History[i]['sign'])
            print(" Summary you'r operation :"+str(Operation_History[i]['summary']))
            print(" Day you'r operation :"+str(Operation_History[i]['dd']))
            print(" Mounth you'r operation :"+str(Operation_History[i]['mm']))
            print(" Year you'r operation :"+str(Operation_History[i]['yy']))
            print(" Comment to you'r operation :"+Operation_History[i]['comment']+"\n")
            i+=1