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

    matches = search_folder(folder, text)  # search folder for files and then files for text. Return matches.
    for m in matches:
        print(repr(m))


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
    return text.lower()  # return lower case text


def search_folder(folder, text):
    all_matches = []  # create an empty collection
    items = os.listdir(folder)  # list all the files (items) in the given folder

    for item in items:
        full_item = os.path.join(folder, item)  # create full path name by joining folder and file
        if os.path.isdir(full_item):  # if item is a directory, skip item
            continue

        matches = search_file(full_item, text)  # if item is a file, search text in file
        all_matches.extend(matches)  # extend collection by adding new matches

    return all_matches


def search_file(filename, search_text):
    matches = []
    # with open(filename, 'r', encoding='utf-8') as fin:
    with open(filename, 'r', encoding='latin-1') as fin:

        for line in fin:
            if line.lower().find(search_text) >= 0:  # search text in the line within the file
                matches.append(line)

        return matches


if __name__ == '__main__':
    main()
