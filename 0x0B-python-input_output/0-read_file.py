#!/usr/bin/python3
"""Module for read_file function"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    Args:
        filename (str): the name of the file
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
