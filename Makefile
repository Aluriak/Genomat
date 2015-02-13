

run_genomat:
	python3 -m genomat

tt:
	python3 unittests.py

run_genomat_func:
	python3 -m genomat_func


clear:
	rm data/stats.csv
