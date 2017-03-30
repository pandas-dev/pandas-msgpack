.. _tutorial:

.. ipython:: python
   :suppress:

   import pandas as pd
   import os

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
       print(o)

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
