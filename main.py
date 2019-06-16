from libs.FileOrganizer import FileOrganizer

''' Execute the program '''
fileOrganizer = FileOrganizer()
fileOrganizer.initialize("/Users/gyro/Desktop")
#fileOrganizer.initialize("")

if(fileOrganizer.validateFolder()):
    if(fileOrganizer.folderPermission()):
        fileOrganizer.fetchFiles()
        fileOrganizer.organizeFiles()
