import os
from mimetypes import MimeTypes

''' Extract MIME type from the file '''
def readMime(file):
    mime = MimeTypes()
    return mime.guess_type(file)[0]

''' Prepare folder name from the MIME type '''
def getFolderName(file):
    parent, offspring = file.split('/')
    children = offspring.split('.')
    return os.path.join(parent.title(), children[len(children) - 1].title())

''' Change to the user's supplied folder '''
def changeFolder(folder):
    #print("Changing current folder to %s" % (self.currentFolder))
    os.chdir(folder)

''' Create folder if not already exists '''
def createFolder(folder):
    if not os.path.exists(folder):
        #print("Creating folder: %s" % (folder))
        os.makedirs(folder)

''' Move files to the newly created folder '''
def moveFileToFolder(folder, file):
    #print("Moving %s to %s" % (file, folder))
    os.rename(file, os.path.join(folder, file))

''' Check for folder's permission '''
def checkFolderPermission(folder):
    #print("Checking for read, write and execute permissions on the folder")
    if(os.access(folder, os.R_OK) &
        os.access(folder, os.W_OK) &
        os.access(folder, os.X_OK)):
        #print("User have permission to access %s" % (folder))
        return True
    else:
        #print("User does not have permission to access %s" % (folder))
        return False
