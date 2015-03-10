# -*- coding: utf-8 -*-
#########################
#       NETWORKS        #
#########################
"""
This package dump different networks of a populatio in a file.
Its something like a Singleton Observer 
of Population object.

Create the object
Call update(1) each time new stats are needed.
Call finalize(1) at the end.
"""


#########################
# IMPORTS               #
#########################
from genomat.config import GENE_NUMBER, NETWORKS_FILE



#########################
# PRE-DECLARATIONS      #
#########################
networks_file   = None



#########################
# MAIN FUNCTIONS        #
#########################
class StatsNetworks():
    def __init__(self, configuration):
        """Open files"""
        self.networks_file = open(configuration[NETWORKS_FILE], 'w')


    def update(self, population, generation_number):
        """create stats, save them"""
        genotypes = population.genotypes
        diversity = (len(genotypes)-1) / population.size
        self.networks_file.write('\n==========================\n')
        self.networks_file.write('\n'.join(str(_) for _ in genotypes))


    def finalize(self, population):
        """Close files"""
        self.networks_file.close()
        self.networks_file = None



