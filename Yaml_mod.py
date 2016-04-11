import yaml


class YamlMethod:

     def serial_method(func):
        def wrapper():
            with open('ser.yaml', 'r') as f:
                ser = yaml.load(f)
            crud = func()
            with open('ser.yaml', 'w') as f:
                yaml.dump(ser, f)
            return crud
        return wrapper
