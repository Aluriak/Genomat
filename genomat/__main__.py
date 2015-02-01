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
from genomat import Genomat




#########################
# PRE-DECLARATIONS      #
#########################




#########################
# MAIN                  #
#########################
if __name__ is '__main__':
    phenotype = Genomat.default_phenotype
    # or define our own phenotype
    phenotype = Genomat.phenotype_from([1, -1, 1, 0, -1])

    pop = Genomat.new_population(size=20, phenotype=phenotype)
    for _ in range(100):
        pop.step(phenotype=phenotype)

    print(pop.prettyfied())

    # KO test:
    # randomly choosen gene is KO now
    from random import randint
    target = randint(1, Genomat.default_genome_size) - 1 # in [0;nb_gene-1]
    pop.gene_KO(target) 
    print(pop.viable_ratio(phenotype))



