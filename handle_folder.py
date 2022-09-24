import os
import utils

my_list = []


def scan_folders(mydir, modify_folder):
    """Parcours les fichiers dans le dossier"""
    with os.scandir(mydir) as it:
        for entry in it:
            if entry.is_dir():
                total, count = folder_size(entry)
                rename_folder(mydir, entry.name, total, count, modify_folder)
    utils.sort_data(my_list)


def rename_folder(mydir, name, total, count, modify_folder):
    """Renomme le nom du dossier"""
    clean_name = utils.clean_name(name)
    humane_size = utils.human_readable_size_go(total)

    my_list.append(utils.my_file(total, humane_size, clean_name, str(count))) ## size hsize folder
    if modify_folder:
        new_name = f'{clean_name:<12}' + ' - ' + f'{str(count):<2}' + ' - ' + f'{humane_size:<6}'
        os.rename(mydir + '/' + name, mydir + '/' + new_name)


def folder_size(folder):
    """Retourne le nombre de fichiers et la taille totale."""
    total = 0
    count = 0
    with os.scandir(folder) as it:
        for entry in it:
            if entry.is_file() and not entry.name.endswith('.ini'):
                total += entry.stat().st_size
                count += 1
    return total, count
