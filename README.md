# Perform fast queries in Python against a massive database of complete GWAS summary data

[![Actions Status](https://github.com/MRCIEU/ieugwaspy/workflows/ieugwaspy_test/badge.svg)](https://github.com/MRCIEU/ieugwaspy/actions)

The [IEU GWAS database](https://gwas.mrcieu.ac.uk/) comprises over 10,000 curated, QC'd and harmonised complete GWAS summary datasets and can be queried using an API. See [here](http://gwasapi.mrcieu.ac.uk/docs/) for documentation on the API itself. This Python package package is a wrapper to make generic calls to the API, plus convenience functions for specific queries.

Methods to be implemented:

- Get meta data about specific or all studies
- Obtain the top hits (with on the fly clumping as an option) from each of the GWAS datasets. Clumping and significance thresholds can be specified
- Obtain the summary results of specific variants across specific studies. LD-proxy lookups are performed automatically if a specific variant is absent from a study
- Query a genomic region in a GWAS dataset, e.g. for fine mapping or colocalisation analysis
- Perform PheWAS

There are a few convenience functions also to be implemented:

- Query dbSNP data, allowing conversion between chromosome:position and rsids and getting annotations
- Perform LD clumping using the server, or locally
- Obtain LD matrices for a list of SNPs using the server or locally (e.g. for fine mapping, colocalisation or Mendelian randomization)
