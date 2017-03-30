Changelog
=========

0.1.? / 2017-04-??
------------------

Initial release of transfered code from `pandas <https://github.com/pandas-dev/pandas>`__

Includes patches since the 0.19.2 release on pandas with the following:

- Bug in ``read_msgpack()`` in which ``Series`` categoricals were being improperly processed, see `pandas-GH#14901 <https://github.com/pandas-dev/pandas/pull/14901>`__
- Bug in ``read_msgpack()`` which did not allow loading of a dataframe with an index of type ``CategoricalIndex``, see `pandas-GH#15487 <https://github.com/pandas-dev/pandas/pull/15487>`__
- Bug in ``read_msgpack()`` when deserializing a ``CategoricalIndex``, see `pandas-GH#15487 <https://github.com/pandas-dev/pandas/pull/15487>`__
