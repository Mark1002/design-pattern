class SingletonMetaclass(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)
    # __call__ 表示這個類別實例可以當成函數呼叫
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class Singleton(metaclass=SingletonMetaclass):
    def __init__(self):
        self._id = id(self)

    def get_id(self):
        return self._id
