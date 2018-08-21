def main():
    # print the header
    print_the_header()
    # get the zip code
    code = get_zip_code()
    # get the html from web
    get_html_from_web(code)
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
    return zip_code


def get_html_from_web(zip_code):
    url = 'https://www.wunderground.com/weather/us/va/ashburn/{}'.format(zip_code)
    print('url: {}'.format(url))


if __name__ == '__main__':  # always use this convention when calling main() method
    main()
