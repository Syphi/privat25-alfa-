import json


class JsonMethod:

    def serial_method(func):
        def wrapper(op_id, sign, summary, dd, mm, yy, comment):
            with open('ser.json', 'r') as f:
                ser = json.load(f)
            crud = func(op_id, sign, summary, dd, mm, yy, comment)
            with open('ser.json', 'w') as f:
                json.dump(ser, f)
            return crud
        return wrapper