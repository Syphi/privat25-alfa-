import pickle


class PickleMethod:

     def serial_method(func):
        def wrapper():
            with open('ser.pickle' ,'rb') as f:
                ser = pickle.load(f)
            crud = func()
            with open('ser.pickle', 'wb') as f:
                pickle.dump(ser, f)
            return crud
        return wrapper

