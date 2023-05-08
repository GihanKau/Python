'''
Algorithm to count nucleotide bases separately
in a given DNA sequence in FASTA format
Input : DNA sequence as a .fasta file
Output : Adenine count, Guanine count, Thymine Count, Cytosine count, Total Count
'''
# Initialize variables
total_count =0
adenine_count =0
guanine_count =0
thymine_count =0
cytosine_count=0

# open and read the file line by line
with open("sequence.fasta", "r") as seq_file:
    # for call lines in file
    for line in seq_file:
        # to remove the description line
        if ">" not in line:
            # to remove leading and trailing whitespaces and "\n" in lines
            line = line.strip(' \n')
            # for call bases in lines
            for base in line:
                if base == "A":
                    adenine_count += 1
                elif base == "G":
                    guanine_count += 1
                elif base == "T":
                    thymine_count += 1
                else:
                    cytosine_count += 1
                total_count += 1

seq_file.close()
print("Adenine count = ", adenine_count, "\n"
      "Guanine count = ", guanine_count, "\n"
      "Thymine count = ", thymine_count, "\n"
      "Cytosine count = ", cytosine_count, "\n"
      "Total count = ", total_count)
