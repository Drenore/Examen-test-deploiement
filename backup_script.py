import os
import platform
import shutil

def detect_os():
    return platform.system()

def get_home_directory():

    return os.path.expanduser("~")

def create_backup_archive(home_dir, archive_name='backup'):

    try:
        archive_path = shutil.make_archive(archive_name, 'zip', home_dir)
        return archive_path
    except Exception as e:
        print("Erreur lors de la création de l'archive :", e)
        return None

def main():
    os_name = detect_os()
    print("OS détecté :", os_name)
    
    home_dir = get_home_directory()
    print("Répertoire personnel :", home_dir)
    
    answer = input("Voulez-vous créer une archive de sauvegarde de votre répertoire personnel ? (o/n) : ")
    if answer.lower() in ['o', 'oui']:
        archive_path = create_backup_archive(home_dir)
        if archive_path:
            print("Archive créée avec succès :", archive_path)
        else:
            print("Échec de la création de l'archive.")
    else:
        print("Sauvegarde annulée.")

if __name__ == '__main__':
    main()
