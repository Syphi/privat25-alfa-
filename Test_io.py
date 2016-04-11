import io
from operation import balance
test_balance = balance

operation_test_0 = {'sign': '+',
               'summary': 2}
operation_test_1 = {'sign': '+',
               'summary': 2}
operation_test_2 = {'sign': '-',
               'summary': 4}

test_string = io.StringIO(operation_test_0,operation_test_1,operation_test_2)

def test_balance_plus():
    Operation_History = test_string
    print(test_balance().balance_plus)

def test_balance_minus():
    Operation_History = test_string
    print(test_balance().balance_minus)

def test_balance_dif():
    Operation_History = test_string
    print(test_balance().balance_difference)




