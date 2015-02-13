# -*- coding: utf-8 -*-
#########################
#       __MAIN__        #
#########################
"""
Pure functionnal incomplete implementation of PRJ project.
Gene KO and mutations are not implemented.
Computation of viability for a genome is not really implemented, but works…

Its just for playing and teaching.
Real project is implemented as genomat module.
"""



#########################
# IMPORTS               #
#########################
from functools import partial
from itertools import product
from numpy import matrix, array
import random



#########################
# PRE-DECLARATIONS      #
#########################
NB_PARENTS           = 2
DEFAULT_GENE_NUMBER  = 5
DEFAULT_GENE_VALUE   = partial(random.randint, 0, 9)
DEFAULT_PHENOTYPE    = matrix([[1] for _ in range(DEFAULT_GENE_NUMBER)])
def DEFAULT_THRESHOLDING(phenotype):
    """
    Threshold function for a phenotype
    for each gene, >0 becomes 1 and <0 becomes -1
    """
    # verification, sign declaration, return thresholded phenotype
    assert(phenotype.shape == (DEFAULT_GENE_NUMBER, 1))
    def sign(x): return (1 if x > 0 else (-1 if x < 0 else 0))
    return matrix([[sign(gene_expr)] for gene_expr in phenotype])



#########################
# INIT FUNCTIONS        #
#########################
def init_genome(size=DEFAULT_GENE_NUMBER, random_value=DEFAULT_GENE_VALUE):
    """
    Return genome, define as dict that links a gene id A and another gene id B to interaction of
    gene A on gene B.

    So:
        2 3
        1 0
    Can be translated as :
        gene 0 promotes itself by factor 2
        gene 0 promotes gene 1 by factor 3
        gene 1 promotes gene 0 by factor 1
        gene 1 promotes itself by factor 0
    And can be readed in returned dict as :
        assert(genome[0, 0] == 2)
        assert(genome[0, 1] == 3)
        assert(genome[1, 0] == 1)
        assert(genome[1, 1] == 0)
    """
    return matrix([[random_value() for _ in range(size)] for _ in range(size)])


def init_population(size, is_viable, new_indiv=init_genome):
    pop = []
    while len(pop) < size:
        indiv = new_indiv()
        pop.append(indiv) if is_viable(indiv) else None
    return pop





#########################
# PRINT FUNCTIONS       #
#########################
def prettyfied_genome(genome, size=DEFAULT_GENE_NUMBER):
    """Return well vizualisation of genome as string"""
    return str(genome)

def prettyfied_population(pop, genome_size=DEFAULT_GENE_NUMBER):
    return ('\nPOPULATION:\n'
            + '\n'.join([prettyfied_genome(ind, genome_size) for ind in pop]))




#########################
# STEPS FUNCTIONS       #
#########################
def genome_from(parents, size=DEFAULT_GENE_NUMBER):
    """
    Return a new genome, create by cross received genomes.
    Each line of new genome is randomly choosed from
    one parent.
    """
    new_indiv = []
    for gene in range(size):
        # for each row choose a parent
        parent = array(random.choice(parents))
        new_indiv.append(parent[gene])
    return matrix(new_indiv)


def next_population(pop, is_viable, size=None):
    """Return new population, derived from given one"""
    size = len(pop) if size is None else size
    new_pop = []
    while len(new_pop) < size:
        new_indiv = genome_from(random.sample(pop, NB_PARENTS))
        new_pop.append(new_indiv) if is_viable(new_indiv) else None
    return new_pop


def genome_is_viable(genome, initial_phenotype, thresholding=DEFAULT_THRESHOLDING, size=DEFAULT_GENE_NUMBER):
    """
    Genome is viable if its stabilize itself.
    Stabilization of a genome is verified if thresholding of multiplication of initial_phenotype and genome is
    equal to initial phenotype.
    Not really implemented.
    """
    return random.randint(0, 1) == 0



#########################
# MAIN FUNCTION         #
#########################
if __name__ is '__main__':
    genome_is_viable = partial(genome_is_viable,
                               initial_phenotype=DEFAULT_PHENOTYPE,
                               thresholding=DEFAULT_THRESHOLDING
                              )
    p = init_population(10, genome_is_viable)
    for _ in range(10):
        p = next_population(p, genome_is_viable)
        print(prettyfied_population(p))



