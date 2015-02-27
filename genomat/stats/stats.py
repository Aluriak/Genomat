# -*- coding: utf-8 -*-
#########################
#       STATS           #
#########################
"""
This package do statistics.
Its something like a Singleton Observer 
of Population object.

Call initialize(1) at the beginning.
Call finalize() at the end.
Call update(1) each time new stats are needed.
"""


#########################
# IMPORTS               #
#########################
import csv
import math
from functools import partial
from genomat.config import STATS_FILE, GENE_NUMBER



#########################
# PRE-DECLARATIONS      #
#########################
stats_file = None
writer     = None



#########################
# MAIN FUNCTIONS        #
#########################
def initialize(configuration):
    """Open files"""
    global stats_file, writer
    stats_file = None
    openf = partial(open, configuration[STATS_FILE])
    stats_file = openf('w' if configuration['erase_previous_stats'] else 'a')
    writer = csv.DictWriter(
        stats_file, 
        fieldnames=stats_file_keys(configuration[GENE_NUMBER])
    )
    # print header if no previous stats
    if configuration['erase_previous_stats']:
        writer.writeheader()



def update(population, generation_number):
    """create stats, save them"""
    global stats_file, writer
    configuration = population.configuration
    if stats_file is None: return # case where no initialize was called
    # init
    gene_number = configuration[GENE_NUMBER]
    ratios = [population.test_genes([gene])[1] for gene in range(gene_number)]
    # get values and write them in file
    writer.writerow(stats_file_values(
        population.size,
        gene_number,
        generation_number,
        *[ratios]
    ))



def finalize():
    """Close files"""
    global stats_file
    if stats_file is None: return # case where no initialize was called
    stats_file.close()
    stats_file = None



#########################
# FILE MANIPULATION     #
#########################
# content stats file 
def stats_file_keys(gene_number):
    """Return fiels in stats file, ordered, as a list of string"""
    return [
            'popsize',
            'genenumber',
            'generationnumber',
        ] + ['viabilityratio'   + str(i) for i in range(gene_number)
        ] + ['viabilityratioDB' + str(i) for i in range(gene_number)
        ]
def stats_file_values(pop_size, gene_number, generation_number, viability_ratios):
    """Return a dict usable with csv.DictWriter for stats file"""
    values = {
        'popsize':         pop_size,
        'genenumber':      gene_number,
        'generationnumber':generation_number
    }
    values.update({('viabilityratio'+str(index)):ratio 
                   for index, ratio in enumerate(viability_ratios)
                  })
    values.update({('viabilityratioDB'
                    +str(index)):ratio2dB(ratio, pop_size)
                   for index, ratio in enumerate(viability_ratios)
                  })
    return values


def ratio2dB(ratio, pop_size):
    """Convert given ratio in dB value, based on population size"""
    return math.log(ratio+1/pop_size, 10)

