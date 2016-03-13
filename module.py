from Controller import *

Operation_0={'sign':'+','summary':200,'dd':16,'mm':01,'yy':2016,'comment':"salary"}
Operation_1={'sign':'+','summary':35,'dd':8,'mm':03,'yy':2016,'comment':"debt"}
Operation_2={'sign':'-','summary':1500,'dd':16,'mm':05,'yy':2016,'comment':"B'day"}

Operation_History = [Operation_0,Operation_1,Operation_2]

class Create_Method:

    def Create(self,sign,summary,dd,mm,yy,comment):
        global Operation_History
        Operation={'sign':sign,'summary':summary,'dd':dd,'mm':mm,'yy':yy,'comment':comment}
        Operation_History.append(Operation)

class Edit_Method:

    def Edit_sign(self,op_id,sign):
        global Operation_History
        Operation_History[op_id-1]['sign']=sign

    def Edit_summary(self,op_id,summary):
        global Operation_History
        Operation_History[op_id-1]['summary']=summary

    def Edit_dd(self,op_id,dd):
        global Operation_History
        Operation_History[op_id-1]['dd']=dd

    def Edit_mm(self,op_id,mm):
        global Operation_History
        Operation_History[op_id-1]['mm']=mm

    def Edit_yy(self,op_id,yy):
        global Operation_History
        Operation_History[op_id-1]['yy']=yy

    def Edit_comment(self,op_id,comment):
        global Operation_History
        Operation_History[op_id-1]['comment']=comment


class Delete:

    def Delete_operation(self,op_id):
        global Operation_History
        Operation_History.pop(op_id-1)