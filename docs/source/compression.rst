.. _compression:

.. ipython:: python
   :suppress:

   import pandas as pd
   import os

Compression
-----------

Optionally, a ``compression`` argument will compress the resulting bytes.
These can take a bit more time to write. The available compressors are
``zlib`` and `blosc <https://pypi.python.org/pypi/blosc>`__.

Generally compression will increase the writing time.

.. ipython:: python

   import pandas as pd
   from pandas_msgpack import to_msgpack, read_msgpack

   df = pd.DataFrame({'A': np.arange(100000),
                      'B': np.random.randn(100000),
                      'C': 'foo'})

.. ipython:: python

   %timeit -n 1 -r 1 to_msgpack('uncompressed.msg', df)

.. ipython:: python

   %timeit -n 1 -r 1 to_msgpack('compressed_blosc.msg', df, compress='blosc')

.. ipython:: python

   %timeit -n 1 -r 1 to_msgpack('compressed_zlib.msg', df, compress='zlib')

If compressed, it will be be automatically inferred and de-compressed upon reading.

.. ipython:: python

   %timeit -n 1 -r 1 read_msgpack('uncompressed.msg')

.. ipython:: python

   %timeit -n 1 -r 1 read_msgpack('compressed_blosc.msg')

.. ipython:: python

   %timeit -n 1 -r 1 read_msgpack('compressed_zlib.msg')

These can provide storage space savings.

.. ipython:: python

   !ls -ltr *.msg

.. ipython:: python
   :suppress:
   :okexcept:

   os.remove('uncompressed.msg')
   os.remove('compressed_blosc.msg')
   os.remove('compressed_zlib.msg')
