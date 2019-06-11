import os
import sys

u = os.getcwd().split("/")[2]
BiB_directory = f'/Users/{u}/BeatsinBytes/'
test_kern_directory = BiB_directory + 'test_kern/'
test_data_directory = BiB_directory + 'test_data/'
sys.path.append(BiB_directory)

from pyBiB import analysisTools
from pyBiB import errors
import unittest


class TestAnalysisTools(unittest.TestCase):

    def test_find_key_signature(self):
        # file has both declaration and regular encoded key signature
        self.assertEqual(
            analysisTools.find_key_signature(test_kern_directory + 'beethoven.txt'),
            [['F Minor'] for i in range(2)]
            )
        
        # file has no declaration
        self.assertEqual(
            analysisTools.find_key_signature(test_kern_directory + 'mozart.krn'),
            [['G Major'] for i in range(4)]
            )

        # file has no encoded key signature
        self.assertRaises(
            errors.NoKeySignatureError, 
            analysisTools.find_key_signature, 
            test_data_directory + 'clementi_without_key.txt'
            )


if __name__ == '__main__':
    unittest.main()
