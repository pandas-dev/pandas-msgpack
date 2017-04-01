# flake8: noqa

# pandas versioning
import pandas

from distutils.version import LooseVersion
pv = LooseVersion(pandas.__version__)

if pv < '0.19.0':
    raise ValueError("pandas_msgpack requires at least pandas 0.19.0")
_is_pandas_legacy_version = pv.version[1] == 19 and len(pv.version) == 3

from .packers import to_msgpack, read_msgpack

# versioning
from ._version import get_versions

versions = get_versions()
__version__ = versions.get('closest-tag', versions['version'])
__git_revision__ = versions['full-revisionid']
del get_versions, versions, pv, LooseVersion, pandas
