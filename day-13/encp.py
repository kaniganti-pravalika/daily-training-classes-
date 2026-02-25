class A:
    def __init__(self,variable):
        self._variable=variable
        print(variable)
    
obj=A("10")

class demo:
    def __init__(self):
        self._x=10
    def __show(self):
        print(self._x)
    def get_value(self):
        return self._x
obj=demo
print(obj.get_value)
obj.__show()

class demo:
    def __init__(self):
        self.__x=10
    def get_value(self):
        return self.__x
    def set_value(self,value):
        self._x=value
obj=demo()
print(obj.get_value())
obj.set_value(20)
print(obj.get_value)