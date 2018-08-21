def main():
    # print the header
    print_the_header()
    # get the zip code
    get_zip_code()
    # get the html from web
    # parse the html
    # display the forecast


def print_the_header():
    print('-------------------------------------------')
    print('                Weather App')
    print('-------------------------------------------')
    print()


def get_zip_code():
    zip_code = input('What is your zip code? ')
    print(zip_code)


if __name__ == '__main__':  # always use this convention when calling main() method
    main()
