def find_key_signature(kern_file):
    """Return key signatures of kern file.
    
    Args:
        kern_file (str) -- text file (.krn or .txt) using Humdrum **kern format

    Returns:
        list -- list of key signatures for each track
                [
                #       Spline (track) 1
                #   ==========================
                    [key1, key2], [key1, key2],

                #       Spline (track) 2
                #   ==========================
                    [key1, key2], [key1, key2]
                    ]
    """
    pass
