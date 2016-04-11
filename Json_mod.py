import json


class JsonMethod:

    def serial_method(func):
        def wrapper():
            with open('ser.json', 'r') as f:
                ser = json.load(f)
            crud = func()
            with open('ser.json', 'w') as f:
                json.dump(ser, f)
            return crud
        return wrapper