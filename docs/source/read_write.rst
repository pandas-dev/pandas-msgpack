.. _read_write:

.. ipython:: python
   :suppress:

   import pandas as pd


Read/Write API
--------------

Msgpacks can also be read from and written to strings.

.. ipython:: python

   df.to_msgpack()

Furthermore you can concatenate the strings to produce a list of the original objects.

.. ipython:: python

  pd.read_msgpack(df.to_msgpack() + s.to_msgpack())
