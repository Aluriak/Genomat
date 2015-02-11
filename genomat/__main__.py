# -*- coding: utf-8 -*-
#########################
#       __MAIN__        #
#########################
"""
OO implementation of PRJ project.

Things that need to be implemented:
    - individual     : YES
    - gene network   : YES
    - population     : YES
    - crossing       : YES
    - viability test : YES
    - mutation       : YES
    - KO             : NO
    - interface      : NO
"""


#########################
# IMPORTS               #
#########################
from genomat.population import Population
import genomat.config as config 




#########################
# PRE-DECLARATIONS      #
#########################




#########################
# MAIN                  #
#########################
if __name__ is '__main__':
    phenotype = config.default_phenotype
    # or define our own phenotype
    phenotype = config.create_phenotype([1, -1, 1, 0, -1])
    # or use a randomly created phenotype
    phenotype = config.random_phenotype(size=5)

    # get config and create pop
    configuration = config.load()
    for generation_count in (10, 100, 1000):
        pop = Population(configuration)
        pop.step(generation_count)

        #print(pop)

        # KO test:
        pop.gene_KO() # randomly choosen gene is KO now
        print(pop.viable_ratio())



