import os


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry, we can't search that location.")
        return

    text = get_search_text_from_user():
    if not text:
        print("Sorry, we can't search for nothing!")
        return

    search_folder(folder, text)


def print_header():
    print('-----------------------------------')
    print('         FILE SEARCH APP')
    print('-----------------------------------')


def get_folder_from_user():
    folder = input('What folder do you want to search?')
    if not folder or folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    pass


def search_folder():
    pass


if __name__ == '__main__':
    main()
