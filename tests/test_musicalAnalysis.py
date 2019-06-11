import os
import sys

u = os.getcwd().split("/")[2]
sys.path.append(f'/Users/{u}/BeatsinBytes')

import unittest
from pyBiB import musicalAnalysis

BiB_directory = f'/Users/{u}/BeatsinBytes/'
test_kern_directory = BiB_directory + 'test_kern/'
test_data_directory = BiB_directory + 'test_data/'


class TestKern(unittest.TestCase):

    def test_composer(self):
        # composer name is Last, First
        beethoven_kern = musicalAnalysis.Kern(test_kern_directory + 'beethoven.txt')
        # composer name is First Last
        clementi_kern = musicalAnalysis.Kern(test_kern_directory + 'clementi.txt')
        # no specified composer in kern file
        mozart_kern = musicalAnalysis.Kern(test_kern_directory + 'mozart.krn')

        self.assertEqual(beethoven_kern.composer, 'Ludwig van Beethoven')
        self.assertEqual(clementi_kern.composer, 'Muzio Clementi')
        self.assertEqual(mozart_kern.composer, 'unknown')

    def test_title(self):
        # title specified in kern file
        beethoven_kern = musicalAnalysis.Kern(test_kern_directory + 'beethoven.txt')
        # no specified title in kern file
        mozart_kern = musicalAnalysis.Kern(test_kern_directory + 'mozart.krn')

        self.assertEqual(beethoven_kern.title, 'Piano Sonata no. 1 in F minor')
        self.assertEqual(mozart_kern.title, 'mozart')

    def test_reference_records(self):

        with open(test_data_directory + 'mozart_reference_records.txt', 'r') as f:
            mozart_reference_records = f.read().split('\n')

        # no reference records
        beethoven_kern = musicalAnalysis.Kern(test_data_directory + 'beethoven_recordless.txt')
        # has reference records
        mozart_kern = musicalAnalysis.Kern(test_kern_directory + 'mozart.krn')

        self.assertEqual(beethoven_kern.reference_records, []) 
        self.assertEqual(mozart_kern.reference_records, mozart_reference_records)


if __name__ == '__main__':
    unittest.main()
