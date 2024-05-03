# Perform fast queries in Python against a massive database of complete GWAS summary data

[![Actions Status](https://github.com/MRCIEU/ieugwaspy/workflows/ieugwaspy_test/badge.svg)](https://github.com/MRCIEU/ieugwaspy/actions)

The [IEU OpenGWAS database](https://gwas.mrcieu.ac.uk/) comprises over 50,000 curated, QC'd and harmonised complete GWAS summary datasets and can be queried using an API. See [here](https://api.opengwas.io/api/) for documentation on the API itself. This Python package is a wrapper to make generic calls to the API, plus convenience functions for specific queries.

[See ieugwaspy documentation](https://mrcieu.github.io/ieugwaspy/) for details of how to use this package.

### Installation

Install using ```pip install ieugwaspy```

### Features

- Get meta data about specific or all studies
- Obtain the top hits (with on the fly clumping as an option) from each of the GWAS datasets. Clumping and significance thresholds can be specified
- Obtain the summary results of specific variants across specific studies. LD-proxy lookups are performed automatically if a specific variant is absent from a study
- Perform PheWAS (look up all associations for a variant)
- Convert between chromosome:position and rsids and getting annotations


#### Developer notes
To run tests, use `pytest -v -s --select-api="dev"`

To generate docs, use `pdoc --html ieugwaspy; rm -rf docs/; mkdir docs; mv html/ieugwaspy/* docs/; rm -r html/`
