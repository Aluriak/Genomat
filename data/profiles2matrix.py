


from math import sqrt
import csv
import sys
fields = 'generation,mean0x0,mean0x1,mean0x2,mean0x3,mean0x4,mean1x0,mean1x1,mean1x2,mean1x3,mean1x4,mean2x0,mean2x1,mean2x2,mean2x3,mean2x4,mean3x0,mean3x1,mean3x2,mean3x3,mean3x4,mean4x0,mean4x1,mean4x2,mean4x3,mean4x4,stdev0x0,stdev0x1,stdev0x2,stdev0x3,stdev0x4,stdev1x0,stdev1x1,stdev1x2,stdev1x3,stdev1x4,stdev2x0,stdev2x1,stdev2x2,stdev2x3,stdev2x4,stdev3x0,stdev3x1,stdev3x2,stdev3x3,stdev3x4,stdev4x0,stdev4x1,stdev4x2,stdev4x3,stdev4x4'.split(',')



if __name__ == '__main__':
    assert(len(sys.argv) == 2)
    # get last line in csv format of given file
    last_entry = None
    with open(sys.argv[1], 'r') as fcsv:
        reader = csv.DictReader(fcsv, fieldnames=fields)
        for line in reader:
            last_entry = line
    #print(last_entry)


    # generate latex-like string
    #output  = ''
    output  = '\\begin{pmatrix}'
    nb_gene = int(sqrt((len(fields) - 1) // 2))
    print('NB_GENE (detected):', nb_gene)
    assert(nb_gene == 5)
    for i in range(nb_gene):
        output += '\n'
        for j in range(nb_gene):
            coords = str(i) + 'x' + str(j)
            mean_val = 'mean' + coords
            varc_val = 'stdev' + coords
            output += (str(round(float(last_entry[mean_val]), 2)) 
                       + ' +- ' 
                       +  str(round(float(last_entry[varc_val]), 2)) + ' & ')
        output = output.rstrip(' \t& \t') + ' \\\\'

    output = output.rstrip('\\\\') + '\n\\end{pmatrix}\n'

    # print it
    print(output)


