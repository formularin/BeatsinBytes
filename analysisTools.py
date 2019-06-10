def grep(string, pattern):
    """Replicates Bash "grep" command.

    Takes string and outputs all lines containing certain pattern.
    
    Args:
        string -- string to search through
        pattern -- string to search for
    """
    lines = string.split('\n')

    lines_containing_pattern = []
    for line in lines:
        if pattern in line:
            lines_containing_pattern.append(line)

    if len(lines_containing_pattern) == 0:
        return False
    elif len(lines_containing_pattern) == 1:
        return lines_containing_pattern[0]
    else:
        return lines_containing_pattern


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
