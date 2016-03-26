from database import *


class create_method:

    def create(self, sign, summary, dd, mm, yy, comment):
        """

        create operation in our list
        :return:

        """
        global Operation_History
        operation = {'sign': sign,
                     'summary': summary,
                     'dd': dd, 'mm': mm, 'yy': yy,
                     'comment': comment}
        Operation_History.append(operation)


class edit_method:

    def edit_sign(self, op_id, sign):
        """

        edit sign in need operation
        :return:

        """
        global Operation_History
        Operation_History[op_id-1]['sign'] = sign

    def edit_summary(self, op_id, summary):
        """

        edit summary in need operation
        :return:

        """
        global Operation_History
        Operation_History[op_id-1]['summary'] = summary

    def edit_dd(self, op_id, dd):
        """

        edit day in need operation
        :return:

        """
        global Operation_History
        Operation_History[op_id-1]['dd'] = dd

    def edit_mm(self, op_id, mm):
        """

        edit month in need operation
        :return:

        """
        global Operation_History
        Operation_History[op_id-1]['mm'] = mm

    def edit_yy(self, op_id, yy):
        """

        edit year in need operation
        :return:

        """
        global Operation_History
        Operation_History[op_id-1]['yy'] = yy

    def edit_comment(self, op_id, comment):
        """

        edit comment in need operation
        :return:

        """
        global Operation_History
        Operation_History[op_id-1]['comment'] = comment


class delete:

    def delete_operation(self, op_id):
        """

        delete need operation
        :return:

        """
        global Operation_History
        Operation_History.pop(op_id-1)
