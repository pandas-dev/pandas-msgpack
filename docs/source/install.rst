Installation
============

You can install pandas-msgpack with ``conda``, ``pip``, or by installing from source.

Conda
-----

.. code-block:: shell

   $ conda install pandas-msgpack --channel conda-forge

This installs pandas-msgpack and all common dependencies, including ``pandas``.

Pip
---

To install the latest version of pandas-msgpack: from the

.. code-block:: shell

    $ pip install pandas-msgpack -U

This installs pandas-msgpack and all common dependencies, including ``pandas``.


Install from Source
-------------------

.. code-block:: shell

    $ pip install git+https://github.com/pydata/pandas-msgpack.git


Dependencies
------------

This module requires following additional dependencies:

- `httplib2 <https://github.com/httplib2/httplib2>`__: HTTP client
- `google-api-python-client <http://github.com/google/google-api-python-client>`__: Google's API client
- `oauth2client <https://github.com/google/oauth2client>`__: authentication and authorization for Google's API
