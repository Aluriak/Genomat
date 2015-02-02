# -*- coding: utf-8 -*-


class GeneNetwork():

    def __init__(self, matrix):
        """Each individual's genes network is defined by a 5/5 matrix.
        IN:
            A n*n matrix which describes the genes network.
        OUT:
        """
        self.matrix = matrix

    def is_viable(self, phenotype):
        """An individual is viable if his phenotype is stable.
        IN:
            phenotype
        OUT:
            True if stable, else False
        """
        return NotImplemented

    @staticmethod
    def cross(self, genes_networks):
        """Crosses received genes networks and returns a new one.
        IN:
            list of genes networks
        OUT:
            a new genes network
        """
        return NotImplemented

    def mutate(self, mutation_rate):
        """Introduce a mutation rate.
        IN:
            a genes network, and a mutation rate
        OUT:
            a new genes network mutated with the mutation rate
        """
        return NotImplemented




