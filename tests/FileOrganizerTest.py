import unittest, os, sys
sys.path.append(os.path.abspath(sys.path[0]) + '/../')
from libs.FileOrganizer import FileOrganizer

class FileOrganizerTest(unittest.TestCase):

    def setUp(self):
        self.fileOrganizer = FileOrganizer()

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(FileOrganizerTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
