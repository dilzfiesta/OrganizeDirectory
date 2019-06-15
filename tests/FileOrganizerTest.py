import unittest, os, sys
sys.path.append(os.path.abspath(sys.path[0]) + '/../')
from libs.FileOrganizer import FileOrganizer

class FileOrganizerTest(unittest.TestCase):

    def setUp(self):
        self.fileOrganizer = FileOrganizer()

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(FileOrganizerTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
