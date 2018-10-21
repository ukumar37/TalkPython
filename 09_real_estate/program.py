import csv
import os
import statistics

from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    print(filename)
    data = load_file(filename)
    query_data(data)


def print_header():
    print('----------------------------------')
    print('-------The Real Estate App--------')
    print('----------------------------------')
    print('')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:

        reader = csv.DictReader(fin)
        purchases = []  # create an empty list
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        return purchases

        # header = fin.readline().strip()
        # reader = csv.reader(fin, delimiter=',')
        #
        # print(header)
        # for row in reader:
        #     print(type(row), row)


# def load_file_basic(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline().strip()
#         print('found header :' + header)
#
#         lines = []
#         for line in fin:
#             line_data = line.strip().split(',')
#             bed_count = line_data[4]
#             lines.append(line_data)
#
#         print(lines[:5])


#  def get_price(p):
#      return p.price


def query_data(data):

    #  if data were sorted by price:
    data.sort(key=lambda p: p.price)  # 'p' is the argument which

    #  most expensive house
    high_price = data[-1]
    print('The most expensive house is ${:,} with {} beds and {} baths.'.format(high_price.price, high_price.beds,
                                                                                high_price.baths))

    #  least expensive house
    low_price = data[0]
    print('The least expensive house is ${:,} with {} beds and {} baths.'.format(low_price.price, low_price.beds,
                                                                                 low_price.baths))

    #  average price of house
    # prices = []  # create an empty list
    # for pur in data:
    #    prices.append(pur.price)

    prices = [
        p.price  # projection or items
        for p in data  # the set to process
    ]

    mean_price = statistics.mean(prices)
    print("The average home price is ${:,}".format(int(mean_price)))

    #  average price of a 2-bedroom house
    # prices = []  # create an empty list
    # for pur in data:
    #     if pur.beds ==2:
    #         prices.append(pur.price)

    two_bed_homes = [
        p  # projection or items
        for p in data  # the set to process
        if p.beds == 2  # test or condition
    ]

    average_price = statistics.mean([p.price for p in two_bed_homes])  # this concept is called "list comprehension"
    average_baths = statistics.mean([p.baths for p in two_bed_homes])
    average_sqft = statistics.mean([p.sq__ft  for p in two_bed_homes])
    mean_price = statistics.mean(prices)
    print("The average 2 bedroom home is ${:,}, baths {}, and sq ft {:,}".format(int(mean_price),
                                                                                 round(average_baths, 1),
                                                                                 round(average_sqft, 1)))


if __name__ == '__main__':
    main()


