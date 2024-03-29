import os
import sys

u = os.getcwd().split("/")[2]
sys.path.append(f'/Users/{u}/BeatsinBytes')

from pyBiB import analysisTools


class Kern:
    """Song using humdrum **kern encoding.
    
    Object used to measure musical analysis metrics of a song.
    Methods based off of Beats in Bytes musical analysis shell scripts.

    Notes:
        File must follow all kern syntax rules documented here:
        http://www.humdrum.org/guide/ch02/
        http://www.humdrum.org/guide/ch06/
        http://www.humdrum.org/rep/kern/
    
    Attributes:
        file_path -- path to kern file in UTF-8 encoding. Extension can be '.krn' or '.txt'
        
        title -- title of song 
                 (if not provided will look in reference records. 
                 If not in reference records will use file name without extension)
        
        composer -- composer of song
                    (if not provided will look in reference records. 
                    If not in reference records will default to "unknown")
        reference_records -- metadata in kern file
    """
    def __init__(self, file_path, title=None, composer=None):
        self.file_path = file_path

        self.reference_records = analysisTools.prepare_kern_file(self.file_path)[0]

        # title was specified in initialization
        if title != None:
            self.title = title

        # title was not specified in initialization
        else:
            title_line = ''
            for line in self.reference_records:
                if '!!!OTL:' in line:
                    title_line = line

                # no stated title in kern file
                if title_line == '':
                    self.title = self.file_path.split('/')[-1].split('.')[0]
                else:
                    self.title = title_line.split(':')[1].strip()
        
        

        # composer was specified in initialization
        if composer != None:
            self.composer = composer
        
        # composer was not specified in initialization
        else:
            composer_line = ''
            for line in self.reference_records:
                if '!!!COM:' in line:
                    composer_line = line

            # no stated composer in kern file
            if composer_line == '':
                self.composer = 'unknown'
            else:
                composer_raw = composer_line.split(':')[1].strip()
                if ',' in composer_raw:
                    composer_list = [name.strip() for name in composer_raw.split(',')]
                    self.composer = '{} {}'.format(composer_list[1], composer_list[0])

                else:
                    self.composer = composer_raw


    def average_note_value(self):
        pass

    def average_pitch(self):
        pass

    def average_steps(self):
        pass

    def key_signature(self):
        return analysisTools.find_key_signature(self.file_path)

    def most_used_note_value(self):
        pass

    def most_used_pitch(self):
        pass

    def repeated_note_value(self):
        pass

    def repeated_pitches(self):
        pass

    def rhythmic_themes(self):
        pass

    def scales(self):
        pass

    def tempo(self):
        pass

    def time_signature(self):
        pass
