import os
from mimetypes import MimeTypes

class Common:
    def __init__(self):
        self.mime = MimeTypes()

    ''' Extract MIME type from the file '''
    def readMime(self, file):
        return self.mime.guess_type(file)[0]

    ''' Validate folder '''
    def validateFolder(self, folder):
        print("Validating %s" % folder)
        if(os.path.isdir(folder) & os.path.exists(folder)):
            self.changeFolder(folder)
            return True
        else:
            print("Invalid folder, exiting.")
            return False

    ''' Prepare folder name from the MIME type '''
    def getFolderName(self, file):
        parent, offspring = file.split('/')
        children = offspring.split('.')
        return os.path.join(parent.title(), children[len(children) - 1].title())

    ''' Change to the user's supplied folder '''
    def changeFolder(self, folder):
        #print("Changing current folder to %s" % (folder))
        os.chdir(folder)

    ''' Create folder if not already exists '''
    def createFolder(self, folder):
        if not os.path.exists(folder):
            #print("Creating folder: %s" % (folder))
            os.makedirs(folder)

    ''' Move files to the newly created folder '''
    def moveFileToFolder(self, folder, file):
        #print("Moving %s to %s" % (file, folder))
        os.rename(file, os.path.join(folder, file))

    ''' Check folder's permission '''
    def checkFolderPermission(self, folder):
        #print("Checking for read, write and execute permissions on %s" % folder)
        if(os.access(folder, os.R_OK) &
            os.access(folder, os.W_OK) &
            os.access(folder, os.X_OK)):
            #print("User have permission to access %s" % (folder))
            return True
        else:
            #print("User does not have permission to access %s" % (folder))
            return False
