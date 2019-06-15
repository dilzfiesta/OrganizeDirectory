import os
from modules.Common import Common

class FileOrganizer:

    ''' Initialize variables '''
    def __init__(self, folder):
        self.common = Common()
        self.currentFolder = ''
        self.currentFiles = ''

        if(folder != ""):
            self.currentFolder = folder
        else:
            self.fetchInput()

    ''' Request user for the name of the folder '''
    def fetchInput(self):
        print("Enter folder to organize:")
        try:
            folder = input()
        except:
            folder = ''

        self.currentFolder = folder

    ''' Validate Folder '''
    def validateFolder(self):
        return self.common.validateFolder(self.currentFolder)

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
            except:
                print("Exception occured")
            finally:
                print("Process completed.")
