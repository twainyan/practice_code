class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class Spam(metaclass=Singleton):
    def __init__(self):
        print('create spam')

class Spam2(metaclass=Singleton):
    def __init__(self):
        print('create spam2')

s = Spam()
b = Spam()
print(s is b)
s2 = Spam2()
print(s2 is s)
