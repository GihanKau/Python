'''
Author      : B.M.G.G.K.Rajapaksha
Date        : 27/10/21
Practical   : 4
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
        self.sequence =sequence
        self.gene_id = gene_id
        self.gene_name = gene_name
        self.seq_type = self.get_Seq_Type()
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

    def get_Seq_Type(self):
        sequence=self.sequence
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

    def get_Character_Count(self):
        sequence = self.sequence
        # Initiate the dictionary
        character_dict = {}
        for character in sequence:
            if character in character_dict:
                character_dict[character] += 1
            else:
                character_dict[character] = 1
        return character_dict


'''
Author      : B.M.G.G.K.Rajapaksha
Date        : 4/11/21
Practical   : 5
Question    : 1) Write subclasses for DNA, mRNA, and amino acid sequences 
'''
# ****************************************DNA sub class***********************************************

class DNAseq(Sequence):
    at_content = 0
    transcribed_sequence = ""

    def __init__(self, gene_id, gene_name, sp_name, subsp_name, sequence):
        super().__init__(gene_id, gene_name, sp_name, subsp_name, sequence)
        self.sequence = sequence
        self.sp_name = sp_name
        self.subsp_name = subsp_name
        self.at_content = self.get_ATcontent()
        self.transcribed_sequence = self.transcribe_Sequence()


    def transcribe_Sequence(self):
        sequence = self.sequence
        trans_seq = ""
        for base in sequence:
            if base == "A":
                trans_seq=trans_seq+"U"
            elif base == "T":
                trans_seq = trans_seq + "A"
            elif base == "G":
                trans_seq = trans_seq + "C"
            else:
                trans_seq = trans_seq + "G"

        self.transcribed_sequence = trans_seq
        return self.transcribed_sequence


    def get_ATcontent(self):
        sequence = self.sequence
        seq_len = len(sequence)
        a_content = 0
        t_content = 0
        for base in sequence:
            if base == "A":
                a_content += 1
            elif base == "T":
                t_content += 1
            else:
                continue
        # Calculate and round the at content into two decimal points
        at_content = round((a_content + t_content) / seq_len, 2)
        self.at_content = at_content
        return self.at_content

# ****************************************mRNA sub class***********************************************

class MRNAseq(Sequence):
    at_content = 0
    translated_sequence = ""
    __amino_acid_codons = {}

    def __init__(self, gene_id, gene_name, sp_name, subsp_name, sequence):
        super().__init__(gene_id, gene_name, sp_name, subsp_name, sequence)

        self.sequence = sequence
        self.translated_sequence = self.translate_Sequence()
        self.at_content = self.get_ATcontent()

    def get_ATcontent(self):
        sequence = self.sequence

        seq_len = len(sequence)
        sequence = sequence.replace("U", "T")
        a_content = 0
        t_content = 0

        for base in sequence:
            if base == "A":
                a_content += 1
            elif base == "T":
                t_content += 1
            else:
                continue
        # Calculate and round the at content into two decimal points
        at_content = round((a_content + t_content) / seq_len, 2)
        self.at_content = at_content

        return self.at_content


    @classmethod
    def upload_Codons(self):
        # initiate the "seq_dict" dictionary (values are stored as a list)
        seq_dict = {"Codons": [], "Amino_acids": []}

        # open the codon file
        with open("codon_table.txt", "r") as seq:
            for line in seq:
                if '#' not in line:
                    line = line.strip()
                    line = (line.split('\t'))
                    # take codons and amino acids into the seq_dict
                    seq_dict['Codons'].append(line[0])
                    seq_dict['Amino_acids'].append(line[2])

        self.__amino_acid_codons = seq_dict
        return self.__amino_acid_codons

    def translate_Sequence(self):
        sequence = self.sequence
        self.upload_Codons()

        cod_dict_values = list(self.__amino_acid_codons.values())
        codon = ""
        base_count = 0
        codon_list = []
        for base in sequence:

            codon = codon + base
            base_count += 1

            if base_count % 3 == 0:
                codon_list.append(codon)
                codon=""

        codons = cod_dict_values[0]
        for code in codon_list:
            if code in codons:
                # aa_index means index of the relevant aa in the list
                aa_index = codons.index(code)
                if cod_dict_values[1][aa_index]=="O":
                    break
                else:
                    self.translated_sequence=self.translated_sequence+cod_dict_values[1][aa_index]
        return self.translated_sequence

# ****************************************Protein sub class***********************************************

class Proteinseq(Sequence):

    def __init__(self, gene_id, gene_name, sp_name, subsp_name, uniprot_id, reviewed_status, sequence):

        super().__init__(gene_id, gene_name, sp_name, subsp_name, sequence)
        self.sequence=sequence
        self.uniprot_id = uniprot_id
        self.reviewed_status = reviewed_status
        self.hydrophobicity= self.get_Hydrophobicity()


    def get_Hydrophobicity(self):

        sequence = self.sequence
        hydro_count = 0
        # aa means amino acid
        for aa in sequence:
            if aa in "AILMFWYV":
                hydro_count += 1

        self.hydrophobicity = round((hydro_count/self.seq_len), 4)*100
        return self.hydrophobicity

# Objects are in the s14210_Q2_code.py file

# END