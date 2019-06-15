import os, sys, unittest
sys.path.append(os.path.abspath(sys.path[0]) + '/../')
from shutil import copyfile
from modules.Common import Common

class CommonTest(unittest.TestCase):

    def setUp(self):
        self.common = Common()

    ''' Test MIME type from the file '''
    def test_readMime(self):
        # Assert
        self.assertEqual("image/png", self.common.readMime("artifacts/css-cheat-sheet-v1.png"))

    ''' Test folder name from the MIME type '''
    def test_getFolderName(self):
        # Initialize
        mime = self.common.readMime("artifacts/css-cheat-sheet-v1.png")

        # Assert
        self.assertEqual("Image/Png", self.common.getFolderName(mime))

    ''' Test chaning to user's supplied folder '''
    def test_changeFolder(self):
        # Initialize
        current = os.getcwd()
        folder = os.path.join(current, "tests/artifacts")

        # Execute
        self.common.changeFolder(folder)

        # Assert
        self.assertEqual(os.getcwd(), folder);

        # Cleanup
        self.common.changeFolder(current)

    ''' Test create folder if not already exists '''
    def test_createFolder(self):
        # Initialize
        current = os.getcwd()
        folder = os.path.join(current, "tests/artifacts/tmp")

        # Execute
        self.common.createFolder(folder)

        # Assert
        self.assertTrue(os.path.isdir(folder) & os.path.exists(folder))

        # Cleanup
        os.rmdir(folder)

    ''' Test moving files to the newly created folder '''
    def test_moveFileToFolder(self):
        # Initialize
        parent = os.path.join(os.getcwd(), "tests/artifacts")
        folder = os.path.join(parent, "tmp")
        file = "css-cheat-sheet-v1.png"
        newfile = "css-cheat-sheet-v1-new.png"

        # Execute
        self.common.changeFolder(parent)
        copyfile(file, newfile)
        self.common.createFolder(folder)
        self.common.moveFileToFolder(folder, newfile)

        # Assert
        self.assertTrue(os.path.isfile(os.path.join(folder, newfile)))

        # Cleanup
        os.remove(os.path.join(folder, newfile))
        os.rmdir(folder)

    ''' Test folder's permission when output is True '''
    def test_checkFolderPermissionTrue(self):
        # Initialize
        folder = os.path.join(os.getcwd(), "tests/artifacts")

        # Execute
        self.common.checkFolderPermission(folder)

        # Assert
        self.assertTrue(folder)

    ''' Check folder's permission when output is False '''
    def test_checkFolderPermissionFalse(self):
        # Initialize
        folder = "/etc/apache2/extra"

        # Execute
        self.common.checkFolderPermission(folder)

        # Assert
        self.assertTrue(folder)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(CommonTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
