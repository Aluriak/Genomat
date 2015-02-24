# -*- coding: utf-8 -*-
#########################
#       PROGRESSBAR     #
#########################
"""
Few functions for dirty and quick progress bar in stdout.
"""


#########################
# IMPORTS               #
#########################
import sys



#########################
# PRE-DECLARATIONS      #
#########################
LOADING_BAR_SIZE = 80
LOADING_BAR_SIZE_NO_SEP = LOADING_BAR_SIZE - 2
# -2: for [ and ] delimiters
LOADING_BAR_SIZE_FINAL  = LOADING_BAR_SIZE_NO_SEP + 1
# +1: for > character, the head of the bar



#########################
# FUNCTIONS             #
#########################
def create_progress_bar(prefix=''):
    """Print an empty progress bar"""
    print(prefix+'[' + LOADING_BAR_SIZE_FINAL*' ' + ']', end='')
    sys.stdout.flush()

def update_progress_bar(generation_number, total):
    """"""
    ratio = int((generation_number / total) * LOADING_BAR_SIZE_NO_SEP)
    ratio += 1
    print('\r[' + ratio*'#' + '>' + (LOADING_BAR_SIZE_NO_SEP-ratio)*' ' + ']', end='')
    sys.stdout.flush()

def finish_progress_bar():
    print('\r[' + LOADING_BAR_SIZE_FINAL*'#' + ']')




