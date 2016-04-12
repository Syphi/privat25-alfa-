from database import *
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
if config['DEFAULT']['FileType'] == pickle
    from Pickle_mod import PickleMethod
    Methods=PickleMethod
elif config['DEFAULT']['FileType'] == json
    from Json_mod import JsonMethod
    Methods=JsonMethod
elif config['DEFAULT']['FileType'] == yaml
    from Yaml_mod import YamlMethod
    Methods=YamlMethod



class create_method:

    @staticmethod
    @Methods.serial_method
    def create(op_id, sign, summary, dd, mm, yy, comment):
        """

        create operation in our list
        :return:

        """
        op_id = 0
        global Operation_History
        operation = {'sign': sign,
                     'summary': summary,
                     'dd': dd, 'mm': mm, 'yy': yy,
                     'comment': comment}
        Operation_History.append(operation)


class edit_method:

    @staticmethod
    @Methods.serial_method
    def edit_sign( op_id, sign, summary, dd, mm, yy, comment):
        """

        edit sign in need operation
        :return:

        """
        summary = 0
        dd = 0
        mm = 0
        yy = 0
        comment = ''
        global Operation_History
        Operation_History[op_id-1]['sign'] = sign

    @staticmethod
    @Methods.serial_method
    def edit_summary( op_id, sign, summary, dd, mm, yy, comment):
        """

        edit summary in need operation
        :return:

        """
        sign = 0
        dd = 0
        mm = 0
        yy = 0
        comment = ''
        global Operation_History
        Operation_History[op_id-1]['summary'] = summary

    @staticmethod
    @Methods.serial_method
    def edit_dd( op_id, sign, summary, dd, mm, yy, comment):
        """

        edit day in need operation
        :return:

        """
        summary = 0
        sign = 0
        mm = 0
        yy = 0
        comment = ''
        global Operation_History
        Operation_History[op_id-1]['dd'] = dd

    @staticmethod
    @Methods.serial_method
    def edit_mm( op_id, sign, summary, dd, mm, yy, comment):
        """

        edit month in need operation
        :return:

        """
        summary = 0
        sign = 0
        dd = 0
        yy = 0
        comment = ''
        global Operation_History
        Operation_History[op_id-1]['mm'] = mm

    @staticmethod
    @Methods.serial_method
    def edit_yy( op_id, sign, summary, dd, mm, yy, comment):
        """

        edit year in need operation
        :return:

        """
        summary = 0
        sign = 0
        mm = 0
        dd = 0
        comment = ''
        global Operation_History
        Operation_History[op_id-1]['yy'] = yy

    @staticmethod
    @Methods.serial_method
    def edit_comment( op_id, sign, summary, dd, mm, yy, comment):
        """

        edit comment in need operation
        :return:

        """
        summary = 0
        sign = 0
        mm = 0
        yy = 0
        dd = 0
        global Operation_History
        Operation_History[op_id-1]['comment'] = comment


class delete:

    @staticmethod
    @Methods.serial_method
    def delete_operation( op_id, sign, summary, dd, mm, yy, comment):
        """

        delete need operation
        :return:

        """
        summary = 0
        sign = 0
        mm = 0
        yy = 0
        dd = 0
        comment = ''
        global Operation_History
        Operation_History.pop(op_id-1)
