import os


def get_current_directory_filenames(dir=""):
    filenames = []

    for root, dirs, files in os.walk("." + dir):
        for filename in files:
            if filename[-3:] == '.py':
                filenames.append(filename)

    return filenames
