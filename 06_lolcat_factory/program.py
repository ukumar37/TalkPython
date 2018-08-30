import os
import subprocess

import cat_service


def main():
    print_header()

    folder = get_or_create_output_folder()
    print('found or created folder: ' + folder)

    download_cats(folder)

    display_cats(folder)


def print_header():
    print('---------------------------')
    print('       CAT FACTORY')
    print('---------------------------')


def get_or_create_output_folder():
    base_folder = os.path.dirname(__file__)  # '__file__' is the current file name (i.e. program.py)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):  # check to see if a file or folder by that name
        # already exists. If yes, do not 'mkdir'
        print('creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path

    print(full_path)


def download_cats(folder):
    print('contacting server to download cats ...')
    cat_count = 8  # get 8 cats only
    for i in range(1, cat_count + 1):
        name = 'lolcat {}'.format(i)
        print('downloading cat ' + name)
        cat_service.get_cat(folder, name)

    print('done')


def display_cats(folder):
    # open folder
    print('displaying cats in OS window.')
    subprocess.call(['open', folder])

if __name__ == '__main__':  # only run the main method if it is being called from the program (i.e. not as a package)
    main()
