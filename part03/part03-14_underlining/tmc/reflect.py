import importlib
from bdb import Bdb
import sys


class RecursionDetected(Exception):
    pass


class RecursionDetector(Bdb):
    def do_clear(self, arg):
        pass

    def __init__(self, *args):
        Bdb.__init__(self, *args)
        self.stack = set()

    def user_call(self, frame, argument_list):
        code = frame.f_code
        if code in self.stack:
            raise RecursionDetected
        self.stack.add(code)

    def user_return(self, frame, return_value):
        self.stack.remove(frame.f_code)


def test_recursion(func: callable, *args):
    detector = RecursionDetector()
    detector.set_trace()
    try:
        func(*args)
    except RecursionDetected:
        return True
    else:
        return False
    finally:
        sys.settrace(None)


class Reflect:
    def __init__(self, modulename: str = "", classname: str = ""):
        self.__classname = classname
        self.__modulename = modulename
        self.__cls = None

    def load_class(self):
        try:
            self.__cls = getattr(importlib.import_module(self.__modulename), self.__classname)
            return self.__cls
        except Exception as e:
            return None

    def load_object(self, *params):
        try:
            if not self.__cls:
                self.load_class()
            self.__obj = self.cls(*params)
            return self.__obj
        except Exception as e:
            print(e)
            return None

    def set_object(self, obj):
        self.__obj = obj

    @property
    def cls(self):
        return self.__cls

    @property
    def object(self):
        return self.__obj

    def list_attributes(self, filter_builtin=False):
        if filter_builtin:
            return [x for x in dir(self.__obj) if not x.startswith("__")]
        return dir(self.__obj)

    def has_attribute(self, attribute: str):
        if attribute in dir(self.__obj):
            return True
        if ("_" + self.__classname + attribute) in dir(self.__obj):
            return True
        return False

    def get_attribute(self, attribute: str):
        if attribute in dir(self.__obj):
            return getattr(self.__obj, attribute)
        elif ("_" + self.__classname + attribute) in dir(self.__obj):
            return getattr(self.__obj, "_" + self.__classname + attribute)
        return None

    def list_public_members(self):
        return [x for x in dir(self.__obj) if not x.startswith("_")]
