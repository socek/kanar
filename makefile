all: venv_rotarran/bin/python

venv_rotarran:
	virtualenv $@

venv_rotarran/bin/python: venv_rotarran setup.py
	source ./venv_rotarran/bin/activate && python setup.py develop
	touch $@
