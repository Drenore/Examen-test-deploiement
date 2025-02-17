import os
import tempfile
import zipfile
import pytest
import shutil

from backup_script import detect_os, get_home_directory, create_backup_archive

def test_detect_os():
    os_name = detect_os()
    assert os_name in ['Linux', 'Windows', 'Darwin']

def test_get_home_directory():
    home_dir = get_home_directory()
    assert os.path.isdir(home_dir)

def test_create_backup_archive():

    with tempfile.TemporaryDirectory() as temp_dir:
        test_file = os.path.join(temp_dir, 'test.txt')
        with open(test_file, 'w') as f:
            f.write("Hello World")
        

        archive_base = os.path.join(temp_dir, 'test_backup')
        archive_path = create_backup_archive(temp_dir, archive_base)
        

        assert archive_path is not None
        assert os.path.isfile(archive_path)
        

        with zipfile.ZipFile(archive_path, 'r') as zip_ref:
            namelist = zip_ref.namelist()
            # On cherche un chemin se terminant par "test.txt" (il peut être dans un sous-dossier).
            assert any(name.endswith('test.txt') for name in namelist)
