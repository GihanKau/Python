'''
Author      : B.M.G.G.K.Rajapaksha
Date        : 27/10/21
Question    : 2)I. A python sequence class to store any biological sequence
'''

class Sequence:
    # Attributes
    gene_id = ""
    gene_name = ""
    seq_type = ""
    seq_len = ""
    seq_count = 0
    sp_name = ""
    subsp_name = ""

    '''
    Question    : 2)VIII. Constructor method
    Input       : Gene ID and Gene Name
    Output      : Gene ID, Gene Name and Sequence Count
    '''

    def __init__(self, gene_id, gene_name, sp_name, subsp_name, sequence):
        self.gene_id = gene_id
        self.gene_name = gene_name
        self.seq_type = self.get_Seq_Type(sequence)
        self.seq_len = len(sequence)
        self.sp_name = sp_name
        self.subsp_name = subsp_name
        Sequence.seq_count += 1

    '''
    Question    : 2)IX. A static method to split multiple FASTA sequences in a
                  single text file
    Input       : A Fasta file contains multiple sequences
    Output      : A dictionary containing sequences
    '''

    @staticmethod
    def fasta_Split(self, file):
        # Initiate the dictionary
        sequences = {}
        values = []
        for line in file:
            line = line.strip()
            if ">" in line:
                line = line.strip(">")
                line = line.split('-')
                values = line
                seq_header = values[0]

            elif line != "\n":
                values.append(line)
                sequences[seq_header] = values

        return (sequences)

    '''
    Question    : 2)X. A static method to check sequence type
    Input       : A sequence (DNA, mRNA, Protein)
    Output      : Sequence type
    '''

    def get_Seq_Type(self, sequence):
        # sequence is a string variable
        # "M" = Methionine, "A" = Adenine, "T" = Thymine

        if "M" not in sequence and "T" in sequence:
            self.seq_type = "DNA"
            return self.seq_type
        elif "M" not in sequence and "U" in sequence:
            self.seq_type = "mRNA"
            return self.seq_type
        else:
            self.seq_type = "Amino acid"
            return self.seq_type

    '''
    Question    : 2)XI. A method to create a dictionary of a character counts
                        with each character as the key and count as the value
                        
    Input       : A sequence (DNA, mRNA, Protein)
    Output      : A dictionary of A character counts
    '''

    def get_Character_Count(self, sequence):

        # Initiate the dictionary
        character_dict ={}
        for character in sequence:
            if character in character_dict:
                character_dict[character]+=1
            else:
                character_dict[character]=1
        return character_dict


#END






