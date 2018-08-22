import requests
import bs4

def main():
    print_the_header()

    code = get_zip_code()

    html = get_html_from_web(code)

    get_weather_from_html(html)

    # display the forecast


def print_the_header():
    print('-------------------------------------------')
    print('                Weather App')
    print('-------------------------------------------')
    print()


def get_zip_code():
    zip_code = input('What is your zip code? ')
    # print(zip_code)
    return zip_code


def get_html_from_web(zip_code):
    url = 'https://www.wunderground.com/weather/us/va/ashburn/{}'.format(zip_code)
    # print('url: {}'.format(url))
    response = requests.get(url)
    # print(response.status_code)
    # print(response.text[0:250])

    return response.text


def get_weather_from_html(html):
    soup = bs4.BeautifulSoup(html)
    print(soup)


if __name__ == '__main__':  # always use this convention when calling main() method
    main()
