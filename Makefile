#OPTIONS=--use_db_in_stats

run_genomat:
	python3 -m genomat $(OPTIONS)

test_computation:
	python3 -m genomat --erase_previous_stats --do_stats --pop_size=10 --generations=30 $(OPTIONS)

computation:
	python3 -m genomat --mutation_rate=0.000001 --erase_previous_stats --do_stats --pop_size=100 --generations=150 $(OPTIONS)

tt:
	python3 unittests.py

run_genomat_func:
	python3 -m genomat_func


clear:
	rm data/stats.csv
