# -*- coding: utf-8 -*-



from individual import Individual
import random


class Population:

    def __init__(self, pop_size, parent_cross_count=2):
        """The population is defined by the number of individual it is composed of.
        IN:
            A number of individuals
            Count of parents for crossing (default is 2)
        OUT:
            A population
        """
        self.generate_pop(pop_size)
        self.parent_cross_count = parent_cross_count

    def generate_pop(self, pop_size):
        """Generate a new population
        IN:
            Individuals
        OUT:
            A population
        """
        self.indivs = []
        for _ in range(pop_size):
            self.indivs.append(Individual(None)) #TODO: generate matrix

    def size(self):
        """Returns the population's size.
        IN:
            The population
        OUT:
            The population's size
        """
        return len(self.indivs)

    def step(self, pop_size=None):
        """Pass to the next generation.
        IN:
            Size of next generation population (if None, population size will not be changed)
        OUT:
            A new generation. The previous generation is overwritten.
        """
        new_indivs = []
        pop_size = self.size() if pop_size is None else pop_size
        while len(new_indivs) < pop_size:
            parents = random.sample(self.indivs, self.parent_cross_count)
            test_indiv = Individual.cross_individual(parents)
            if test_indiv.is_viable():
                new_indivs.append(test_indiv)
            # on crée une variable intermédiaire dans laquelle on stocke le nouvel individu le temps de tester sa viabilité
            # on appelle la fonction "is_viable" de Individuals pour tester cet individu
            # si cet individu est viable, on l'ajoute à la nouvelle population
            # sinon, on le supprime
            #new_indivs.append(Individual.cross_individual(parents))

    


    @staticmethod
    def random_phenotype(size, generator=lambda:random.choice((-1, 0, 1))):
        """return a random phenotype, of given size and generator"""
        return matrix([[generator()] for _ in range(size)])

    @staticmethod
    def default_phenotype(size):
        """Return phenotype of given size"""
        return matrix([[1] for _ in range(size)])

    @staticmethod
    def create_phenotype(values):
        """Return phenotype with given values"""
        return matrix([[v] for v in values])



