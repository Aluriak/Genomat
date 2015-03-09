# -*- coding: utf-8 -*-
#########################
#       __MAIN__        #
#########################
"""
OO implementation of PRJ project.

Usage:
    __main__.py [options] 

Options:
    -v --version                            show version
    -h --help                               show this docstring                         
    --pop_size=<COUNT>                      size of populations                         
    --generations=<COUNT>[(,<COUNT>)]...    number of generations computed 
    --gene_number=<COUNT>                   number of gene in a network                 
    --initial_phenotype=<COUNT>[(,<COUNT>)]...  phenotype used as first phenotype 
    --mutation_rate=<RATE>                  rate of mutation (float in [0;1])           
    --parent_number=<COUNT>                 number of parents for give a new individual 
    --save_config                           save config as                              
    --config_file=<FILE>                    path to config file in json format [default: data/config.json]
    --do_stats                              save stats about each step in stats file    
    --stats_file=<FILE>                     save stats in FILE                           
    --erase_previous_stats                  delete previous stats data in stats file   [default: True]
    --wideness_gene=<COUNT>                 wideness of normal law used create 1st generation
    --wideness_mut=<COUNT>                  wideness of normal law used in case of mutation
    --save_networks                         dump all matrices in NETWORKS_FILE at each generation
    --networks_file=<FILE>                  file that receive dump of matrices
    --save_profiles                         do profiles at each generation on all individuals
    --profiles_file=<FILE>                  file that receive profiles data

"""


#########################
# IMPORTS               #
#########################
from collections        import ChainMap
from genomat.population import Population
from docopt             import docopt
from numpy              import matrix
import genomat.config as config 
import genomat.stats  as stats
import csv




#########################
# PRE-DECLARATIONS      #
#########################




#########################
# MAIN                  #
#########################
if __name__ is '__main__':
    # parse args and add them to args configuration
    config_args = {}
    arguments = docopt(__doc__, version=config.VERSION)
    filtered_arguments = {key[2:]:val # don't keep the '--' at the beginning
                          for key, val in arguments.items() 
                          if val is not None and key.startswith('--')
                         }
    # update config_args with values, cast in int or [int,…] if necessary
    for key, val in filtered_arguments.items():
        if 'file' in key:
            config_args[key] = val
        elif '.' in str(val):
            config_args[key] = float(val)
        elif key == config.GENERATION_COUNTS:
            config_args[key] = [int(_) for _ in val.split(',')]
        elif key == config.INITIAL_PHENOTYPE:
            config_args[key] = matrix(val.replace(',', ';'))
        else:
            config_args[key] = int(val)
    # load configuration from file
    config_file = config.load(filename=config_args[config.CONFIG_FILE])
    # merge configs as configuration
    configuration = ChainMap({}, config_args, config_file)

    # save it if asked
    if configuration['save_config']:
        config.save(dict(configuration), filename=configuration[config.CONFIG_FILE])
    # do stats
    stats.initialize(configuration)

    # print used configuration
    print('USED CONFIGURATION IS:\n', config.prettify(configuration, '\t'), "\n---------------\n", sep='')



    # START USE INTERESTING THINGS
    phenotype = config.default_phenotype
    # or define our own phenotype
    phenotype = config.create_phenotype([1, -1, 1, 0, -1])
    # or use a randomly created phenotype
    phenotype = config.random_phenotype(size=configuration[config.GENE_NUMBER])
    configuration[config.INITIAL_PHENOTYPE] = phenotype
    pop = None

    # for each run of generation, create pop, step, KO, count
    for generation_count in configuration[config.GENERATION_COUNTS]:
        print('START FOR', generation_count, 'GENERATIONS.')
        pop = Population(configuration)
        print('POPULATION OF', configuration[config.POP_SIZE], 'INDIVIDUES CREATED.')
        pop.step(generation_count)
        print('DONE. NOW TEST KO OF A RANDOM GENE.')
        deactivated_genes, viability_ratio = pop.test_genes()
        print('DEACTIVATED GENE      :', deactivated_genes)
        print('RATIO OF SURVIVABILITY:', viability_ratio, '\n---------------\n')
    

    # finalize all
    stats.finalize(pop)



