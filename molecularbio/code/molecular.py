def make_encoder(mapping):
    return lambda x: Nucleotide(x)


class Ribosome:

    def accept(self):
        pass


class RNA:

    def __init__(self):
        self.seq = []
        self.current = 0


    def advance(self):
        self.current += 1

    
    def advance_codon(self):
        self.current += 3;


    def get_codon(self):
        return self.seq[current]


class Nucleotide:
    def __init__(self):
        pass


    def symbol(self):
        return ''


    def next(self):
        pass


class AminoAcid:
    def __init__(self):
        pass



