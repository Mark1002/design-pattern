class SingletonMetaclass(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)
    # 決定若使用類別來建構物件時，該如何進行物件的建立與初始
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
