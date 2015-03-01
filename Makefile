OPTIONS=
STATS=--erase_previous_stats --do_stats 

run_genomat:
	python3 -m genomat $(OPTIONS) $(STATS)

test_computation:
	python3 -m genomat --mutation_rate=0.1 --pop_size=10 --generations=60 $(OPTIONS) $(STATS)

computation:
	python3 -m genomat --mutation_rate=0.000001 --pop_size=100 --generations=150 $(OPTIONS) $(STATS)

do_config:
	python3 -m genomat --save_config

tt:
	python3 unittests.py

run_genomat_func:
	python3 -m genomat_func


clear:
	rm data/stats.csv
