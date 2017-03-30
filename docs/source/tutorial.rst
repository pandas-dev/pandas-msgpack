.. _tutorial:

.. ipython:: python
   :suppress:

   import pandas as pd
   import os

Tutorial
--------

.. ipython:: python

   import pandas as pd
   from pandas_msgpack import to_msgpack, read_msgpack

.. ipython:: python

   df = pd.DataFrame(np.random.rand(5,2), columns=list('AB'))
   to_msgpack('foo.msg', df)
   read_msgpack('foo.msg')
   s = pd.Series(np.random.rand(5),index=pd.date_range('20130101',periods=5))

You can pass a list of objects and you will receive them back on deserialization.

.. ipython:: python

   to_msgpack('foo.msg', df, 'foo', np.array([1,2,3]), s)
   read_msgpack('foo.msg')

You can pass ``iterator=True`` to iterate over the unpacked results

.. ipython:: python

   for o in read_msgpack('foo.msg',iterator=True):
       print(o)

You can pass ``append=True`` to the writer to append to an existing pack

.. ipython:: python

   to_msgpack('foo.msg', df, append=True)
   read_msgpack('foo.msg')

Furthermore you can pass in arbitrary python objects.

.. ipython:: python

   to_msgpack('foo2.msg', { 'dict' : [ { 'df' : df }, { 'string' : 'foo' }, { 'scalar' : 1. }, { 's' : s } ] })
   read_msgpack('foo2.msg')

.. ipython:: python
   :suppress:
   :okexcept:

   import os
   os.remove('foo.msg')
   os.remove('foo2.msg')
