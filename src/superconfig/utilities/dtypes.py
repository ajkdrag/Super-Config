class CallableConverter(type):
    def __call__(cls, val):
        return cls.convert(val)


class ANY(metaclass=CallableConverter):
    @staticmethod
    def convert(value):
        return value


class STR(ANY):
    @staticmethod
    def convert(value):
        return str(value)


class INT(STR):
    @staticmethod
    def convert(value):
        return int(value)


class FLOAT(STR):
    @staticmethod
    def convert(value):
        return float(value)


class BOOL(STR):
    @staticmethod
    def convert(value):
        return bool(value)
