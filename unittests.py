# -*- coding: utf-8 -*-
#########################
#       UNITTESTS       #
#########################


#########################
# IMPORTS               #
#########################
import doctest


#########################
# FUNCTIONS             #
#########################
if __name__ == '__main__':
    print('TESTS OF GENENETWORK CLASS…')
    doctest.testfile('genomat/geneNetwork/geneNetwork.py')

    print('ALL TESTS OK !')


