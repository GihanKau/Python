'''
Author      : B.M.G.G.K.Rajapaksha
Date        : 15/11/21
Practical   : 6
Question    : Use of Python modules for bioinformatics
'''

from Bio import SeqIO
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import re

# Part II
for seq_record in SeqIO.parse("ATdreb2a.fasta", "fasta"):
    print("ID : ", seq_record.id)
    print("Description : ", seq_record.description)
    print("Sequence : ", seq_record.seq)
    print("Sequence length : ", len(seq_record), "\n")

# Part III
fasta_string = open("ATdreb2a.fasta").read()
result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)

with open("dreb2a_blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()

result_handle = open("dreb2a_blast.xml")

# Part IV
blast_records = NCBIXML.parse(result_handle)
blast_record = next(blast_records)

E_VALUE_THRESH = 0.05
for alignment in blast_record.alignments:
    for hsp in alignment.hsps:
        if hsp.expect < E_VALUE_THRESH:
            print("****Alignment****")
            print("Blast hit title : ", alignment.title)
            print("Alignment length : ", alignment.length)
            print("E-value:", hsp.expect)
            print("Score : ", hsp.score)
            print("Hit/Subject sequence : ", hsp.sbjct[0:])
            print("Hit sequence length : ", abs(hsp.sbjct_start - hsp.sbjct_end), "\n")

# Part V
print("")
print("--------------Blast hits with the ABRE cis-acting ABA-dependent transcription factor binding element--------------")
seq_count = 0
for alignment in blast_record.alignments:

    for hsp in alignment.hsps:

        if hsp.expect < E_VALUE_THRESH:

            sequence = hsp.sbjct[0:]
            abre = re.finditer('[CT]ACGT[GT]C', sequence)

            for item in abre:
                if item.group()!= None:
                    print("sequence:", alignment.title)
                    print("Sequence fragment : ", item.group())
                    print("Sequence location : ", item.span(), "\n")
                    seq_count += 1

print("No.of BLAST hits with ABRE element present in the sequence : \n", seq_count)




