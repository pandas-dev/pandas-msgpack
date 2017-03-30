.. _tutorial:

Tutorial
--------

.. ipython:: python

   import pandas as pd

.. ipython:: python

   df = pd.DataFrame(np.random.rand(5,2), columns=list('AB'))
   df.to_msgpack('foo.msg')
   pd.read_msgpack('foo.msg')
   s = pd.Series(np.random.rand(5),index=pd.date_range('20130101',periods=5))

You can pass a list of objects and you will receive them back on deserialization.

.. ipython:: python

   pd.to_msgpack('foo.msg', df, 'foo', np.array([1,2,3]), s)
   pd.read_msgpack('foo.msg')

You can pass ``iterator=True`` to iterate over the unpacked results

.. ipython:: python

   for o in pd.read_msgpack('foo.msg',iterator=True):
       print o

You can pass ``append=True`` to the writer to append to an existing pack

.. ipython:: python

   df.to_msgpack('foo.msg', append=True)
   pd.read_msgpack('foo.msg')

Unlike other io methods, ``to_msgpack`` is available on both a per-object basis,
``df.to_msgpack()`` and using the top-level ``pd.to_msgpack(...)`` where you
can pack arbitrary collections of python lists, dicts, scalars, while intermixing
pandas objects.

.. ipython:: python

   pd.to_msgpack('foo2.msg', { 'dict' : [ { 'df' : df }, { 'string' : 'foo' }, { 'scalar' : 1. }, { 's' : s } ] })
   pd.read_msgpack('foo2.msg')

.. ipython:: python
   :suppress:
   :okexcept:

   import os
   os.remove('foo.msg')
   os.remove('foo2.msg')

Compression
-----------

Optionally, a ``compression`` argument will compress the resulting bytes.
These can take a bit more time to write.

.. ipython:: python

   df = pd.DataFrame(np.random.randn(100000, 10))

.. ipython:: python

   %timeit df.to_msgpack('uncompressed.msg')

.. ipython:: python

   %timeit df.to_msgpack('compressed_blosc.msg', compression='blosc')

.. ipython:: python

   %timeit df.to_msgpack('compressed_zlib.msg', compression='zlib')

If compressed, it will be be automatically inferred and de-compressed upon reading.

.. ipython:: python

   %timeit pd.read_msgpack('uncompressed.msg')

.. ipython:: python

   %timeit pd.read_msgpack('compressed_blosc.msg')

.. ipython:: python

   %timeit pd.read_msgpack('compressed_blosc.msg')

.. ipython:: python
   :suppress:
   :okexcept:

   os.remove('uncompressed.msg')
   os.remove('compressed_blosc.msg')
   os.remove('compressed_zlib.msg')


Read/Write API
--------------

Msgpacks can also be read from and written to strings.

.. ipython:: python

   df.to_msgpack()

Furthermore you can concatenate the strings to produce a list of the original objects.

.. ipython:: python

  pd.read_msgpack(df.to_msgpack() + s.to_msgpack())
