OPTIONS=
POP_DEFAULT=--generations=200 --pop_size=300 
STATS=--erase_previous_stats --do_stats --save_profiles
PHENO_ALT1=--initial_phenotype=-1,1,-1,1,-1
PHENO_ALT1=--initial_phenotype=1,-1,1,-1,1
SEED=--seed=4223 

	
test_computation:
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.00001 --profiles_file="doc/test_p.csv" --stats_file="doc/test.csv" $(OPTIONS) $(STATS)

###############################################################################
# PROJECT TEST CASES
###############################################################################
#parameters given by needed for the report
computation1:
	# telltale
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.0001	--profiles_file="doc/ps300xg200xmr1-10-4xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-4.csv" $(OPTIONS) $(STATS)
	# mutation rate variation
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=1		--profiles_file="doc/ps300xg200xmr1-10-0xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-0.csv" $(OPTIONS) $(STATS)
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.1		--profiles_file="doc/ps300xg200xmr1-10-1xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-1.csv" $(OPTIONS) $(STATS)
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.01		--profiles_file="doc/ps300xg200xmr1-10-2xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-2.csv" $(OPTIONS) $(STATS)
	# initial phenotype variation
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.0001	--profiles_file="doc/ps300xg200xmr1-10-4xalt1xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-4xalt1.csv" $(OPTIONS) $(STATS) $(PHENO_ALT1)
	# population size and parent count variation  (consanguinity in little population)
	python3 -m genomat $(SEED) --generations=200 --pop_size=20 --mutation_rate=0.0001	--profiles_file="doc/ps20xg200xprt20xmr1-10-4xprfl.csv" --stats_file="doc/ps20xg200xprt20xmr1-10-4.csv" $(OPTIONS) $(STATS) --parent_number=20

computation2:
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.00001	--profiles_file="doc/ps300xg200xmr1-10-5xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-5.csv" $(OPTIONS) $(STATS)
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.000001	--profiles_file="doc/ps300xg200xmr1-10-6xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-6.csv" $(OPTIONS) $(STATS)
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.0000000001	--profiles_file="doc/ps300xg200xmr1-10-10xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-10.csv" $(OPTIONS) $(STATS)
	# parent variation
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.0001	--profiles_file="doc/ps300xg200xmr1-10-4xprt300xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-4xprt300.csv" $(OPTIONS) $(STATS) --parent_number=300
	# initial phenotype variation
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.0001	--profiles_file="doc/ps300xg200xmr1-10-4xalt2xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-4xalt2.csv" $(OPTIONS) $(STATS) $(PHENO_ALT2)
	# population size variation
	python3 -m genomat $(SEED) --generations=200 --pop_size=20 --mutation_rate=0.0001	--profiles_file="doc/ps20xg200xmr1-10-4xprfl.csv" --stats_file="doc/ps20xg200xmr1-10-4.csv" $(OPTIONS) $(STATS)

experience_plan:
	# telltale
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.0001	--profiles_file="doc/ps300xg200xmr1-10-4xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-4.csv" $(OPTIONS) $(STATS)
	# mutation rate variation
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=1		--profiles_file="doc/ps300xg200xmr1-10-0xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-0.csv" $(OPTIONS) $(STATS)
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.1		--profiles_file="doc/ps300xg200xmr1-10-1xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-1.csv" $(OPTIONS) $(STATS)
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.01		--profiles_file="doc/ps300xg200xmr1-10-2xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-2.csv" $(OPTIONS) $(STATS)
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.00001	--profiles_file="doc/ps300xg200xmr1-10-5xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-5.csv" $(OPTIONS) $(STATS)
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.000001	--profiles_file="doc/ps300xg200xmr1-10-6xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-6.csv" $(OPTIONS) $(STATS)
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.0000000001	--profiles_file="doc/ps300xg200xmr1-10-10xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-10.csv" $(OPTIONS) $(STATS)
	# parent variation
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.0001	--profiles_file="doc/ps300xg200xmr1-10-4xprt300xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-4xprt300.csv" $(OPTIONS) $(STATS) --parent_number=300
	# initial phenotype variation
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.0001	--profiles_file="doc/ps300xg200xmr1-10-4xalt1xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-4xalt1.csv" $(OPTIONS) $(STATS) $(PHENO_ALT1)
	python3 -m genomat $(SEED) $(POP_DEFAULT) --mutation_rate=0.0001	--profiles_file="doc/ps300xg200xmr1-10-4xalt2xprfl.csv" --stats_file="doc/ps300xg200xmr1-10-4xalt2.csv" $(OPTIONS) $(STATS) $(PHENO_ALT2)
	# population size variation
	python3 -m genomat $(SEED) --generations=200 --pop_size=20 --mutation_rate=0.0001	--profiles_file="doc/ps20xg200xmr1-10-4xprfl.csv" --stats_file="doc/ps20xg200xmr1-10-4.csv" $(OPTIONS) $(STATS)
	# population size and parent count variation  (consanguinity in little population)
	python3 -m genomat $(SEED) --generations=200 --pop_size=20 --mutation_rate=0.0001	--profiles_file="doc/ps20xg200xprt20xmr1-10-4xprfl.csv" --stats_file="doc/ps20xg200xprt20xmr1-10-4.csv" $(OPTIONS) $(STATS) --parent_number=20



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
