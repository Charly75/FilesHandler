from string import digits
import math as m
import re


def human_readable_size_go(size, decimal_places=2):
    """Transforme octets """
    for unit in ['o', 'Ko', 'Mo', 'Go', 'To', 'Po']:
        if size < 1024.0 or unit == 'Po':
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f}{unit}"


def human_readable_size(size, decimal_places=2):
    """Transforme octets """
    for unit in ['o', 'Ko', 'Mo', 'Go', 'To', 'Po']:
        if size < 1024.0 or unit == 'Po':
            break
        size /= 1024.0

    if unit == 'Go':
        return str(m.trunc(size))
    elif unit == 'Mo':
        return '1'
    else:
        return f"{size:.{decimal_places}f}{unit}"


def clean_name(folder_name):
    """Supprimer les chiffres et mets en majuscule les premières lettres."""
    """ Suppression des caractères spéciaux"""
    # regex = re.compile('[^a-zA-Z]')
    regex = re.compile('[,\.\-_!?]')
    # First parameter is the replacement, second parameter is your input string
    folder_name = regex.sub('', folder_name)

    """ Suppression des Go """
    regex = re.compile('\d[KMGT]o\s*$')
    folder_name = regex.sub('', folder_name)

    """ Suppression des chiffres """
    remove_digits = str.maketrans('', '', digits)
    folder_name = folder_name.translate(remove_digits)

    """ Suppression des lettres isolées """
    regex = re.compile('\s[a-zA-Z]\s')
    folder_name = regex.sub('', folder_name)

    """ Suppression des doubles espaces """
    folder_name = ' '.join(folder_name.split())

    """  Suppression des espaces debut/fin """
    folder_name = folder_name.strip()

    return folder_name.title()
    # return folder_name.capitelize()


def sort_data(my_list):
    """Trie et formate les fichiers"""
    sorted_by_size = sorted(my_list, key=lambda x: x.size, reverse=True)
    for item in sorted_by_size:
        if item.count == 0:
            print(f'{item.size:<12}', ' | ' + f'{item.hsize:<12}', ' | ', item.name)
        else:
            print(f'{item.size:<12}', ' | ' + f'{item.hsize:<12}', ' | ' + f'{item.count:<2}', ' | ', item.name)

class my_file:
    def __init__(self, size, hsize, name, count=0):
        self.size = size
        self.hsize = hsize
        self.name = name
        self.count = count
