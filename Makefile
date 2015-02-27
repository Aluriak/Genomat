OPTIONS=

run_genomat:
	python3 -m genomat $(OPTIONS)

test_computation:
	python3 -m genomat --erase_previous_stats --do_stats --mutation_rate=0.1 --pop_size=100 --generations=60 $(OPTIONS)

computation:
	python3 -m genomat --mutation_rate=0.000001 --erase_previous_stats --do_stats --pop_size=100 --generations=150 $(OPTIONS)

do_config:
	python3 -m genomat --save_config

tt:
	python3 unittests.py

run_genomat_func:
	python3 -m genomat_func


clear:
	rm data/stats.csv
