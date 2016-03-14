from Controller import *

operation_0 = {'sign': '+',
               'summary': 200,
               'dd': 16, 'mm': 1, 'yy': 2016,
               'comment': "salary"}
operation_1 = {'sign': '+',
               'summary': 35,
               'dd': 8, 'mm': 3, 'yy': 2016,
               'comment': "debt"}
operation_2 = {'sign': '-',
               'summary': 1500,
               'dd': 16, 'mm': 5, 'yy': 2016,
               'comment': "B'day"}

Operation_History = [operation_0, operation_1, operation_2]


class create_method:

    def create(self, sign, summary, dd, mm, yy, comment):
        global Operation_History
        operation = {'sign': sign,
                     'summary': summary,
                     'dd': dd, 'mm': mm, 'yy': yy,
                     'comment': comment}
        Operation_History.append(operation)


class edit_method:

    def edit_sign(self, op_id, sign):
        global Operation_History
        Operation_History[op_id-1]['sign'] = sign

    def edit_summary(self, op_id, summary):
        global Operation_History
        Operation_History[op_id-1]['summary'] = summary

    def edit_dd(self, op_id, dd):
        global Operation_History
        Operation_History[op_id-1]['dd'] = dd

    def edit_mm(self, op_id, mm):
        global Operation_History
        Operation_History[op_id-1]['mm'] = mm

    def edit_yy(self, op_id, yy):
        global Operation_History
        Operation_History[op_id-1]['yy'] = yy

    def edit_comment(self, op_id, comment):
        global Operation_History
        Operation_History[op_id-1]['comment'] = comment


class delete:

    def delete_operation(self, op_id):
        global Operation_History
        Operation_History.pop(op_id-1)
