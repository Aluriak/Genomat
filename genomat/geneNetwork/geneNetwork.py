# -*- coding: utf-8 -*-
"""
Module that describes GeneNetwork class.
"""

#########################
# IMPORTS               #
#########################
from numpy import matrix, array, array_equal
from genomat.config import GENE_NUMBER, INITIAL_PHENOTYPE, MUTATION_RATE
from genomat.config import RANDOM_GENE_VAL_FUNC, THRESOLDED_FUNC, MUTATED_FUNC
import genomat.config as config
import random



#########################
# PRE-DECLARATIONS      #
#########################

class GeneNetwork():
    """
    A GeneNetwork is something like a 2 dimensions matrix 
    that describes regulation of genes.
    So:
        2 3
        1 0
    Can be translated as :
        gene 0 promotes itself by factor 2
        gene 0 promotes gene 1 by factor 3
        gene 1 promotes gene 0 by factor 1
        gene 1 promotes itself by factor 0

    Used values heavily depends of given configuration,
    and methods provided.
    """

    def __init__(self, nmatrix):
        """Each individual's genes network is defined by a square matrix.
        IN:
            A n*n numpy matrix which describes the genes network.
                If None or not provided, generate a random matrix
                based on configuration informations
        """
        assert(nmatrix is not None)
        self.genome = nmatrix
        self.genome_preserved = self.genome # only used if gene deactivation


    def is_viable(self, configuration):
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
        def next_phenotype(): 
            return configuration[THRESOLDED_FUNC](
                self.genome.dot(current_phenotype)
            ) 
        walked_phenotypes = list() 
        current_phenotype = configuration[INITIAL_PHENOTYPE]
        while not any((array_equal(current_phenotype, p) for p in walked_phenotypes)):
            walked_phenotypes.append(current_phenotype)
            current_phenotype = next_phenotype()
        return all(next_phenotype() == current_phenotype)

    def deactivate_genes(self, deactivated_genes):
        """
        Deactive given deactivated_genes. If others genes was already deactived, 
        they will be reactivated
        Genes must be defined by integers (its internally place in the matrix).
        Population is not garanted totally viable after that.
        IN:
            Iterable of integer (in [0;X-1] with X the number of genes)


        Tests:
            >>> from numpy import matrix, array
            >>> from genomat.geneNetwork import GeneNetwork
            >>> gn = GeneNetwork(nmatrix=matrix('1,2,3;4,5,6;7,8,9'))
            >>> gn.deactivate_genes([1])
            >>> str(gn)
            '[[1 0 3]\n [0 0 0]\n [7 0 9]]'

        """
        assert(all((0 <= gene for gene in deactivated_genes)))
        # reactivate all if necessary
        if self.genome_preserved is not self.genome:
            self.reactivate_genes()
        # deactivate targeted
        ko_genome = array(self.genome)
        for gene in range(len(ko_genome)):
            if gene in deactivated_genes:
                ko_genome[gene] = [0] * len(ko_genome)
            else:
                for deactivated_gene in deactivated_genes:
                    ko_genome[gene][deactivated_gene] = 0
        self.genome = ko_genome

    def reactivate_genes(self):
        """
        Reactive all genes. 
        If genes are desactived, they regain there normal values.
        Population is not garanted totally viable after that.
        """
        self.genome = self.genome_preserved


    @staticmethod
    def mutated(gene_network, configuration):
        """given GeneNetwork instance can mutate,
        according to configuration
        IN:
            a gene network instance
            a mutation rate ([0;1])
        OUT:
            a new gene network eventually mutated 
                with the mutation rate
        """
        # init
        mutated_genome = []
        genome = gene_network.genome
        rate = configuration[MUTATION_RATE]
        # for each value of gene network
        for gene in range(len(genome)):
            mutated_gene = []
            for value in array(genome[gene])[0]:
                # something can change
                mutated_gene.append(configuration[MUTATED_FUNC](value) 
                                    if random.random() < rate 
                                    else value) 
            mutated_genome.append(mutated_gene)
        return GeneNetwork(nmatrix=matrix(mutated_genome))


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
    def viable_from_configuration(configuration):
        """Return a new GeneNetwork instance, create from data
        in given configuration. 
        Returned instance is viable in given configuration.
        """
        gn = GeneNetwork(GeneNetwork.matrix_from(configuration))
        while not gn.is_viable(configuration):
            gn = GeneNetwork(GeneNetwork.matrix_from(configuration))
        return gn

    @staticmethod
    def matrix_from(configuration):
        """Return a new random numpy matrix instance 
        based on configuration values"""
        nb_gene = configuration[GENE_NUMBER]
        return matrix([
            [configuration[RANDOM_GENE_VAL_FUNC]() for _ in range(nb_gene)] 
                for _ in range(nb_gene)
        ])


    def __str__(self):
        return str(self.genome)


