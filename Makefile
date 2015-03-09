OPTIONS=
STATS=--erase_previous_stats --do_stats --save_profiles
PHENO_ALT=--initial_phenotype=-1,1,-1,1,-1

run_genomat:
	python3 -m genomat --generations=200 --pop_size=300 --gene_number=5 --mutation_rate=0.01 --stats_file="doc/200x300x2.csv" $(OPTION) $(STATS)
	python3 -m genomat --generations=200 --pop_size=300 --gene_number=5 --mutation_rate=0.01 $(PHENO_ALT) --stats_file="doc/200x300x2xmpmpm.csv" $(STATS)
	python3 -m genomat --generations=200 --pop_size=300 --gene_number=5 --mutation_rate=0.001 --stats_file="doc/200x300x3.csv" $(OPTION) $(STATS)
	python3 -m genomat --generations=200 --pop_size=300 --gene_number=5 --mutation_rate=0.0001 --stats_file="doc/200x300x4.csv" $(OPTION) $(STATS)

test_computation:
	python3 -m genomat $(PHENO_ALT) --mutation_rate=0.1 --pop_size=50 --generations=20 $(OPTIONS) $(STATS)

computation:
	python3 -m genomat --generations=300 --pop_size=100 --mutation_rate=0.1		--stats_file="doc/300x100x1.csv" $(OPTIONS) $(STATS)
	python3 -m genomat --generations=300 --pop_size=100 --mutation_rate=0.01	--stats_file="doc/300x100x2.csv" $(OPTIONS) $(STATS)
	python3 -m genomat --generations=300 --pop_size=100 --mutation_rate=0.0001	--stats_file="doc/300x100x4.csv" $(OPTIONS) $(STATS)
	python3 -m genomat --generations=300 --pop_size=100 --mutation_rate=0.000001	--stats_file="doc/300x100x6.csv" $(OPTIONS) $(STATS)
	python3 -m genomat --generations=150 --pop_size=100 --mutation_rate=0.000001	--stats_file="doc/150x100x6.csv" $(OPTIONS) $(STATS)

do_config:
	python3 -m genomat --save_config

tt:
	python3 unittests.py

run_genomat_func:
	python3 -m genomat_func


clear:
	rm data/stats.csv
