import os
from modules.Common import Common

class FileOrganizer:
    ''' Initialize variables '''
    def __init__(self):
        self.common = Common()
        self.currentFolder = ''
        self.currentFiles = ''

    ''' Request user for the name of the folder '''
    def fetchInput(self):
        print("Enter folder to organize:")
        try:
            folder = input()
        except:
            folder = ''

        # Check if folder is a directory and it exists
        if(os.path.isdir(folder) & os.path.exists(folder)):
            self.currentFolder = folder
            self.common.changeFolder(self.currentFolder)
        else:
            print("Invalid folder name, exiting.")

    ''' Check for folder's permission '''
    def folderPermission(self):
        return self.common.checkFolderPermission(self.currentFolder)

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
            try:
                for file in self.currentFiles:
                    folder = self.common.getFolderName(self.common.readMime(file))
                    self.common.createFolder(folder)
                    self.common.moveFileToFolder(folder, file)
            except e:
                print("Exception occured: %s" % e)
            finally:
                print("Process completed.")
