import datetime

def print_header():
    print('------------------------')
    print('      Birthday App')
    print('------------------------')
    print()


def get_birthday_from_user():
    print("When were you born?")
    birthday_month = int(input('Enter birthday month in mm format: '))
    birthday_day = int(input('Enter birthday day in dd format: '))
    birthday_year = int(input('Enter birthday year in yyyy format: '))

    birthday = datetime.date(birthday_year, birthday_month, birthday_day)
    return birthday


def compute_days_between_dates():
    pass


def print_birthday_information():
    pass


def main():
    print_header()
    bday = get_birthday_from_user()
    print(bday)
    now = None
    number_of_days = compute_days_between_dates(bday, now)
    print_header(number_of_days)

main()