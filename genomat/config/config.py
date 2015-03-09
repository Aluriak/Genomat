# -*- coding: utf-8 -*-
#########################
#       CONFIG          #
#########################


#########################
# IMPORTS               #
#########################
import json
import random
from numpy     import matrix
from functools import partial


#########################
# PRE-DECLARATIONS      #
#########################
# version of project
VERSION = '0.1.0'
# define keys of config dictionnary
CONFIG_FILE         = 'config_file'
STATS_FILE          = 'stats_file'
DO_STATS            = 'do_stats'
POP_SIZE            = 'pop_size'
INITIAL_PHENOTYPE   = 'initial_phenotype'
__INITIAL_PHENOTYPE = 'initial_phenotype_as_list'
MUTATION_RATE       = 'mutation_rate'
PARENT_COUNT        = 'parent_number'
GENE_NUMBER         = 'gene_number'
GENERATION_COUNTS   = 'generations'
THRESOLDED_FUNC     = 'thresholded_func'
RANDOM_GENE_VAL_FUNC= 'random_gene_val_func'
MUTATED_FUNC        = 'mutated_func'
WIDENESS_GENE       = 'wideness_gene'
WIDENESS_MUT        = 'wideness_mut'
SAVE_NETWORKS       = 'save_networks'
NETWORKS_FILE       = 'networks_file'
SAVE_PROFILES       = 'save_profiles'
PROFILES_FILE       = 'profiles_file'
# use theses keys
default_configuration = {
    POP_SIZE:               20,
    INITIAL_PHENOTYPE:      [1 for _ in range(5)],
    MUTATION_RATE:          0.01,
    PARENT_COUNT:           2,
    GENE_NUMBER:            5,
    GENERATION_COUNTS:      [10,100],
    CONFIG_FILE:            'data/config.json',
    STATS_FILE:             'data/stats.csv',
    WIDENESS_GENE:          100,
    WIDENESS_MUT:           10,
    SAVE_NETWORKS:          False,
    NETWORKS_FILE:          'data/networks.txt',
    SAVE_PROFILES:          False,
    PROFILES_FILE:          'data/profiles.csv',
}


#########################
# CONFIG FUNCTIONS      #
#########################
def save(configuration=None, filename=default_configuration[CONFIG_FILE]):
    """
    Save given configuration in CONFIG_FILE in json.
    """
    configuration = usable2json(
        configuration if configuration is not None else default()
    )
    try:
        with open(filename, 'w') as f:
            json.dump(configuration, f, indent=4, separators=(',', ':'))
    except FileNotFoundError:
        print("configuration can't be saved because file " + filename + " can't be found.")

def load(filename=default_configuration[CONFIG_FILE]):
    """
    Load configuration from given file. If not found or incomplete
    recording, default configuration is used for fill in the blanks.
    """
    config = default()
    try:
        with open(filename, 'r') as f:
            config.update(json.load(f)) 
            config = json2usable(config)
    except FileNotFoundError:
        pass
    except ValueError:
        pass
    return config

def default():
    """ Return default config """
    return json2usable(default_configuration)

def json2usable(configuration):
    """return a new configuration create from given one, 
    from JSON serializable to usable format"""
    configuration = dict(configuration)
    # use numpy matrices for phenotype
    configuration[__INITIAL_PHENOTYPE] = configuration[INITIAL_PHENOTYPE]
    configuration[INITIAL_PHENOTYPE]   = matrix([
        [_] for _ in configuration[INITIAL_PHENOTYPE]
    ])
    # add functions
    configuration[THRESOLDED_FUNC]      = thresholded
    configuration[RANDOM_GENE_VAL_FUNC] = partial(random_gene_value, configuration[WIDENESS_GENE])
    configuration[MUTATED_FUNC]         = partial(mutated_value, amplitude_mut=configuration[WIDENESS_MUT])
    # conversion done !
    return configuration

def usable2json(configuration):
    """return a new configuration create from given one,
    from usable format to JSON serializable format"""
    configuration = dict(configuration)
    # get lists in place of phenotype
    configuration[INITIAL_PHENOTYPE] = configuration[__INITIAL_PHENOTYPE]
    del configuration[__INITIAL_PHENOTYPE]
    # del functions
    del configuration[THRESOLDED_FUNC]
    del configuration[RANDOM_GENE_VAL_FUNC]
    del configuration[MUTATED_FUNC]
    # conversion done !
    return configuration



#########################
# OTHERS FUNCTIONS      #
#########################
def thresholded(phenotype):
    """
    Threshold given phenotype (that is a numpy matrix)
    """
    def sign(x): return (1 if x > 0 else (-1 if x < 0 else 0))
    return matrix([[sign(gene_expr)] for gene_expr in phenotype])

def random_gene_value(amplitude_gene):
    """
    Return a randomly value choosen that 
    can be used as a gene value
    """
    return int(random.gauss(0, 1) * amplitude_gene)

def mutated_value(value, amplitude_mut):
    """return a randomly choosen mutated equivalent of given value"""
    return value + int((random.gauss(0, 1) * amplitude_mut))

def random_phenotype(size, generator=lambda:random.choice((-1, 0, 1))):
    """return a random phenotype, of given size and generator"""
    return matrix([[generator()] for _ in range(size)])

def default_phenotype(size):
    """Return phenotype of given size"""
    return matrix([[1] for _ in range(size)])

def create_phenotype(values):
    """Return phenotype with given values"""
    return matrix([[v] for v in values])

def prettify(configuration, prefix=''):
    """Return str vision of configuration, ready to be print"""
    to_print = {
        prefix+'gene number      :\t': configuration[GENE_NUMBER],
        prefix+'init phenotype   :\n': configuration[INITIAL_PHENOTYPE],
        prefix+'mutation rate    :\t': configuration[MUTATION_RATE],
        prefix+'parent count     :\t': configuration[PARENT_COUNT],
        prefix+'gene wideness    :\t': configuration[WIDENESS_GENE],
        prefix+'mutation wideness:\t': configuration[WIDENESS_MUT],
        prefix+'perform stats    :\t': ('yes ['+configuration[STATS_FILE]+']') if configuration[DO_STATS] else 'no',
        prefix+'perform profiles :\t': ('yes ['+configuration[PROFILES_FILE]+']') if configuration[SAVE_PROFILES] else 'no',
    }
    return (
        '\n'.join((k + str(v) for k, v in to_print.items()))
    )


#########################
# MAIN                  #
#########################
if __name__ == '__main__':
    save(filename='test.json')
    assert(usable2json(default()) == usable2json(load(filename='test.json')))
    print('ok !')
