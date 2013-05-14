#!/bin/bash
PYTHON=${PYTHON:=`which python2.7`}
git submodule init && git submodule update
cd src/Products.RhaptosPrint
git submodule init && git submodule update
cd ../../
$PYTHON bootstrap.py -c buildout.cfg
bin/buildout -c buildout.cfg
./init-db.sh
