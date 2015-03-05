OPTIONS=
STATS=--erase_previous_stats --do_stats 
PHENO_ALT=--initial_phenotype=-1,1,-1,1,-1

run_genomat:
	python3 -m genomat --generations=200 --pop_size=300 --gene_number=5 --mutation_rate=0.01$(OPTION) $(STATS)
	mv data/stats.csv doc/200x300x2.csv
	python3 -m genomat --generations=200 --pop_size=300 --gene_number=5 --mutation_rate=0.01$(PHENO_ALT) $(STATS)
	mv data/stats.csv doc/200x300x2xmpmpm.csv
	python3 -m genomat --generations=200 --pop_size=300 --gene_number=5 --mutation_rate=0.001$(OPTION) $(STATS)
	mv data/stats.csv doc/200x300x3.csv
	python3 -m genomat --generations=200 --pop_size=300 --gene_number=5 --mutation_rate=0.0001$(OPTION) $(STATS)
	mv data/stats.csv doc/200x300x4.csv

test_computation:
	python3 -m genomat --initial_phenotype=1,1,1,1,1 --mutation_rate=0.1 --pop_size=50 --generations=200 $(OPTIONS) $(STATS)

computation:
	python3 -m genomat --generations=300 --pop_size=100 --mutation_rate=0.1 $(OPTIONS) $(STATS)
	mv data/stats.csv doc/300x100x1.csv
	python3 -m genomat --generations=300 --pop_size=100 --mutation_rate=0.01 $(OPTIONS) $(STATS)
	mv data/stats.csv doc/300x100x2.csv
	python3 -m genomat --generations=300 --pop_size=100 --mutation_rate=0.0001 $(OPTIONS) $(STATS)
	mv data/stats.csv doc/300x100x4.csv
	python3 -m genomat --generations=300 --pop_size=100 --mutation_rate=0.000001 $(OPTIONS) $(STATS)
	mv data/stats.csv doc/300x100x6.csv
	python3 -m genomat --generations=150 --pop_size=100 --mutation_rate=0.000001 $(OPTIONS) $(STATS)
	mv data/stats.csv doc/150x100x6.csv

do_config:
	python3 -m genomat --save_config

tt:
	python3 unittests.py

run_genomat_func:
	python3 -m genomat_func


clear:
	rm data/stats.csv
