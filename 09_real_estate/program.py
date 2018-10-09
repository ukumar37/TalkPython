import os


def main():
    print_header()
    filename = get_data_file()
    print(filename)


def print_header():
    print('----------------------------------')
    print('-------The Real Estate App--------')
    print('----------------------------------')
    print('')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data',
                        'SacramentoRealEstateTransactions2008.csv')

if __name__ == '__main__':
    main()


