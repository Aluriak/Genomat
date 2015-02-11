# -*- coding: utf-8 -*-
#########################
#       __MAIN__        #
#########################
"""
OO implementation of PRJ project.

Things that need to be presents:
    - individual     : NO
    - gene network   : NO
    - population     : NO
    - crossing       : NO
    - viability test : NO
    - mutation       : NO
    - KO             : NO
    - interface      : NO
"""


#########################
# IMPORTS               #
#########################
from genomat.population import Population




#########################
# PRE-DECLARATIONS      #
#########################




#########################
# MAIN                  #
#########################
if __name__ is '__main__':
    phenotype = Population.default_phenotype
    # or define our own phenotype
    phenotype = Population.create_phenotype([1, -1, 1, 0, -1])
    # or use a randomly created phenotype
    phenotype = Population.random_phenotype(5)

    pop = Population(size=20, phenotype=phenotype)
    for _ in range(100):
        pop.step(phenotype=phenotype)

    print(pop.prettyfied())

    # KO test:
    # randomly choosen gene is KO now
    from random import randint
    target = randint(1, Population.default_genome_size) - 1 # in [0;nb_gene-1]
    pop.gene_KO(target) 
    print(pop.viable_ratio(phenotype))



