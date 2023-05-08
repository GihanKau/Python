'''
Author      : B.M.G.G.K.Rajapaksha
Date        : 27/10/21
Question    : 2)II. A python program to read the sequences in
                    OSDREB_sequence.fasta file
input       : Multi sequence Fasta file
Output      : GeneID, sequence length, sequence type and base count
'''

# Import the sequence class
from S14210_lab4.s14210_Q2_I_code import Sequence

#if __name__ == "__main__":
with open("OSDREB_sequences.fasta", "r") as file:
    # Create an Sequence class object and implement fasta_split method
    seq_dict = Sequence.fasta_Split("self", file)
    # Take dictionary values into a list
seq_info = []
for item in seq_dict:
    dict_values = seq_dict[item]
    seq_info.append(dict_values)

# Take sequences from seq_info dictionary into a
# sequences list
sequences = []
seq_no = 0
total_characters= ""
while seq_no<4:
    seq= seq_info[seq_no][6:]
    for line in seq:
        for character in line:
            total_characters += character
    sequences.append(total_characters)
    seq_no = seq_no + 1
    total_characters = ""
if seq_no == 4:
    while seq_no <8:
        seq = seq_info[seq_no][4:]

        for line in seq:
            for character in line:
                total_characters = total_characters + character
        sequences.append(total_characters)
        seq_no = seq_no + 1
        total_characters = ""

# Create objects for each sequence

s1 = Sequence(seq_info[0][1], seq_info[0][0], seq_info[0][2], seq_info[0][3], sequences[0])
s2 = Sequence(seq_info[1][1], seq_info[1][0], seq_info[1][2], seq_info[1][3], sequences[1])
s3 = Sequence(seq_info[2][1], seq_info[2][0], seq_info[2][2], seq_info[2][3], sequences[2])
s4 = Sequence(seq_info[3][1], seq_info[3][0], seq_info[3][2], seq_info[3][3], sequences[3])
s5 = Sequence(seq_info[4][1], seq_info[4][0], seq_info[4][2], seq_info[4][3], sequences[4])
s6 = Sequence(seq_info[5][1], seq_info[5][0], seq_info[5][2], seq_info[5][3], sequences[5])
s7 = Sequence(seq_info[6][1], seq_info[6][0], seq_info[6][2], seq_info[6][3], sequences[6])
s8 = Sequence(seq_info[7][1], seq_info[7][0], seq_info[7][2], seq_info[7][3], sequences[7])

print("No. of sequences in the file : ", s8.seq_count)
print("Gene name : ", s5.gene_name)
print("Species Name : ", s5.sp_name)
print("Species Name : ", s5.subsp_name)
print("-------------------------------------------------------------------")

# Q2.II Print Gene ID, sequence length, and sequence type of the DREB1A DNA sequence

print("Gene ID : ", s5.gene_id)
print("Sequence Length : ", s5.seq_len)
print("Sequence Type : ", s5.seq_type)

# Q2.III Output of the Character count of DREB1A DNA sequence

print("Character Count : ", s5.get_Character_Count(sequences[4]))


#END
