Changelog
=========

0.1.0 / 2017-04-??
------------------

Initial release of transfered code from `pandas <https://github.com/pandas-dev/pandas>`__

Includes patches since the 0.19.2 release on pandas with the following:

- ``read_gbq`` now stores ``INTEGER`` columns as ``dtype=object`` if they contain ``NULL`` values. Otherwise they are stored as ``int64``. This prevents precision lost for integers greather than 2**53. Furthermore ``FLOAT`` columns with values above 10**4 are no longer casted to ``int64`` which also caused precision loss `pandas-GH#14064 <https://github.com/pandas-dev/pandas/pull/14064>`__, and `pandas-GH#14305 <https://github.com/pandas-dev/pandas/pull/14305>`__
