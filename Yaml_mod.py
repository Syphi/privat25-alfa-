import yaml


class YamlMethod:

     def serial_method(func):
        def wrapper(op_id, sign, summary, dd, mm, yy, comment):
            with open('ser.yaml', 'r') as f:
                ser = yaml.load(f)
            crud = func(op_id, sign, summary, dd, mm, yy, comment )
            with open('ser.yaml', 'w') as f:
                yaml.dump(ser, f)
            return crud
        return wrapper
