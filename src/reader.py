# Author: Louis-Clément LEROUX
# File: reader.py
# Date: 06/09/19
# Desc: Read extern files


def readTableStat():
    """Read the frecency of letters in a language.

    Output :
    A table mapping each letter with a frequency.

    """
    with open('statsEn.txt', 'r') as data:
        table = {}
        line = data.readline()

        while line:
            lineSplit = line.split()
            table[lineSplit[0]] = lineSplit[1]
            line = data.readline()

    return table

