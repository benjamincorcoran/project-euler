.PHONEY: setup problem

setup: 
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

problem: 
	.venv/bin/python ./get_problem.py --problem ${problem}