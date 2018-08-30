import requests
import bs4
import collections

# Define/create a new type of collection called "WeatherReport"
WeatherReport = collections.namedtuple('WeatherReport',
                                       'cond, scale, temp, loc')


def main():
    print_the_header()

    code = get_zip_code()

    html = get_html_from_web(code)

    report = get_weather_from_html(html)

    # display the forecast
    print('The temp in {} is {} {} and {}.'.format(
        report.loc,
        report.temp,
        report.scale,
        report.cond
    ))


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
    # cityCss = '.region-content-header h1'
    # weatherConditionCss = '.condition-icon'
    # weatherTempCss = '.wu-unit-temperature.wu-value'
    # weatherScaleCss = '.wu-unit-temperature.wu-label'

    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = cleanup_text(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # print(loc, condition, temp, scale)
    # return loc, condition, temp, scale
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report


def cleanup_text(text: str):
    if not text:
        return text

    text = text.strip()

    return text


if __name__ == '__main__':  # always use this convention when calling main() method
    main()
