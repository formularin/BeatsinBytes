import os
import sys

u = os.getcwd().split("/")[2]
sys.path.append(f'/Users/{u}/BeatsinBytes')

from pyBiB import errors
import string


def check_equal(iterator):
    """Checks if all elements in list are equal"""
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)


def prepare_kern_file(kern_file):
    """Outputs often useful lists from kern file
    
    Args:
        kern_file (str) -- absolute path to text file (.krn or .txt) 
                           using Humdrum **kern format
    
    Returns:
        list -- [reference_records, content_lines, content_columns]
                references_records (list): kern metadata
                content_lines (list): lines containing kern information
                content_columns (list): columns containing kern information
    """
    with open(kern_file, 'r') as f:
        song = f.read().strip()

    lines = song.split('\n')

    rr_first_chunk_end = 0
    line = lines[rr_first_chunk_end]
    while '**' not in line and '!!' in line and ':' in line:
        rr_first_chunk_end += 1
        line = lines[rr_first_chunk_end]

    rr_second_chunk_begin = rr_first_chunk_end
    line = lines[rr_second_chunk_begin]
    while '*-' not in line:
        rr_second_chunk_begin += 1
        line = lines[rr_second_chunk_begin]
    
    rr_second_chunk_begin += 1

    reference_records = lines[:rr_first_chunk_end] + lines[rr_second_chunk_begin:]

    string_content_lines = [line for line in lines 
                            if line not in reference_records]
    
    content_lines = [line.split('\t') for line in string_content_lines]

    lengths = [len(line) for line in content_lines]

    r = []
    for l, line in zip(lengths, content_lines):
        if l < lengths[0]:
            r.append(content_lines.index(line))

    removables = [content_lines[i] for i in r]
    for removable in removables:
        content_lines.remove(removable)

    all_content_columns = [[line[i] for line in content_lines]
                            for i in range(len(content_lines[0]))]

    content_columns = [column for column in all_content_columns if column[0] == '**kern']

    content_lines = [[column[i] for column in content_columns]
                     for i in range(len(content_columns[0]))]

    return [reference_records, content_lines, content_columns]



def find_key_signature(kern_file):
    """Return key signatures of kern file.
    
    Args:
        kern_file (str) -- absolute path to text file (.krn or .txt) 
                           using Humdrum **kern format

    Returns:
        list -- list of key signatures for each track
                [
                #       spline (track) 1
                #   ==========================
                    [key1, key2], [key1, key2],

                #       spline (track) 2
                #   ==========================
                    [key1, key2], [key1, key2]
                    ]
                if there no key signature for a track
                (ex. percussion instrument), then track list is empty
    """

    def key_signature_from_kern(kern):
        
        key_signature = ''

        if kern == '*k[]':
            key_signature = 'C Major'

        elif kern == '*k[f#]':
            key_signature = 'G Major'

        elif kern == '*k[f#c#]':
            key_signature = 'D Major'

        elif kern == '*k[f#c#g#]':
            key_signature = 'A Major'

        elif kern == '*k[f#c#g#d#]':
            key_signature = 'E Major'

        elif kern == '*k[f#c#g#d#a#]':
            key_signature = 'B Major'

        elif kern == '*k[f#c#g#d#a#e#]':
            key_signature = 'F# Major'

        elif kern == '*k[f#c#g#d#a#e#b#]':
            key_signature = 'C# Major'

        elif kern == '*k[b-]':
            key_signature = 'F Major'

        elif kern == '*k[b-e-]':
            key_signature = 'Bb Major'

        elif kern == '*k[b-e-a-]':
            key_signature = 'Eb Major'

        elif kern == '*k[b-e-a-d-]':
            key_signature = 'Ab Major'

        elif kern == '*k[b-e-a-d-g-]':
            key_signature = 'Db Major'

        elif kern == 'k*[b-e-a-d-g-c-]':
            key_signature = 'Gb Major'

        elif kern == 'k*[b-e-a-d-g-c-f-]':
            key_signature = 'Cb Major'

        return key_signature

    content_lines = ['\t'.join(line) for line in prepare_kern_file(kern_file)[1]]
    declarations = [line for line in content_lines 
                if '*' in line and ':' == line[-1]]

    def tracks_from_keysigs(keysigs):
        line_lengths = [len(i) for i in keysigs]

        tracks = [[line[i] for line in keysigs]
                  for i in range(len(
                      keysigs[line_lengths.index(max(line_lengths))]
                      ))]

        return tracks

    if declarations != []:
        keysigs = [d.split('\t') for d in declarations]
        
        # list containing raw kern in format of output
        tracks = tracks_from_keysigs(keysigs)

        output = []
        for track in tracks:
            siglist = []
            for sig in track:
                tonic = [i for i in sig
                         if i in string.ascii_letters][0]
                major_or_minor = 'Major'
                if tonic in string.ascii_lowercase:
                    major_or_minor = 'Minor'
                key_signature = '{} {}'.format(tonic.upper(), major_or_minor)
                siglist.append(key_signature)

            output.append(siglist)

        return output

    else:
        
        keysig_lines = [line for line in content_lines
                        if '*k[' in line]

        if keysig_lines == []:
            raise errors.NoKeySignatureError(kern_file)

        keysigs = [line.split('\t') for line in keysig_lines]

        # list containing final output
        tracks = tracks_from_keysigs(keysigs)

        output = [[key_signature_from_kern(i) for i in track] for track in tracks]

        return output
        
