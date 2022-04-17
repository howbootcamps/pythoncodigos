class Two:
    def __init__(self):
        self.__private_attr = 20


class TwoChild(Two):
    def __init__(self):
        super().__init__()
