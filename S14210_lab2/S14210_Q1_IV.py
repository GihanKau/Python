''''
Algorithm to correctly identify the mRNA records from the amino acid sequence.
This algorithm also replaces "T"s by "U"s.
Input = Fasta file with the amino acid sequence and mRNA sequence.
Output = New fasta file with the transcribed mRNA sequence.
'''

# initiate a dictionary names as sequences
sequences={}

# read the fasta file
with open("OSDREB1A.fasta","r") as fasta_file:
    seq_header=''
    for line in fasta_file:
        line=line.strip()
        # identify the keys in dictionary
        if">"in line:
            seq_header=line
            sequences[seq_header]=""
        # Add values to each key
        elif line!="\n":
            sequences[seq_header]=sequences[seq_header]+line
fasta_file.close()

# take keys in to a list
keys = list(sequences.keys())
# take values into a list
values = list(sequences.values())

count=0
# open a new file to write mRNA sequence
with open("OSDREB1A_mRNA.fasta", "a") as mRNA:
    # take the mRNA header from the keys list
    mRNA.write(keys[1] + " transcribed"+"\n")
    # take mRNAs from values list
    for base in values[1]:
        # define the length of a line in the file
        if count%70==0 and count!=0:
            mRNA.write("\n")
        count=count+1
        # replace "T"s by "U"
        if base == "T":
            mRNA.write("U")
        else:
            mRNA.write(base)
mRNA.close()


