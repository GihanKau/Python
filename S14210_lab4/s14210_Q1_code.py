'''
Author      : B.M.G.G.K.Rajapaksha
Date        : 27/10/21
Question    : 1)III. A custom method to calculate the AT content of a given DNA sequence.
Input       : A DNA sequence
Output      : AT content as a fraction
'''

def at_Content(sequence):
    # "sequence" argument is a string variable.
    # "M" = Methionine, "A" = Adenine, "T" = Thymine
    if "M" not in sequence and "T" in sequence:
        seq_len= len(sequence)
        a_content=0
        t_content=0
        for base in sequence:
            if base == "A":
                a_content += 1
            elif base == "T":
                t_content += 1
            else:
                continue
        # Calculate and round the at content into two decimal points
        at_content = round((a_content+t_content)/seq_len, 2)
        return at_content
    else:
        at_content = "Not Applicable"
        return at_content


'''
Question    : 1)IV. A custom method to split multiple FASTA sequences 
                     in single test file and to return a dictionary containing
                     sequence headers as keys and the sequences as values.
    
Input       : A fasta file containing multiple FASTA sequences 
Output      : A dictionary containing sequence headers as keys and the sequences 
              as values.
'''

def file_Split(file):
    # file is the file that contains the fasta sequences.
    sequences = {}
    seq_header = ''
    for line in file:
        line = line.strip()

        if ">" in line:
            seq_header = line
            # identify the headers as keys in dictionary
            sequences[seq_header] = ""

        elif line != "\n":
            # Add sequence characters as values to each key
            sequences[seq_header] = sequences[seq_header] + line

    return sequences


'''
Question    : 1)V. A custom method to check the type of a given sequence is DNA, mRNA, 
                   or Amino acid sequence.
                   
Input       : A DNA, mRNA, or Amino Acid sequence
Output      : Type of the sequence
'''

def get_Seq_Type(sequence):
    # "sequence" argument is a string variable.
    # "M" = Methionine, "T" = Thymine, "U" = Uracil
    if "M" not in sequence and "T" in sequence:
        seq_type = "DNA"
        return seq_type
    elif "M" not in sequence and "U" in sequence:
        seq_type = "mRNA"
        return seq_type
    else:
        seq_type = "Amino acid"
        return seq_type


'''
Question    : 1)VI. Implementation of three methods to check each sequence in the
                    OSDREB_sequences.fasta file and print the AT content
Input       : OSDREB_sequences.fasta file
Output      : Type of the each sequence and AT content of DNA sequences as a fraction.
'''

with open("OSDREB_sequences.fasta", "r") as file:
    seq_dict = file_Split(file)

    print("Sequence Dictionary : ", seq_dict, "\n")

    for item in seq_dict:
        gene_name = item.replace(">", "")
        sequence = seq_dict[item]
        seq_type = (get_Seq_Type(sequence))
        at_content = (at_Content(sequence))

        print("Sequence Description : ", gene_name, "||", "Sequence Type : ", seq_type,
              "||", "AT Content : ", at_content)
#END