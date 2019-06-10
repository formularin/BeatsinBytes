import analysisTools
import errors


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
    """
    def __init__(self):
        pass

    def average_note_value(self):
        pass

    def average_pitch(self):
        pass

    def average_steps(self):
        pass

    def key_signature(self):
        pass

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
