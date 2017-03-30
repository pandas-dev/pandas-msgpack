To build a local copy of the pandas-msgpack docs, install the programs in
requirements-docs.txt and run 'make html'. If you use the conda package manager
these commands suffice::

  git clone git@github.com:pydata/pandas-msgpack.git
  cd dask/docs
  conda create -n pandas-msgpack-docs --file requirements-docs.txt
  source activate pandas-msgpack-docs
  make html
  open build/html/index.html
