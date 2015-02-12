# -*- coding: utf-8 -*-
#########################
#       __MAIN__        #
#########################
"""
OO implementation of PRJ project.

Usage:
    __main__.py [--pop_size=<COUNT>] [--generations=<COUNT>[(,<COUNT>)]...] [--gene_number=<COUNT>] 

Options:
    -v --version    show version
    -h --help       show this docstring
    --pop_size=<COUNT>   size of population
    --generations=<COUNT>[(,<COUNT>)]... number of generations computed (multiple numbers lead to multiple populations)
    --gene_number=<COUNT> number of gene in a network 

"""

#THINGS THAT NEED TO BE IMPLEMENTED:
    #- gene network   : DONE
    #- population     : DONE
    #- crossing       : DONE
    #- viability test : DONE
    #- mutation       : DONE
    #- KO             : NO
    #- interface      : NO


#########################
# IMPORTS               #
#########################
from collections import ChainMap
from genomat.population import Population
import genomat.config as config 
from docopt import docopt




#########################
# PRE-DECLARATIONS      #
#########################




#########################
# MAIN                  #
#########################
if __name__ is '__main__':
    # load configuration from file
    config_file = config.load()
    # parse args and add them to args configuration
    config_args = {}
    arguments = docopt(__doc__, version=config.VERSION)
    filtered_arguments = {key[2:]:val 
                          for key, val in arguments.items() 
                          if val is not None and key[0:2] == '--'
                         }
    # update config_args with values, cast in int or [ints] if necessary
    for key, val in filtered_arguments.items():
        if key == 'generations':
            config_args[key] = [int(_) for _ in val.split(',')]
        else:
            config_args[key] = int(val)
    # merge configs as configuration
    configuration = ChainMap({}, config_args, config_file)


    # START USE INTERESTING THINGS
    phenotype = config.default_phenotype
    # or define our own phenotype
    phenotype = config.create_phenotype([1, -1, 1, 0, -1])
    # or use a randomly created phenotype
    phenotype = config.random_phenotype(size=5)

    # for each run of generation, create pop, step, KO, count
    for generation_count in configuration[config.GENERATION_COUNTS]:
        print('START FOR', generation_count, 'GENERATIONS.')
        pop = Population(configuration)
        print('POPULATION OF', configuration[config.POP_SIZE], 'INDIVIDUES CREATED.')
        pop.step(generation_count)
        print('DONE. NOW TEST KO OF A RANDOM GENE.')
        pop.gene_KO() 
        print('RATIO OF SURVIVABILITY:', pop.viable_ratio(), '\n---------------\n')



