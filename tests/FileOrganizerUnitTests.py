import unittest, os, sys
sys.path.append(os.path.abspath(sys.path[0]) + '/../')
from mock import mock, patch, create_autospec
from libs.FileOrganizer import FileOrganizer
from modules.Common import Common

class FileOrganizerTest(unittest.TestCase):

    ''' Request user for the name of the folder '''
    #def test_fetchInput(self):
    #    with patch.object(FileOrganizer, 'rawInput', return_value=None) as mocked_rawInput:
    #        FileOrganizer.rawInput("/Users/gyro/Desktop")

    #    mocked_rawInput.assert_called_once_with("/Users/gyro/Desktop")
        #FileOrganizer.fetchInput()

        #self.assertEqual(FileOrganizer.currentFolder, "/Users/gyro/Desktop")

    @mock.patch('libs.FileOrganizer.rawInput', autospec=True)
    def test_fetchInput(mocked_input):
        mocked_input.return_value = "/Users/gyro/Desktop"
        thing = FileOrganizer("")
        assert(thing.fetchInput())

        mocked_input.assert_called()


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(FileOrganizerTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
