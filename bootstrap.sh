#!/bin/bash

# ############### #
#   Environment   #
# ############### #
virtualenv -p `which python` --distribute .
PYTHON=$(pwd -P)/bin/python

# ########### #
#   Sources   #
# ########### #
mkdir -p src
cd src
# PyBit
git clone https://github.com/Connexions/pybit.git
cd pybit
git checkout working-copy
$PYTHON setup.py develop
cd ..
# cnx-pybit
git clone https://github.com/Connexions/cnx-pybit.git
cd cnx-pybit
$PYTHON setup.py develop
cd ..
# rbit
git clone https://github.com/Connexions/rbit.git
cd rbit
git checkout consumption-refactoring
$PYTHON setup.py develop
cd ..
# rbit-ext
git clone https://github.com/Connexions/rbit-ext.git
cd rbit-ext
$PYTHON setup.py develop
cd ..
