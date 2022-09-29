#!usr/bin/env python

""" Programming (SBI129): DOPS 3

Write a set of unit tests to evaluate whether the output of a script or
set of functions is correct, including edge cases.

Execute the command 'pytest' in the terminal to run the test suite. """


import sbi129_dops_1 as dops


def test_remove_header():
    """ Should return FASTA header and body separately """

    test_string = '>Fas\rta header\nFasta body\n'

    assert dops.remove_header(test_string) == (
        '>Fas\rta header', 'Fasta body\n')


def test_clean_input():
    """ Should return string as uppercase with newline/return characters
    removed, and non-nucleotide characters replaced with 'X' """

    test_string = 'm1x 0F Case5 \nAnd cHARA\rct3rs\n'

    assert dops.clean_input(test_string) == 'XXX XX CAXXX ANX CXAXACTXXX'


def test_reverse_string():
    """ Should return the reverse of the input string """

    test_string = 'this should be reversed'

    assert dops.reverse_string(test_string) == 'desrever eb dluohs siht'


def test_dna_complement():
    """ Should return string with nucleotides converted to complements """

    test_string = 'ACGTNX 123bcd'

    assert dops.dna_complement(test_string) == 'TGCANX 123bGd'


def test_in_combination():
    """ Given a FASTA-format string, should return the reverse complement
    of the body """

    test_string = '>Example header\nh0pEFul1Y yOu WoU\rLd n3ver acTUa1ly\n ' \
        'get A dNA sEqu\nENcx WHIch lo0ks \rl1K3 tHi5'

    header, parsed = dops.remove_header(test_string)
    cleaned = dops.clean_input(parsed)
    reversed = dops.reverse_string(cleaned)
    complement = dops.dna_complement(reversed)

    assert complement == 'XXXA XXXX XXXXX XGXXX XGNXXXXX TNX T AXC ' \
        'XXXTXAGT XXXXN XXXXX XXX XXXXXXXXX'
