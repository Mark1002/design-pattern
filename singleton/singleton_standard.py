class SingleTon:
    _instance = None

    @staticmethod
    def get_instance():
        if SingleTon._instance == None:
            SingleTon()
        return SingleTon._instance
    # 應為 private 的建構子
    def __init__(self):
        if SingleTon._instance is not None:
            raise Exception('only one instance can exist')
        else:
            self._id = id(self)
            SingleTon._instance = self
    
    def get_id(self):
        return self._id
