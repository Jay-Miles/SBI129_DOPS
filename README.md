# STP Clinical Bioinformatics (Genomics)
## Programming (SBI129): Direct observation of practical skill

## DOPS 1

Write a program to create a reverse complement from a DNA sequence, and explain the development environment, the data source, the libraries used and the algorithm employed. 

Development environment
- OS: Linux, Ubuntu 22.04.1 LTS
- Code editor: Visual Studio Code v1.59.0

Data source:
- The original data is a text file ('sall2_A_original_sequence.txt') containing a FASTA DNA record
- This was obtained from the NCBI Nucleotide database - SALL2 gene RefSeqGene FASTA sequence
- https://www.ncbi.nlm.nih.gov/nuccore/NG_051069.1?from=15871&to=21137&report=fasta

Libraries:
- No external libraries used

Algorithm (in sbi129_dops_1.py):
- Read in entire file contents as a single string
- Confirm contents are in basic FASTA format using assertions
- Remove FASTA header from DNA sequence using a string slice
- Convert sequence to uppercase using .upper() string method
- Remove newline/return characters using .join() and list comprehension
- Replace non-nucleotide characters using .join() and list comprehension
- Reverse order of string characters using a string slice
- Get the complementary sequence using .join() and list comprehension
- Write the resulting sequence out to another text file

## DOPS 3

Write a set of unit tests to evaluate whether the output of a script or set of functions is correct, including edge cases.

test_sbi129_dops_3.py is a suite of pytest tests for functions in sbi129_dops_1.py. It can be run by executing 'pytest' on the command line from within the parent directory.
