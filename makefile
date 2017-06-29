all: venv_kanar/bin/python

venv_kanar:
	virtualenv $@

venv_kanar/bin/python: venv_kanar scripts/setup.py
	source ./venv_kanar/bin/activate && cd scripts && python setup.py develop
	touch $@
