from datetime import datetime, timedelta


users = [{"name": "Tanya", "birthday": datetime(1960, 2, 6)},
         {"name": "Sonya", "birthday": datetime(2015, 2, 7)},
         {"name": "Bill", "birthday": datetime(1965, 2, 8)},
         {"name": "Jill", "birthday": datetime(1978, 2, 9)},
         {"name": "Kim", "birthday": datetime(1989, 2, 10)},
         {"name": "Nastya", "birthday": datetime(1990, 4, 11)},
         {"name": "Jan", "birthday": datetime(1991, 3, 12)}]


def get_birthdays_per_week(users):

    Monday = []
    Tuesday = []
    Wednesday = []
    Thursday = []
    Friday = []

    current_datetime = datetime.now()
    next_month = current_datetime.month + 1

    for i in users:
        user_db = i.get("birthday")
        user_db_name = i.get("name")
        user_db = user_db.replace(year=current_datetime.year)
        if current_datetime.month == user_db.month and current_datetime.day <= user_db.day <= current_datetime.day + 7 or next_month == user_db.month and current_datetime.day <= user_db.day <= current_datetime.day + 7:
            if user_db.weekday() == 0:
                Monday.append(user_db_name)
            elif user_db.weekday() == 1:
                Tuesday.append(user_db_name)
            elif user_db.weekday() == 2:
                Wednesday.append(user_db_name)
            elif user_db.weekday() == 3:
                Thursday.append(user_db_name)
            elif user_db.weekday() == 4:
                Friday.append(user_db_name)
            elif user_db.weekday() == 5:
                Monday.append(user_db_name)
            elif user_db.weekday() == 6:
                Monday.append(user_db_name)
            else:
                continue
    if Monday != []:
        print(f"Monday: {Monday}")
    if Tuesday != []:
        print(f"Tuesday: {Tuesday}")
    if Wednesday != []:
        print(f"Wednesday : {Wednesday}")
    if Thursday != []:
        print(f"Thursday: {Thursday}")
    if Friday != []:
        print(f"Friday: {Friday}")


get_birthdays_per_week(users)
