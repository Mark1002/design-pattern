class _SingleTon:
    def __init__(self):
        self._id = id(self)
    
    def get_id(self):
        return self._id

SingleTonObject = _SingleTon()
