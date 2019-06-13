import os
from mimetypes import MimeTypes

class FileOrganizer:
    ''' Initialize variables '''
    def __init__(self):
        self.currentFolder = ''
        self.currentFiles = ''
        self.mime = MimeTypes()

    ''' Request user for the name of the folder '''
    def inputFolder(self):
        print("Enter name of the folder to organize:")
        while(True):
            try:
                folder = input()
            except:
                folder = ""

            # Check if folder is a directory and it exists
            if(os.path.isdir(folder) & os.path.exists(folder)):
                self.currentFolder = folder
                break
            else:
                print("Invalid folder name, please re-enter name of the folder to organize:")

    ''' Check for folder's permission '''
    def checkFolderPermission(self):
        print("Checking for read, write and execute permissions on the folder")
        if(os.access(self.currentFolder, os.R_OK) &
            os.access(self.currentFolder, os.W_OK) &
            os.access(self.currentFolder, os.X_OK)):
            return True
        else:
            return False

    ''' Change to the user's supplied folder '''
    def changeFolder(self):
        print("Changing current folder to %s" % (self.currentFolder))
        os.chdir(self.currentFolder)

    ''' Fetch all the files from the folder and store them in list '''
    def fetchFiles(self):
        print("Fetching all files from %s" % (os.getcwd()))
        for root, dirs, files in os.walk(os.getcwd()):
            self.currentFiles = [f for f in files if not f[0] == '.']
            break

    ''' Extract MIME type from the file '''
    def readMime(self, file):
        return self.mime.guess_type(file)[0]

    ''' Identify folder name from the MIME type '''
    def getFolderName(self, file):
        parent, offspring = file.split('/')
        children = offspring.split('.')
        return os.path.join(parent.title(), children[len(children) - 1].title())

    ''' Create folder if not already exists '''
    def createFolder(self, folderName):
        if not os.path.exists(folderName):
            print("Creating folder: %s" % (folderName))
            os.makedirs(folderName)

    ''' Move files to the newly created folder '''
    def moveFileToFolder(self, folder, file):
        print("Moving %s to %s" % (file, folder))
        os.rename(file, os.path.join(folder, file))

    ''' Organize files into folders and sub-folders '''
    def organizeFiles(self):
        if(len(self.currentFiles) == 0):
            print("Folder is empty. No files to organize")
        else:
            print("Organizing files: %s" % (self.currentFiles))
            for file in self.currentFiles:
                folder = self.getFolderName(self.readMime(file))
                self.createFolder(folder)
                self.moveFileToFolder(folder, file)

''' Execute the program '''
if __name__ == '__main__':
    ob = FileOrganizer()
    ob.inputFolder()
    if(ob.checkFolderPermission()):
        ob.changeFolder()
        ob.fetchFiles()
        ob.organizeFiles()
