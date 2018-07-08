from singleton_module import SingleTonObject
from singleton_meta import Singleton
from singleton_standard import SingleTon

def execute():
    print("standard method: {}".format(SingleTon.get_instance().get_id()))
    print("module method: {}".format(SingleTonObject.get_id()))
    print("metaClass method: {}".format(Singleton().get_id()))
