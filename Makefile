OPTIONS=
STATS=--erase_previous_stats --do_stats --save_profiles
PHENO_ALT=--initial_phenotype=-1,1,-1,1,-1

	
test_computation:
	python3 -m genomat --generations=200 --pop_size=300 --mutation_rate=1   	--stats_file="doc/ps300xg200xmr1-10-0.csv" $(OPTIONS) $(STATS)
	#python3 -m genomat $(PHENO_ALT) --mutation_rate=0.1 --pop_size=50 --generations=20 $(OPTIONS) $(STATS)

###############################################################################
# PROJECT TEST CASES
###############################################################################
#parameters given by needed for the report
computation:
	python3 -m genomat --generations=200 --pop_size=300 --mutation_rate=1   	--stats_file="doc/ps300xg200xmr1-10-0.csv" $(OPTIONS) $(STATS)
	python3 -m genomat --generations=200 --pop_size=300 --mutation_rate=0.1		--stats_file="doc/ps300xg200xmr1-10-1.csv" $(OPTIONS) $(STATS)
	python3 -m genomat --generations=200 --pop_size=300 --mutation_rate=0.01	--stats_file="doc/ps300xg200xmr1-10-2.csv" $(OPTIONS) $(STATS)
	python3 -m genomat --generations=200 --pop_size=300 --mutation_rate=0.01	--stats_file="doc/ps300xg200xmr1-10-2xmpmpm.csv" $(STATS) $(PHENO_ALT)
computation2:
	python3 -m genomat --generations=200 --pop_size=300 --mutation_rate=0.001	--stats_file="doc/ps300xg200xmr1-10-3.csv" $(OPTIONS) $(STATS)
	python3 -m genomat --generations=200 --pop_size=300 --mutation_rate=0.0001	--stats_file="doc/ps300xg200xmr1-10-4.csv" $(OPTIONS) $(STATS)
	python3 -m genomat --generations=200 --pop_size=300 --mutation_rate=0.000001	--stats_file="doc/ps300xg200xmr1-10-6.csv" $(OPTIONS) $(STATS)
	python3 -m genomat --generations=200 --pop_size=300 --mutation_rate=0.000001	--stats_file="doc/ps300xg200xmr1-10-6.csv" $(OPTIONS) $(STATS)


###############################################################################
# USE CASES
###############################################################################
do_config:
	python3 -m genomat --save_config

tt:
	python3 unittests.py

run_genomat_func:
	python3 -m genomat_func


clear:
	rm data/stats.csv


###############################################################################
# TOOLS
###############################################################################
verif:
	pylint genomat/__main__.py

uml: 
	pyreverse -o png genomat -p genomat
	mkdir -p doc/diagrams
	mv packages_* classes_* doc/diagrams/
