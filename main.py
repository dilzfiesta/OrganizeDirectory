import os
import sys
sys.path.insert(0, "modules")
import common

class FileOrganizer:
    ''' Initialize variables '''
    def __init__(self):
        self.currentFolder = ''
        self.currentFiles = ''

    ''' Request user for the name of the folder '''
    def fetchInput(self):
        print("Enter folder to organize:")
        try:
            folder = input()
        except:
            folder = ""

        # Check if folder is a directory and it exists
        if(os.path.isdir(folder) & os.path.exists(folder)):
            self.currentFolder = folder
            common.changeFolder(self.currentFolder)
        else:
            print("Invalid folder name, exiting.")

    ''' Check for folder's permission '''
    def folderPermission(self):
        return common.checkFolderPermission(self.currentFolder)

    ''' Fetch all the files from the folder and store them in list '''
    def fetchFiles(self):
        print("Fetching all files from %s" % (os.getcwd()))
        for root, dirs, files in os.walk(os.getcwd()):
            self.currentFiles = [f for f in files if not f[0] == '.']
            break

    ''' Organize files into folders and sub-folders '''
    def organizeFiles(self):
        if(len(self.currentFiles) == 0):
            print("Folder is empty. No files to organize, exiting.")
        else:
            print("Organizing files into sub-folders.")
            for file in self.currentFiles:
                folder = common.getFolderName(common.readMime(file))
                common.createFolder(folder)
                common.moveFileToFolder(folder, file)

''' Execute the program '''
if __name__ == '__main__':
    ob = FileOrganizer()
    ob.fetchInput()
    if(ob.folderPermission()):
        ob.fetchFiles()
        ob.organizeFiles()
