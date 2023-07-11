#!/usr/bin/python3
""" appends a string """


def read_lines(filename="", nb_lines=0):
    """Reads n number of lines of a text file, and prints to stdout.

    Args:
        filename (str): name of file to be opened
        nb_lines (int): number of lines to read

    """
    line_count = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            line_count += 1
        if nb_lines <= 0 or nb_lines > line_count:
            nb_lines = line_count
        file.seek(0)
        for i in range(nb_lines):
            print(file.readline(), end='')
