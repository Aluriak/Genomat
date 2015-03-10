# -*- coding: utf-8 -*-


#########################
# IMPORTS               #
#########################
import concurrent.futures
import random

from numpy               import matrix, array, array_equal
from statistics          import mean, variance
from collections         import defaultdict


import genomat.config as config
import genomat.stats  as stats

from genomat.geneNetwork import GeneNetwork
from genomat.config      import POP_SIZE, MUTATION_RATE, GENE_NUMBER, SEED_VALUE
from genomat.config      import PARENT_COUNT, INITIAL_PHENOTYPE, DO_STATS, STATS_FILE
from genomat.progressbar import create_progress_bar, update_progress_bar, finish_progress_bar


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
        create_progress_bar()
        # while population not filled
        for _ in range(self.configuration[POP_SIZE]):
            self.indivs.append(
                GeneNetwork.viable_from_configuration(configuration)
            )
            update_progress_bar(self.size, self.configuration[POP_SIZE]+1)
        finish_progress_bar()

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

        # do generations computing
        create_progress_bar()
        try:
            for generation_number in range(times):
                new_indivs = []
                # while population not filled
                pop_size = self.configuration[POP_SIZE]
                if self.configuration[SEED_VALUE] is None:
                    # random seed value, so using thread is possible 
                    #   (reproductibility not necessary)
                    with concurrent.futures.ProcessPoolExecutor() as executor:
                        for new_indiv in executor.map(self.new_viable_indiv, [None]*pop_size):
                            new_indivs.append(new_indiv)
                else:
                    # random seed given, so, for provides reproductibility, 
                    #   no thread must be used
                    while len(new_indivs) < pop_size:
                        new_indivs.append(self.new_viable_indiv())
                assert(self.size == pop_size)
                # replace olds by youngs
                self.indivs = new_indivs
                # do stats on youngs
                stats.update(self, generation_number)
                # show to user that its computer is doing something
                update_progress_bar(generation_number, times)
        except (KeyboardInterrupt, concurrent.futures.process.BrokenProcessPool):
            pass

        # finish it !
        finish_progress_bar()


    def new_viable_indiv(self, none=None):
        """
        Return a new indiv, create from population crossing, 
        eventually mutated. Indiv is viable.
        Nothing keyword is an unused arg used for give map compatibility.
        """
        new_indiv = None
        while new_indiv is None or not new_indiv.is_viable(self.configuration):
            parents = random.sample(
                self.indivs, 
                self.configuration[PARENT_COUNT]
            )
            new_indiv = GeneNetwork.mutated(
                GeneNetwork.from_crossing(parents), 
                self.configuration
            )
        return new_indiv


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

    @property
    def size(self):
        return len(self.indivs)

    @property
    def genotypes(self):
        """return all differents geneNetwork in population"""
        genotypes = []
        for genenet in self.indivs:
            if not any(genenet == i for i in genotypes):
                genotypes.append(genenet)
        return genotypes

    @property
    def profiles(self):
        """Return a tuple of two numpy matrices, 
        that contains means and standard variance 
        of each individual in population"""
        summed_values = defaultdict(list)
        nb_gene = self.indivs[0].gene_number
        
        # sum all values of each gene of each individual
        for genome in (array(_.genome) for _ in self.indivs):
            for gene in range(nb_gene):
                values = array(genome[gene])
                for col in range(len(values)):
                    summed_values[gene, col].append(values[col])

        # get means and std deviation
        means = {k:mean(v) for k, v in summed_values.items()}
        varis = {k:variance(v, means[k]) for k, v in summed_values.items()}
        return means, varis
        





