import os

class file:
    def __init__(self, filename, filesize):
        self.filename = filename
        self.filesize = filesize

def GetCurrentDirectoryFilenames():

    files = []

    for root, dirs, files in os.walk("."):
        for filename in files:
            if filename[-3:] == '.py':
                files.append(file(filename, os.path.getsize(filename)))

    return files

