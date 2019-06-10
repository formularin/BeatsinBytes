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
        song = f.read()

    lines = song.split('\n')

    reference_records = [line for line in lines
                         if line[:2] == '!!' and ':' in line]

    string_content_lines = [line for line in lines 
                            if line not in reference_records]
    
    content_lines = [line.split('\t') for line in string_content_lines]

    all_content_columns = [
        [line[i] for line in content_lines]
        for i in range(len(content_lines[0]))
        ]

    content_columns = [column for column in all_content_columns if column[0] == '**kern']

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
    
    content_lines = '\t'.join(prepare_kern_file(kern_file)[1])
    key_signature_lines = [line for line in content_lines if '*k[' in line]

    number_of_tracks_per_key_signature_line = [len(line.split('\t'))
                                               for line in key_signature_lines]
    tracks = [[] for i in
              range(number_of_tracks_per_key_signature_line)]

    for line in key_signature_lines:
        tracks_with_keysig = [track for track in line.split('\t') if '*k[' in line]
        for i, key_sig in enumerate(tracks_with_keysig):
            tracks[i].append(key_signature_from_kern(key_sig))
        
    return tracks
    
