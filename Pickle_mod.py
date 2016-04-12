import pickle


class PickleMethod:

     def serial_method(func):
        def wrapper(op_id, sign, summary, dd, mm, yy, comment):
            with open('ser.pickle', 'rb') as f:
                ser = pickle.load(f)
            crud = func(op_id, sign, summary, dd, mm, yy, comment)
            with open('ser.pickle', 'wb') as f:
                pickle.dump(ser, f)
            return crud
        return wrapper

