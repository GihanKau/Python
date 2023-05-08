'''
Algorithm to measure the sequence length of a
given DNA sequence in FASTA format by using len()
Input : DNA sequence as a .fasta file
Output : Total length of the sequence
'''

# Initialize the variables
line_len= 0
# open and read the file line by line
with open("sequence.fasta", "r") as seq_file:
    # for call lines in file
    for line in seq_file:
        # to remove the description line
        if ">" not in line:
            # to remove leading and trailing whitespaces and "\n" in lines
            line = line.strip(' \n')
            line_len += len(line)

seq_file.close()
print("Total length of the sequence = ", line_len)
