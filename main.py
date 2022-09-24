import handle_files
import handle_folder

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

##### Files #####
#v mydir: str = 'D:/PLURALSIGHT/Angular HTTP/7 T222'
# mydir: str = 'D:/PLURALSIGHT/Angular HTTP/7 T554'
mydir: str = 'F:/Angular HTTP/7 T555' # PROD #


if __name__ == '__main__':

    # Trie par taille de fichiers
    # handle_files.order_files_option_start(mydir, '')

    # Renomme le nom des dossiers | Trie les dossiers par taille
    modify_folder = True
    handle_folder.scan_folders(mydir, modify_folder)

















