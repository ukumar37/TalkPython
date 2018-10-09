import os


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


def load_data():
    return []


def query_data():
    pass


if __name__ == '__main__':
    main()

