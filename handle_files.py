import os
import utils

my_list = []


def files_list(path, file):
    """Liste des fichiers retournés dans un tableau"""
    file_size = os.stat(path + "\\" + file)
    my_list.append(utils.my_file(file_size.st_size, utils.human_readable_size_go(file_size.st_size), file))


def files_list_start_with(path, file, start_with):
    """Liste des fichiers (commençant par) retournés dans un tableau"""
    if file.startswith(start_with):
        file_size = os.stat(path + "\\" + file)
        my_list.append(utils.my_file(file_size.st_size, utils.human_readable_size_go(file_size.st_size), file))


def order_files_option_start(mydir, start_with):
    for path, currentDirectory, files in os.walk(mydir):
        for file in files:
            if start_with:
                files_list_start_with(path, file, start_with)
            else:
                files_list(path, file)
    utils.sort_data(my_list)
