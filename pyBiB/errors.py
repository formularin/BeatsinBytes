class BadKernError(ValueError):
    """Basic exception for kern files with invalid syntax.

    File must follow all kern syntax rules documented here:
    http://www.humdrum.org/guide/ch02/
    http://www.humdrum.org/guide/ch06/
    
    Attributes:
        kern_file -- path to kern file in which the error occurred.
        message -- explanation of the error.
    """
    def __init__(self, kern_file, 
        message="check Humdrum Documentation at http://www.humdrum.org/guide/ch02/ "
        "and http://www.humdrum.org/guide/ch06/ to make sure kern follows proper syntax"):
        ValueError.__init__(self, f'"{kern_file}"' + ' ' + message)\


class NoKeySignatureError(BadKernError):
    """Raised when key signature of kern file cannot be decected."""
    def __init__(self, kern_file):
        BadKernError.__init__(self, kern_file, "has no encoded key signature.\n"
            "Key signature must be encoded as *k followed by list (in brackets)"
            "containing list of flats and sharps in order specified by humdrum documentation")


class NoTimeSignatureError(BadKernError):
    """Raised when time signature of kern file cannot be detected."""
    def __init__(self, kern_file):
        BadKernError.__init__(self, kern_file, "Has no encoded time signature.\n"
            "Time signature must be encoded as *M followed by the time signature.")
