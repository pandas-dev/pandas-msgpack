*   Tag commit

        git tag -a x.x.x -m 'Version x.x.x'

*   and push to github

        git push origin master --tags

*  Upload to PyPI

        git clean -xfd
        python setup.py register sdist --formats=gztar
        twine upload dist/*

*  Do a pull-request to the feedstock on `pandas-msgpack-feedstock <https://github.com/conda-forge/pandas-msgpack-feedstock/>`__

        update the version
        update the SHA256 (retrieve from PyPI)
