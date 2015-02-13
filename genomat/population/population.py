# -*- coding: utf-8 -*-


#########################
# IMPORTS               #
#########################
import random
import csv
from numpy import matrix, array, array_equal
#from genomat.individual import GeneNetwork
from genomat.geneNetwork import GeneNetwork
from genomat.config import POP_SIZE, MUTATION_RATE, GENE_NUMBER
from genomat.config import PARENT_COUNT, INITIAL_PHENOTYPE, DO_STATS, STATS_FILE
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
        # while population not filled
        while len(self.indivs) < self.configuration[POP_SIZE]:
            new_indiv = GeneNetwork(configuration=configuration)
            if new_indiv.is_viable(self.configuration):
                self.indivs.append(new_indiv) 

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
        del configuration
        # init stats
        if self.configuration[DO_STATS]:
            f = open(self.configuration[STATS_FILE], 'a')
            writer = csv.DictWriter(f, fieldnames=[
                'pop_size',
                'gene_number',
                'generation_number',
            ] + ['viability_ratio_' + str(index) for index in range(self.configuration[GENE_NUMBER])])
        # do generations computing
        for generation_number in range(times):
            new_indivs = []
            # while population not filled
            while len(new_indivs) < self.configuration[POP_SIZE]:
                parents = random.sample(
                    self.indivs, 
                    self.configuration[PARENT_COUNT]
                )
                test_indiv = GeneNetwork.mutated(
                    GeneNetwork.from_crossing(parents), 
                    self.configuration
                )
                if test_indiv.is_viable(self.configuration):
                    new_indivs.append(test_indiv)
            # do stats if asked
            if self.configuration[DO_STATS]:
                gene_number = self.configuration[GENE_NUMBER]
                ratios = [self.test_genes([gene])[1] for gene in range(gene_number)]
                values = {
                    'pop_size':         len(new_indivs),
                    'gene_number':      gene_number,
                    'generation_number':generation_number,
                }
                values.update({('viability_ratio_'+str(index)):ratio for index, ratio in enumerate(ratios)})
                writer.writerow(values)
            # replace olds by youngs
            self.indivs = new_indivs
        # close stats file
        if self.configuration[DO_STATS]:
            f.close()

    def deactivate_genes(self, genes=None):
        """
        Deactive given genes in all population. 
        Genes must be defined by integers (its internally place in the matrix).
        Population is not garanted totally viable after that.
        IN:
            Iterable of integer (in [0;X-1] with X the number of genes)
        """
        if genes is None:
            genes = [random.randint(0, self.configuration[GENE_NUMBER]-1)]
        for indiv in self.indivs:
            indiv.deactivate_genes(genes)

    def reactivate_genes(self):
        """
        Reactive all genes in all population. 
        If genes are desactived, they regain there normal values.
        Population is not garanted totally viable after that.
        """
        for indiv in self.indivs:
            indiv.reactivate_genes()

    def test_genes(self, genes=None):
        """
        deactivate given genes (or randomly choosen ones), 
        return viability ratio of population and
        reactivate_genes.
        IN:
            Iterable of integer (in [0;X-1] with X the number of genes)
        OUT:
            Genes deactivated
            The ratio of viable individues in population on population size
        """
        if genes is None:
            genes = [random.randint(0, self.configuration[GENE_NUMBER]-1)]
        self.deactivate_genes(genes)
        ratio = self.viability_ratio()
        self.reactivate_genes()
        return genes, ratio

    def viability_ratio(self):
        """ Return the ratio of viable individues in population on population size """
        return len([i for i in self.indivs if i.is_viable(self.configuration)]) / len(self.indivs)

    
    def __str__(self):
        return("\tPOPULATION: initial phenotype\n" 
               + str(self.configuration[INITIAL_PHENOTYPE]) 
               + "\n\tPOPULATION: individuals\n"
               + '\n'.join((str(i) for i in self.indivs))
              )



