import pickle
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
        if self.birthday:
            current_datetime = datetime.now().date()
            user_db = self.birthday.value.split('.')
            date = datetime(year=current_datetime.year, month=int(
                user_db[1]), day=int(user_db[0])).date()
            next = date - current_datetime
            if next.days < 0:
                date = datetime(year=current_datetime.year + 1,
                                month=int(user_db[1]), day=int(user_db[0])).date()
            else:
                next = date - current_datetime
            return next


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

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def search(self, query):
        query = query.lower()
        results = []
        for record in self.values():
            if query in record.name.value.lower():
                results.append(record)
            for phone in record.phones:
                if query in phone.phone.lower():
                    results.append(record)
            for email in record.emails:
                if query in email.lower():
                    results.append(record)
        return results


# Створення книги
address_book = AddressBook()

# Створення записів
record1 = Record(Name('John Doe'), Phone('555-1234'),
                 'johndoe@example.com', Birthday('01.01.1990'))
record2 = Record(Name('Jane Doe'), Phone('555-5678'),
                 'janedoe@example.com', Birthday('02.02.1991'))

# Додавання записів в книгу
address_book.add_record(record1)
address_book.add_record(record2)

# Перевірка, чи записи додалися в книгу
print(address_book.data)

# Видалення запису з книги
address_book.remove_record('Jane Doe')

# Перевірка, чи запис видалився з книги
print(address_book.data)

# Зміна запису
address_book.change_record('John Doe')

# Ітерація по першим N записам в книзі
for record in address_book.iterator(1):
    print(record)

# Пошук в книзі
results = address_book.search('john')
print(results)

# Збереження книги у файл
address_book.filename = 'address_book.pkl'
address_book.save_to_file()

# Читання книги з файлу
address_book_from_file = AddressBook()
address_book_from_file.filename = 'address_book.pkl'
address_book_from_file.read_from_file()
print(address_book_from_file.data)
