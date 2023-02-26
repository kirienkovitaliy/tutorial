import re
from collections import UserDict
from datetime import datetime


class Field:

    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


class Name(Field):
    pass


class Phone(Field):

    def __init__(self, phone):
        self.__phone = None
        self.phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        phone = re.sub(r'-|\(|\)|\+| ', '', phone)
        phone = phone.strip()
        self.__phone = phone


class Birthday(Field):
    def __init__(self, birthday):
        self.__birthday = None
        self.birthday = birthday

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        if birthday == datetime.strptime(birthday, "%d.%m.%Y"):
            self.__birthday = birthday


class Record:

    def __init__(self, name, phone: Phone = None, email=None, birthday=None):
        self.name = name
        self.phones = []
        self.emails = []
        self.birthday = birthday
        if phone:
            self.phones.append(phone)
        if email:
            self.emails.append(email)

    def days_to_birthday(self):
        if Birthday:
            current_datetime = datetime.now()
            user_db = datetime.strptime(Birthday, "%d.%m.%Y")
            user_db = user_db.replace(year=current_datetime.year)
            return (user_db - current_datetime).days


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def remove_record(self, name):
        self.data.pop(name)

    def change_record(self, name):
        if self.data.name:
            self.data.get(name)

    def iterator(self, N):
        for indx, val in enumerate(self.values, start=1):
            if indx <= N:
                yield val
