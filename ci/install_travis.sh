#!/bin/bash

# install miniconda
MINICONDA_DIR="$HOME/miniconda3"

if [ -d "$MINICONDA_DIR" ]; then
    rm -rf "$MINICONDA_DIR"
fi

# install miniconda
if [ "${TRAVIS_OS_NAME}" == "osx" ]; then
    wget http://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O miniconda.sh || exit 1
else
    wget http://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh || exit 1
fi
bash miniconda.sh -b -p "$MINICONDA_DIR" || exit 1

conda config --set ssl_verify false || exit 1
conda config --set always_yes true --set changeps1 false || exit 1
conda update -q conda

conda info -a || exit 1

conda create -n test-environment python=$PYTHON cython pytest
source activate test-environment

pip install coverage pytest-cov flake8 codecov
if [ $PANDAS == 'master' ]; then

   echo "installing deps"
   pip install numpy pytz python-dateutil

   echo "installing pandas master wheel"
   PRE_WHEELS="https://7933911d6844c6c53a7d-47bd50c35cd79bd838daf386af554a83.ssl.cf2.rackcdn.com"
   pip install --pre --timeout=60 -f $PRE_WHEELS pandas==0.19.0+699.gecaeea1

else
    conda install pandas=$PANDAS
fi

REQ="ci/requirements-${PYTHON}.pip"
if [ -e $REQ ]; then
    pip install -r $REQ;
fi

conda list
python setup.py develop
