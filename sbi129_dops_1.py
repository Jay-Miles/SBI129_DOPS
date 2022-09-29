#!usr/bin/env python

""" Programming (SBI129): DOPS 1

Write a program to create a reverse complement from a DNA sequence,
and explain the development environment, the data source, the libraries
used and the algorithm employed. 

Development environment
- OS: Linux, Ubuntu 22.04.1 LTS
- Code editor: Visual Studio Code v1.59.0

Data source:
- NCBI Nucleotide database - SALL2 gene RefSeqGene FASTA sequence
- https://www.ncbi.nlm.nih.gov/nuccore/NG_051069.1?from=15871&to=21137&report=fasta

Libraries:
- No external libraries used

Algorithm:
- Original data is a text file containing a FASTA DNA record
- Read in entire file contents as a single string
- Confirm contents are in basic FASTA format using assertions
- Remove FASTA header from DNA sequence using a string slice
- Convert sequence to uppercase using .upper() string method
- Remove newline/return characters using .join() and list comprehension
- Replace non-nucleotide characters using .join() and list comprehension
- Reverse order of string characters using a string slice
- Get the complementary sequence using .join() and list comprehension
- Write the resulting sequence out to another text file
"""


def read_file(input_file):
    """ Read in a text file as a single string """

    with open(input_file, 'r') as reader:
        file_contents = reader.read()

    return file_contents


def confirm_fasta_format(text_string):
    """ Check that the file contents have a basic FASTA format """

    assert text_string[0] == '>', "FASTA records should begin with '>'"

    assert '\n' in text_string, "FASTA header/body should be separated by '\n"


def remove_header(file_contents):
    """ Parse a string representing a fasta record to remove the header """

    first_newline = file_contents.find('\n')

    header = file_contents[:first_newline]
    dna_sequence = file_contents[first_newline + 1:]

    return header, dna_sequence


def clean_input(dna_sequence):
    """ Given a string representing a DNA sequence, convert all letters
    to uppercase. Remove any newline or carriage return characters.
    Replace any non-nucleotide characters with 'X', but retain spaces as
    legitimate sequence gaps. """

    # convert to uppercase

    capitalised = dna_sequence.upper()

    # remove newlines and carriage returns

    no_newlines = ''.join([char for char in capitalised \
        if char not in ['\n', '\r']])

    # replace non-nucleotide characters with 'X'

    keep = ['A', 'C', 'G', 'T', 'N', ' ']

    cleaned = ''.join([char if char in keep \
        else 'X' for char in no_newlines])

    return cleaned


def reverse_string(input):
    """ Reverse the order of characters in a string """

    output = input[::-1]

    return output


def dna_complement(dna_sequence):
    """ Given a string, return another where all nucleotides are
    converted to their uppercase complements and all other characters
    are unchanged """

    map = {
        'a' : 'T',
        'A' : 'T',
        'c' : 'G',
        'C' : 'G',
        'g' : 'C',
        'G' : 'C',
        't' : 'A',
        'T' : 'A'}

    output_sequence = ''.join([map[char] if char in map.keys() \
        else char for char in dna_sequence])

    return output_sequence


def write_text(fp, header, string):
    """ Create a text file at the specified filepath from the supplied
    string """

    header += ' REVERSE COMPLEMENT\n'

    with open(fp, 'w') as writer:
        writer.write(header)
        writer.write(string)


def main():

    dna_file = 'sall2_A_original_sequence.txt'
    output_file = 'sall2_B_rev_com.txt'

    file_contents = read_file(dna_file)

    confirm_fasta_format(file_contents)

    header, dna_sequence = remove_header(file_contents)
    cleaned = clean_input(dna_sequence)
    reversed = reverse_string(cleaned)
    complement = dna_complement(reversed)

    write_text(output_file, header, complement)


if __name__ == '__main__':
    main()
