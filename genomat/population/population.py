# -*- coding: utf-8 -*-


#########################
# IMPORTS               #
#########################
import random
from numpy import matrix, array, array_equal
#from genomat.individual import GeneNetwork
from genomat.geneNetwork import GeneNetwork
from genomat.config import POP_SIZE, MUTATION_RATE, PARENT_CROSS_COUNT, INITIAL_PHENOTYPE
import genomat.config as config



#########################
# PRE-DECLARATIONS      #
#########################



class Population:

    def __init__(self, configuration):
        """The population is defined by the number of individual it is composed of.
        IN:
            a configuration that link data name to data value
        OUT:
            A population
        """
        self.configuration = configuration
        self.generate_pop(configuration)

    def generate_pop(self, configuration):
        """Generate a new population
        IN:
            GeneNetworks
        OUT:
            A population
        """
        self.indivs = []
        for _ in range(configuration[POP_SIZE]):
            self.indivs.append(GeneNetwork(configuration=configuration)) 

    def size(self):
        """Returns the population's size.
        IN:
            The population
        OUT:
            The population's size
        """
        return len(self.indivs)

    def step(self, times=1, configuration=None):
        """Pass to the next generation.
        IN:
            times is the number of generation that will be computed.
                default is one generation.
            new configuration to apply. No changements if None or 
                not provided.
        OUT:
            A new generation. The previous generation is overwritten.
        """
        # update configuration if necessary 
        if configuration is not None: self.configuration = configuration
        for _ in range(times):
            new_indivs = []
            # while population not filled
            while len(new_indivs) < self.configuration[POP_SIZE]:
                parents = random.sample(
                    self.indivs, 
                    self.configuration[PARENT_CROSS_COUNT]
                )
                test_indiv = GeneNetwork.from_crossing(parents)
                if test_indiv.is_viable(self.configuration):
                    new_indivs.append(test_indiv)
            # replace olds by youngs
            self.indivs = new_indivs

    def gene_KO(self, genes=None):
        """
        Put given genes KO. 
        Genes must be defined by integers (its internally place in the matrix).
        Population is not garanted totally viable after that.
        IN:
            Iterable of integer (in [1;X] with X the number of genes)
        """
        return NotImplemented

    def viable_ratio(self):
        """ Return the ratio of viable individues in population on population size """
        return len([i for i in self.indivs if i.is_viable(self.configuration)]) / len(self.indivs)

    
    def __str__(self):
        return("\tPOPULATION: initial phenotype\n" 
               + str(self.configuration[INITIAL_PHENOTYPE]) 
               + "\n\tPOPULATION: individuals\n"
               + '\n'.join((str(i) for i in self.indivs))
              )



