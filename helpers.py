'''helper functions '''

import os


def cwd() -> str:
    return os.path.dirname(os.path.realpath(__file__))
