import os


def get_current_directory_filenames(path="."):
    filenames = []

    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename[-3:] == '.py':
                filenames.append(path + '/' + filename)

    return filenames

