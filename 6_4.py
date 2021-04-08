import tarfile
from pathlib import Path
import os
import sys

TESTS_DIR_NAME = 'testy'
PYTHON_DIR = 'C:/Users/mwisniew/AppData/Local/Programs/Python/Python38/'
MODES = ['', 'gz', 'bz2', 'xz']


if __name__ == '__main__':
    homePath = Path.home()
    testsPath = os.path.join(homePath, TESTS_DIR_NAME)
    if TESTS_DIR_NAME not in os.listdir(homePath):
        os.mkdir(testsPath)

    files = [os.path.join(PYTHON_DIR, file) for file in os.listdir(PYTHON_DIR)
             if os.path.isfile(os.path.join(PYTHON_DIR, file))]

    print(f'Test dir:')
    print(f'    {testsPath}')
    print(f'Python\'s dir:')
    print(f'    {PYTHON_DIR}')
    print(
        f'Liczba plików: {len(files)} rozmiar {sum(os.path.getsize(f) for f in files)} B')

    results = []
    for m in MODES:
        archivePath = os.path.join(
            testsPath, f'ppath.{m or "tar"}')
        mode = f'x:{m}'
        try:
            print(f'Tworzenie:')
            print(f'    {archivePath}')
            archive = tarfile.open(archivePath, mode=mode)
            for f in files:
                archive.add(f, recursive=False)
            archive.close()
            results.append(
                f'tryb: {mode} ; size: {os.path.getsize(archivePath)} B')
        except FileExistsError:
            results.append(
                f'tryb: {mode} ; error, file already exists')
    print('Wyniki')
    for r in results:
        print(f'    {r}')
