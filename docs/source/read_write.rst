.. _read_write:

.. ipython:: python
   :suppress:

   import pandas as pd


Read/Write API
--------------

Msgpacks can also be read from and written to strings.

.. ipython:: python

   import pandas as pd
   from pandas_msgpack import to_msgpack, read_msgpack

   df = pd.DataFrame({'A': np.arange(10),
                      'B': np.random.randn(10),
                      'C': 'foo'})

   to_msgpack(None, df)

Furthermore you can concatenate the strings to produce a list of the original objects.

.. ipython:: python

  read_msgpack(to_msgpack(None, df) + to_msgpack(None, df.A))
