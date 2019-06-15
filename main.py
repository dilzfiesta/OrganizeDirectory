from libs.FileOrganizer import FileOrganizer

''' Execute the program '''
fileOrganizer = FileOrganizer("/Users/gyro/Desktop") # Cron
#fileOrganizer = FileOrganizer("") # Interactive
if(fileOrganizer.validateFolder()):
    if(fileOrganizer.folderPermission()):
        fileOrganizer.fetchFiles()
        fileOrganizer.organizeFiles()
