CONTACTS = {}
GOOD_BYE_VERSION = ['good bye', 'close', 'exit']


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            print('Give me correct name please')
        except ValueError:
            print('Enter user name')
        except IndexError:
            print('Give me name and phone please')
        finally:
            main()
    return inner


@input_error
def main():
    bot = True
    while bot:
        print('...')
        answer = input().lower()
        if answer == 'hello':
            print('How can I help you?')
        elif answer in GOOD_BYE_VERSION:
            print('Good bye!')
            bot = False
        elif answer == ".":
            bot = False
        elif 'add' in answer:
            add(answer)
            print('contact added')
        elif 'change' in answer:
            change(answer)
            print('contact changed')
        elif "phone" in answer:
            print(f"phone {phone(answer)}")
        elif answer == 'show all':
            show(CONTACTS)
            print(f"Your contacts:\n{show(CONTACTS)} ")


def add(answer):
    answer = answer.split(' ')
    CONTACTS.update({answer[1]: answer[2]})


def change(answer):
    answer = answer.split(' ')
    if answer[1] in CONTACTS:
        CONTACTS.update({answer[1]: answer[2]})


def phone(answer):
    answer = answer.split(' ')
    phone = CONTACTS[answer[1]]
    return phone


def show(CONTACTS):
    str = ''
    for key, value in CONTACTS.items():
        str += f'{key}: {value} \n'
    str = str[:-2]
    return str


if __name__ == '__main__':
    main()
