# -*- coding: utf-8 -*-
#########################
#       STATS           #
#########################
"""
This package do means and variances computation of genotypes.
Its something like a Singleton Observer 
of Population object.

Create the object
Call update(1) each time new stats are needed.
Call finalize(1) at the end.
"""


#########################
# IMPORTS               #
#########################
import csv
from itertools   import product
from genomat.config import GENE_NUMBER, SAVE_PROFILES, PROFILES_FILE



#########################
# PRE-DECLARATIONS      #
#########################



#########################
# MAIN FUNCTIONS        #
#########################
class StatsProfiles():
    """
    Perform a profiles of all geneNetworks.
    """

    def __init__(self, configuration):
        # open file, initialize the writer, write header
        self.profiles_file = open(configuration[PROFILES_FILE], 'w')
        self.profiles_writer = csv.DictWriter(
            self.profiles_file, 
            fieldnames=profiles_file_keys(configuration[GENE_NUMBER])
        )
        self.profiles_writer.writeheader()


    def update(self, population, generation_number):
        """create stats, save them"""
        self.profiles_writer.writerow(
            profiles_file_values(population.profiles, generation_number)
        )


    def finalize(self, population):
        """Close files"""
        self.profiles_file.close()
        self.profiles_file = None



#########################
# FILE MANIPULATION     #
#########################
def profiles_file_keys(gene_number):
    """Return fiels in profiles file, ordered, as a list of string"""
    return ['generation'] + [
        'mean'+str(gene)+'x'+str(col) 
        for gene, col in product(range(gene_number), repeat=2)
    ] + [
        'varc'+str(gene)+'x'+str(col) 
        for gene, col in product(range(gene_number), repeat=2)
    ]


def profiles_file_values(profiles, generation_number):
    """Return a dict usable with csv.DictWriter for profiles file"""
    means, varc = profiles
    means = {'mean'+str(k[0])+'x'+str(k[1]): v for k,v in means.items()}
    varc  = {'varc'+str(k[0])+'x'+str(k[1]): v for k,v in varc.items()}
    # return all
    means.update(varc)
    means['generation'] = generation_number
    return means



