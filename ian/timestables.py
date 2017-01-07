"""
    Times Tables generation package
"""

import csv


def get(rows, cols):
    """
    Generate a list of times tables

    :param rows: Integer for the number of rows to generate
    :param cols: Integer for the number of columns to generate
    :return: List of lists containing tables numbers per row
    """
    return [x for x in generate(rows, cols)]


def generate(rows, cols):
    """
    Generator that generates rows for a times tables

    :param rows: Integer for the number of rows to generate
    :param cols: Integer for the number of columns to generate
    :yield: Lists containing tables numbers per row
    """
    for i in xrange(1, rows + 1):
        line = []
        for j in xrange(1, cols + 1):
            line.append(i * j)
        yield line


def write(rows, cols, filename):
    """
    Write a times table to a file

    :param rows: Integer for the number of rows to generate
    :param cols: Integer for the number of columns to generate
    :param filename: Output file path
    """
    with open(filename, 'wb') as f:
        writer = csv.writer(f)
        for line in generate(rows, cols):
            writer.writerow(line)
