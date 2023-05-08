''''
Algorithm to translate a given mRNA sequence to its amino acid sequence
Input : Fasta file with the mRNA sequence, Text file with the amino acid codons table
Output : New fasta file with the translated amino acid sequence and length of the sequence
'''

# initiate the "seq_dict" dictionary (values are stored as a list)
seq_dict={"Codons":[], "Amino_acids":[],"mRNACodons":[],"mRNAs":[]}

# open the codon file
with open("codon_table.txt", "r") as seq:
    for line in seq:
        if '#' not in line:
            line = line.strip()
            line = (line.split('\t'))
            # take codons and amino acids into the seq_dict
            seq_dict['Codons'].append(line[0])
            seq_dict['Amino_acids'].append(line[2])
seq.close()

bases=""
# open the mRNA file
with open("OSDREB1A_mRNA.fasta", "r") as mRNA:
    for line in mRNA:
        if '>' not in line:
            line = line.strip()
            for base in line:
                # take mRNAs into the dictionary
                seq_dict['mRNAs'].append(bases+base)
mRNA.close()

count=0
codons=""

for nucleotide in seq_dict['mRNAs']:
    count+=1
    codons=codons+nucleotide
    if count%3==0:
        # make mRNAs into codons and store in the dict
        seq_dict['mRNACodons'].append(codons)
        codons=""
    else:
        continue

# i = index of 'mRNACodons' key
i=0
# convert mRNA codons into amino acids
# aa = amino acid
aa = seq_dict["Amino_acids"][seq_dict["Codons"].index(seq_dict['mRNACodons'][i])]
prot = ""
while aa not in "O":
    i = i + 1
    prot+=aa
    aa = seq_dict["Amino_acids"][seq_dict["Codons"].index(seq_dict['mRNACodons'][i])]

# total length of the translated seq
print("length of the translated sequence = ",len(prot))

# write aa into a new file
with open("Translated_sequence.fasta", "a") as aa_seq:
    aa_seq.write(">translated amino acid sequence\n"+prot)

aa_seq.close()
