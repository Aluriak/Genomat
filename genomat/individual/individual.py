# -*- coding: utf-8 -*-



from geneNetwork import GeneNetwork



class Individual:
    """
    It's a proxy for GeneNetwork.
    It is able to to tell if it is viable or not, and to mutate.
    The class is able to cross individuals to generate a new one.
    """

    def __init__(self, genes_network):
        """An individual is defined by his genes network.
        IN:
            a genes network
        OUT:
            an individual
        """
        self.genome = genes_network

    @staticmethod
    def cross_individual(parents):
        """This function crosses two individuals.
        IN:
            list of individuals
        OUT:
            one new individual
        """
        new_genome = GeneNetwork.cross([parent.genome for parent in parents])
        new_indiv = Individual(new_genome)
        return new_indiv

        # are equivalent to:
        # return Individual(GeneNetwork.cross([parent.genome for parent in parents]))


    def is_viable(self, phenotype):
        """An individual is viable if his phenotype is stable.
        IN:
            phenotype
        OUT:
            True if stable, else False
        """
        return self.genome.is_viable(phenotype)


    def mutate(self, mutation_rate):
        """The mutation rate is defined by the percentage of mutation on each generation.
        IN:
            a genes network
        OUT:
            a mutated genes network
        """
        self.genome.mutate(mutation_rate)



