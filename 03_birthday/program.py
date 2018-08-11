import datetime

def print_header():
    print('-------------------------')
    print('      Birthday App')
    print('-------------------------')
    print()


def get_birthday_from_user():
    print("When were you born?")
    birthday_month = int(input('Enter birthday month in mm format: '))
    birthday_day = int(input('Enter birthday day in dd format: '))
    birthday_year = int(input('Enter birthday year in yyyy format: '))

    birthday = datetime.date(birthday_year, birthday_month, birthday_day)
    return birthday


def compute_days_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days


def print_birthday_information(days):
    if days < 0:
        print("You had your birthday {} days ago this year.".format(-days))
    elif days > 0:
        print("Your birthday is in {} days.".format(days))
    else:
        print("Happy Birthday!!!")


def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday, today)
    print_birthday_information(number_of_days)

main()