# -*- coding: utf-8 -*-
#########################
#       CONFIG          #
#########################


#########################
# IMPORTS               #
#########################
import json
import random
from numpy import matrix


#########################
# PRE-DECLARATIONS      #
#########################
# version of project
VERSION = '0.1.0'
# files
CONFIG_FILE = 'config.json'
# define keys of config dictionnary
POP_SIZE            = 'pop_size'
INITIAL_PHENOTYPE   = 'initial_phenotype'
MUTATION_RATE       = 'mutation_rate'
PARENT_CROSS_COUNT  = 'parent_cross_count'
GENE_NUMBER         = 'gene_number'
GENERATION_COUNTS   = 'generations'
# use theses keys
default_configuration = {
    POP_SIZE:           20,
    INITIAL_PHENOTYPE:  matrix([[1] for _ in range(5)]),
    MUTATION_RATE:      0.01,
    PARENT_CROSS_COUNT: 2,
    GENE_NUMBER:        5,
    GENERATION_COUNTS:  [10,100,1000],
}


#########################
# CONFIG FUNCTIONS      #
#########################
def save(configuration=None, filename=CONFIG_FILE):
    """
    Save given configuration in CONFIG_FILE in json.
    """
    configuration = configuration if configuration is not None else default()
    with open(filename, 'w') as f:
        json.dump(configuration, f)

def load(filename=CONFIG_FILE):
    """
    Load configuration from given file. If not found or incomplete
    recording, default configuration is used for fill the blinks.
    """
    config = default()
    try:
        with open(filename, 'r') as f:
            c = json.load(f)
            config.update(c)
    except FileNotFoundError:
        pass
    return config

def default():
    """ Return default config """
    return default_configuration 


#########################
# OTHERS FUNCTIONS      #
#########################
def thresholded(phenotype):
    """
    Threshold given phenotype (that is a numpy matrix)
    """
    def sign(x): return (1 if x > 0 else (-1 if x < 0 else 0))
    return matrix([[sign(gene_expr)] for gene_expr in phenotype])

def random_gene_value():
    """
    Return a value randomly choosed that 
    can be used as a gene value
    """
    return random.randint(-9, 9)

def random_phenotype(size, generator=lambda:random.choice((-1, 0, 1))):
    """return a random phenotype, of given size and generator"""
    return matrix([[generator()] for _ in range(size)])

def default_phenotype(size):
    """Return phenotype of given size"""
    return matrix([[1] for _ in range(size)])

def create_phenotype(values):
    """Return phenotype with given values"""
    return matrix([[v] for v in values])



#########################
# MAIN                  #
#########################
if __name__ == '__main__':
    save(filename='test.json')
    assert(default() == load(filename='test.json'))
    print('ok !')
