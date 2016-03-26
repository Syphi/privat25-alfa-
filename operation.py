from Controller import *


class balance:

    def balance_plus(self):
        """
        show our income
        :return: our income of all our operation

        """
        plus = 0
        i = 0
        for i in range(len(Operation_History)):
            if Operation_History[i]['sign'] == '+':
                plus += Operation_History[i]['summary']
        return plus

    def balance_minus(self):
        """

        show our expenses
        :return: all our expenses

        """
        minus = 0
        for i in range(len(Operation_History)):
            if Operation_History[i]['sign'] == '-':
                minus += Operation_History[i]['summary']
        return minus

    def balance_difference(self):
        """

        :return: different between our income and expenses

        """
        return self.balance_plus()-self.balance_minus()