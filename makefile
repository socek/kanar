all: venv_rotarran/bin/python

venv_rotarran:
	virtualenv $@

venv_rotarran/bin/python: venv_rotarran scripts/setup.py
	source ./venv_rotarran/bin/activate && cd scripts && python setup.py develop
	touch $@
