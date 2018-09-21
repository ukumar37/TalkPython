import os


def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry, we can't search that location.")
        return

    text = get_search_text_from_user()
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
    if not folder or not folder.strip():
        return None

    if not os.path.isdir(folder):
        return None

    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]?')
    return text


def search_folder(folder, text):

    all_matches = []
    items = os.listdir(folder)  # list all the files (items) in the given folder

    for item in items:
        full_item = os.path.join(folder, item)  # create full path name by joining folder and file
        if os.path.isdir(full_item):  # if item is a directory, skip item
            continue

        matches = search_file(full_item, text)  # if item is a file, search text in file
        all_matches.extend(matches)

if __name__ == '__main__':
    main()
