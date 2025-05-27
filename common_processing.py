"""
Save the common functions for loading txt into python objects and such

"""

import numpy as np
import re


def read_lines(text_file_path: str) -> list[str]:
    """
    read txt and return a list of lines
    """
    with open(text_file_path) as f:
        line_list = f.readlines()

    # Remove \n characters
    line_list = [
          line.replace("\n", "") for line in line_list
    ]

    return line_list


def as_integer_array(line_list: list[str]) -> np.array:
    """
    Try to interpret the loaded data as an array of iteger values

    """
    lines_as_integers = [re.findall(r"\d+", line) for line in line_list]

    return np.array(lines_as_integers).astype(int)
