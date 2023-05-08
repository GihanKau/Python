# import the parent class and the sub classes
from s14210_Q1_code import Sequence, Proteinseq, MRNAseq, DNAseq

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

s1 = Proteinseq(seq_info[0][1], seq_info[0][0], seq_info[0][2], seq_info[0][3], seq_info[0][4], seq_info[0][5], sequences[0])
s2 = Proteinseq(seq_info[1][1], seq_info[1][0], seq_info[1][2], seq_info[1][3], seq_info[1][4], seq_info[1][5], sequences[1])
s3 = Proteinseq(seq_info[2][1], seq_info[2][0], seq_info[2][2], seq_info[2][3], seq_info[2][4], seq_info[2][5], sequences[2])
s4 = Proteinseq(seq_info[3][1], seq_info[3][0], seq_info[3][2], seq_info[3][3], seq_info[3][4], seq_info[3][5], sequences[3])
s5 = DNAseq(seq_info[4][1], seq_info[4][0], seq_info[4][2], seq_info[4][3], sequences[4])
s6 = DNAseq(seq_info[5][1], seq_info[5][0], seq_info[5][2], seq_info[5][3], sequences[5])
s7 = DNAseq(seq_info[6][1], seq_info[6][0], seq_info[6][2], seq_info[6][3], sequences[6])
s8 = DNAseq(seq_info[7][1], seq_info[7][0], seq_info[7][2], seq_info[7][3], sequences[7])


print("-----------------------------OSDREB1A Details--------------------------------------")
print("Gene name : ", s5.gene_name)
print("Species Name : ", s5.sp_name)
print("Species Name : ", s5.subsp_name)

print("-------------------------------Question 2.I----------------------------------------")
# Q2.I Print Gene ID, sequence length, sequence type and the AT of the DREB1A DNA sequence

print("Gene ID : ", s5.gene_id)
print("Sequence Length : ", s5.seq_len)
print("Sequence Type : ", s5.seq_type)
print("AT content : ", s5.at_content)

print("-----------------------Question 2.II transcribed OSDREB2B--------------------------")
# Q2.II transcribe OSDREB2B

transcribed = s8.transcribed_sequence

s9 = MRNAseq(seq_info[7][1], seq_info[7][0], seq_info[7][2], seq_info[7][3],  transcribed)

print("Sequence Length : ", s9.seq_len)
print("Sequence Type : ", s9.seq_type)
print("AT Content : ", s9.at_content)
print("Transcribed sequence : ",transcribed)

print("---------------------Question 2.III translated OSDREB2B mRNA-----------------------")

# Q2. III. Translate the OSDREB2B mRNA sequence

print("Translation : ", s9.translated_sequence)
print("Length : ", len(s9.translated_sequence))

print("-------------------------Question 2.IV DREB2A Protein------------------------------")
# Q2. IV DREB2A Protein

print("Uniprot ID : ",s3.uniprot_id)
print("Reviewed Status : ", s3.reviewed_status)
print("Type : ", s3.seq_type)
print("Amino Acid Composition : ",s3.get_Character_Count())
print("Hydrophobicity : ",s3.hydrophobicity,"%")

print("--------------------------------Question 2.V---------------------------------------")

# Q2. V
print("No. of created sequences : ", Sequence.seq_count)

# END
