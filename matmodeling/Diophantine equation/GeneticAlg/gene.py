class Gene():

    def __init__(self):
        self.alleles = {}
        self.alleles[0] = 0
        self.alleles[1] = 0
        self.alleles[2] = 0
        self.alleles[3] = 0
        self.fitness = 0
        self.probability = 0.0

    def __eq__(self, other):
        for i in range(len(self.alleles.keys())):
            if(self.alleles[i] != other.alleles[i]):
                return False
        return True