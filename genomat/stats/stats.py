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
from functools   import partial
from collections import defaultdict
from genomat.config import STATS_FILE, GENE_NUMBER
import numpy as np



#########################
# PRE-DECLARATIONS      #
#########################
stats_file = None
writer     = None
ratio_data = defaultdict(list)



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
    global stats_file, writer, ratio_data
    configuration = population.configuration
    if stats_file is None: return # case where no initialize was called
    # init
    gene_number = configuration[GENE_NUMBER]
    ratios    = [population.test_genes([gene])[1] for gene in range(gene_number)]
    ratios_db = [ratio2dB(r, population.size) for r in ratios]
    [ratio_data[gene].append(r) for gene, r in enumerate(ratios_db)]
    diversity = population.genotype_count / population.size
    #printed = set()
    #for indiv in population.indivs:
        #if indiv not in printed:
            #print(indiv)
            #printed.add(indiv)
    #print('DIVERSITY:', diversity)
    # get values and write them in file
    writer.writerow(stats_file_values(
        population.size,
        gene_number,
        generation_number,
        diversity,
        ratios, 
        ratios_db
    ))



def finalize():
    """Close files"""
    global stats_file, ratio_data
    if stats_file is None: return # case where no initialize was called
    stats_file.close()
    stats_file = None
    #save_fft(ratio_data)



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
            'diversity',
        ] + ['viabilityratio'   + str(i) for i in range(gene_number)
        ] + ['viabilityratioDB' + str(i) for i in range(gene_number)
        ]


def stats_file_values(pop_size, gene_number, generation_number, diversity, viability_ratios, viability_ratios_db):
    """Return a dict usable with csv.DictWriter for stats file"""
    values = {
        'popsize':         pop_size,
        'genenumber':      gene_number,
        'generationnumber':generation_number,
        'diversity'       :diversity,
    }
    values.update({('viabilityratio'  +str(index)):ratio 
                   for index, ratio in enumerate(viability_ratios)
                  })
    values.update({('viabilityratioDB'+str(index)):ratio 
                   for index, ratio in enumerate(viability_ratios_db)
                  })
    return values




#########################
# CONVERTION            #
#########################
def ratio2dB(ratio, pop_size):
    """Convert given ratio in dB value, based on population size"""
    return math.log(ratio+1/pop_size, 10)




#########################
# STATISTICS            #
#########################
def save_fft(gene_ratios):
    """see http://stackoverflow.com/questions/3694918/how-to-extract-frequency-associated-with-fft-values-in-python """
    # save them in a graph
    from scipy import fftpack
    import numpy as np
    import pylab as py

    for gene, ratios in gene_ratios.items():
        w     = np.fft.fft(ratios)
        freqs = np.fft.fftfreq(len(ratios))


        # Take the fourier transform of the image.
        F1 = fftpack.fft2(myimg)

        # Now shift so that low spatial frequencies are in the center.
        F2 = fftpack.fftshift( F1 )

        # the 2D power spectrum is:
        psd2D = np.abs( F2 )**2

        # plot the power spectrum
        py.figure(1)
        py.clf()
        py.imshow( psf2D )
        py.show()

        #print(freqs)
        #for coef, freq in zip(w,freqs):
            #if coef:
                #print('{c:>6} * exp(2 pi i t * {f})'.format(c=coef,f=freq))




