build:
	pip install -r requirements.txt
	pip install -e .


test:
	pytest -svv --cov hrank
