class Person(object):
    def __init__(self):
        self.__country="China"

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self,country):
        self.__country=country

p=Person()
print(p.country)
p.country="china"
print(p.country)
