from collections import UserDict


class Field:

    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:

    def __init__(self, Name, Phone=[], Email=[]):
        self.name = Name
        self.phones = [Phone]
        self.email = [Email]


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def remove_record(self, name):
        self.data.pop(name)

    def change_record(self, name):
        if self.data.name:
            self.data.get(name)
