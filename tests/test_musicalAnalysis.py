import os
import sys

u = os.getcwd().split("/")[2]
sys.path.append(f'/Users/{u}/BeatsinBytes')

import unittest
from pyBiB import musicalAnalysis

test_kern_directory = f'/Users/{u}/BeatsinBytes/test_kern/'


class TestKern(unittest.TestCase):

    def test_composer(self):
        beethoven_kern = musicalAnalysis.Kern(test_kern_directory + 'beethoven.txt')
        clementi_kern = musicalAnalysis.Kern(test_kern_directory + 'clementi.txt')
        mozart_kern = musicalAnalysis.Kern(test_kern_directory + 'mozart.krn')

        # composer name is Last, First
        self.assertEqual(beethoven_kern.composer, 'Ludwig van Beethoven')
        # composer name is First Last
        self.assertEqual(clementi_kern.composer, 'Muzio Clementi')
        # no specified composer in kern file
        self.assertEqual(mozart_kern.composer, 'unknown')

    def test_title(self):
        pass



if __name__ == '__main__':
    unittest.main()
