# -*- coding: utf-8 -*-

#########################
# IMPORTS               #
#########################
from numpy import matrix, array, array_equal
from genomat.config import GENE_NUMBER, INITIAL_PHENOTYPE, random_gene_value
import genomat.config as config
import random



#########################
# PRE-DECLARATIONS      #
#########################

class GeneNetwork():

    def __init__(self, *, nmatrix=None, configuration=None):
        """Each individual's genes network is defined by a square matrix.
        IN:
            A n*n numpy matrix which describes the genes network.
                If None or not provided, generate a random matrix
                based on configuration informations
            configuration is a configuration dictionnary.
            NB: matrix and configuration can't be provided at the same time.
        """
        assert((nmatrix is None) != (configuration is None))
        if nmatrix is None:
            self.genome = GeneNetwork.matrix_from(configuration)
        else:
            self.genome = nmatrix


    def is_viable(self, configuration, thresholded=config.thresholded):
        """An individual is viable if his phenotype is stable.
        Genome is viable if its stabilize itself on a phenotype.
        A genome is stable iff thresholded phenotype multiplied with genotype 
        give the same phenotype.
        This stabilization can happen after many steps.
        IN:
            configuration that contain initial_phenotype
            thresholded a function that take a phenotype 
                and returned a thresholded phenotype.
        OUT:
            True if stable, else False
        """
        def next_phenotype(): return thresholded(self.genome.dot(current_phenotype)) 
        walked_phenotypes = list() 
        current_phenotype = configuration[INITIAL_PHENOTYPE]
        while not any((array_equal(current_phenotype, p) for p in walked_phenotypes)):
            walked_phenotypes.append(current_phenotype)
            current_phenotype = next_phenotype()
        return all(next_phenotype() == current_phenotype)

    @staticmethod
    def mutated(gene_network, mutation_rate):
        """Introduce a mutation rate.
        IN:
            a gene network instance
            a mutation rate ([0;1])
        OUT:
            a new gene network eventually mutated 
                with the mutation rate
        """
        mutated_genome = []
        genome = gene_network.genome
        for gene in range(len(genome)):
            mutated_gene = []
            for value in array(genome[gene])[0]:
                mutated_gene.append(mutated_value(value) 
                                    if random.randint(1, 100) < rate * 100.
                                    else value) 
            mutated_genome.append(mutated_gene)
        return GeneNetwork(matrix(mutated_genome))


    @staticmethod
    def from_crossing(genes_networks):
        """Crosses received genes networks and returns a new one.
        IN:
            list of genes networks
        OUT:
            a new genes network
        """
        new_indiv = []
        for gene in range(len(genes_networks[0].genome)):
            # for each row choose a parent
            parent = array(random.choice(genes_networks).genome)
            new_indiv.append(parent[gene])
        return GeneNetwork(nmatrix=matrix(new_indiv))

    @staticmethod
    def matrix_from(configuration):
        """Return a new random numpy matrix instance 
        based on configuration values"""
        nb_gene = configuration[GENE_NUMBER]
        return matrix([
            [random_gene_value() for _ in range(nb_gene)] 
                for _ in range(nb_gene)
        ])


    def __str__(self):
        return str(self.genome)


