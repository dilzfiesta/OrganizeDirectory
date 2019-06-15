from libs.FileOrganizer import FileOrganizer

''' Execute the program '''
fileOrganizer = FileOrganizer()
fileOrganizer.fetchInput()
if(fileOrganizer.folderPermission()):
    fileOrganizer.fetchFiles()
    fileOrganizer.organizeFiles()
