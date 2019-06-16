import unittest, os, sys
sys.path.append(os.path.abspath(sys.path[0]) + '/../')
from libs.FileOrganizer import FileOrganizer
from modules.Common import Common

class FileOrganizerTest(unittest.TestCase):

    ''' Initialize '''
    def setUp(self):
        self.fileOrganizer = FileOrganizer()
        self.common = Common()


    ''' Test Folder validation when output is True '''
    def test_validateFolderTrue(self):
        # Initialize
        current = os.getcwd()
        folder = os.path.join(current, "tests/artifacts")
        self.fileOrganizer.currentFolder = folder

        # Execute
        status = self.fileOrganizer.validateFolder()

        # Assert
        self.assertTrue(status)

        # Cleanup
        self.common.changeFolder(current)


    ''' Test Folder validation when output is False '''
    def test_validateFolderFalse(self):
        # Initialize
        current = os.getcwd()
        folder = os.path.join(current, "tests/arti")
        self.fileOrganizer.currentFolder = folder

        # Execute
        status = self.fileOrganizer.validateFolder()

        # Assert
        self.assertFalse(status)

        # Cleanup
        self.common.changeFolder(current)


    ''' Test folder's permission when output is True '''
    def test_folderPermissionTrue(self):
        # Initialize
        current = os.getcwd()
        folder = os.path.join(current, "tests/artifacts")
        self.fileOrganizer.currentFolder = folder

        # Execute
        status = self.fileOrganizer.folderPermission()

        # Assert
        self.assertTrue(status)


    ''' Check folder's permission when output is False '''
    def test_folderPermissionFalse(self):
        # Initialize
        folder = "/etc/apache2/extra"
        self.fileOrganizer.currentFolder = folder

        # Execute
        status = self.fileOrganizer.folderPermission()

        # Assert
        self.assertFalse(status)


    ''' Test fetching all the files from the folder '''
    def test_fetchFiles(self):
        # Initialize
        current = os.getcwd()
        folder = os.path.join(current, "tests/artifacts")

        # Execute
        self.common.changeFolder(folder)
        self.fileOrganizer.fetchFiles()

        # Assert
        self.assertEqual(2, len(self.fileOrganizer.currentFiles))

        # Cleanup
        self.common.changeFolder(current)


    ''' Test organizing files when folder is empty '''
    def test_organizeFilesEmpty(self):
        # Initialize
        self.fileOrganizer.currentFiles = []

        # Execute
        status = self.fileOrganizer.organizeFiles()

        # Assert
        self.assertFalse(status)



if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(FileOrganizerTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
