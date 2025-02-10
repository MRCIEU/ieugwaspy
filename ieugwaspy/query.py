"""API query functions
"""
import datetime
import time
import requests
from retry import retry
from urllib.parse import urljoin

import ieugwaspy.config as config
import ieugwaspy.variants as variants
import ieugwaspy.backwards as backwards


def _check_allowance_reset_timestamp():
    """Check existence of config.allowance_reset_timestamp, reset it when the time has passed or if not, halt the request
    """
    if config.allowance_reset_timestamp == 0:
        return
    if int(time.time()) > config.allowance_reset_timestamp:
        config.allowance_reset_timestamp = 0
    else:
        raise Exception("You have run out of allowance. Please retry after {}".format(datetime.datetime.strftime(datetime.datetime.fromtimestamp(config.allowance_reset_timestamp).astimezone(), '%Y-%m-%d %H:%M %Z')))


def _save_allowance_reset_timestamp(headers):
    """Calculate and save the retry timestamp when there is no remaining allowance

    Args:
        headers: response headers
    """
    if headers.get('X-Allowance-Remaining', None) == "0":
        config.allowance_reset_timestamp = int(time.time()) + int(headers.get('Retry-After', 0))


@retry(tries=5, delay=2, backoff=2)
def _api_query(path, method="GET", data={}):
    """This is a general-purpose function called by other functions to query the API and return the resulting data in JSON format.  

    Args:
        path: the path component of the URL
        method: the HTTP method
        data: the form data

    Returns:
        data: JSON object as returned by API

    """
    url = urljoin(config.env["base_url"], path)

    headers = {
        "X-API-SOURCE": "ieugwaspy/" + config.__version__
    }
    if config.env["jwt"]:
        headers["Authorization"] = "Bearer " + config.env["jwt"]
    if config.env["test_mode_key"]:
        headers["X-TEST-MODE-KEY"] = config.env["test_mode_key"]

    if method == "GET":
        response = requests.get(url, headers=headers)
    elif method == "POST":
        response = requests.post(url, headers=headers, data=data)
    else:
        raise Exception("Invalid API method")

    try:
        _check_allowance_reset_timestamp()
    except Exception as e:
        return str(e)

    try:
        _save_allowance_reset_timestamp(response.headers)
        return response.json()
    except Exception as e:
        raise Exception("Unable to parse the response. " + str(e))


def status():
    """Check API status

    Returns:
        result: JSON object as returned by API

    """
    return _api_query("status")


def user():
    """Get user information

    Returns:
        result: JSON object as returned by API

    """
    return _api_query("user")


def gwasinfo(id=[]):
    """This function will return GWAS study meta-data describing the specific studies selected by id

    Args:
        id (list): OpenGWAS IDs of specific studies, e.g. ["ieu-a-1239", "ieu-a-2"]

    Returns:
        result: JSON object as returned by API

    """
    if id != []:
        return _api_query("gwasinfo", method="POST", data={
            "id": backwards.legacy_ids(id)
        })
    else:
        return _api_query("gwasinfo")


def gwasinfo_files(id):
    """This function will return temporary links to files available for the specific studies selected by id

    Args:
        id (list): OpenGWAS IDs of specific studies, e.g. ["ieu-a-1239", "ieu-a-2"]

    Returns:
        result: JSON object as returned by API

    """
    return _api_query("gwasinfo/files", method="POST", data={
        "id": backwards.legacy_ids(id)
    })


def associations(
        variant,
        id,
        proxies=1,
        r2=0.8,
        align_alleles=1,
        palindromes=1,
        maf_threshold=0.3
):
    """Retrieve associations for specific SNP/study combinations

    Args:
        variant (list): list of variants, e.g. ["rs1205", "7:105561135", "7:105561135-105563135"]
        id (list): list of OpenGWAS IDs, e.g. ["ieu-a-1239", "ieu-a-2"]
        proxies (int): `1` or `0`, whether to look for proxies (1, default) or not (0)
        r2 (float): minimum proxy LD rsq value. Default = 0.8
        align_alleles (int): `1` or `0`, whether to try to align tag alleles to target alleles (1, default) or not (0). Only active when proxies = 1
        palindromes (int): `1` or `0`, whether to allow palindromic SNPs (1, default) or not (0). Only active when proxies = 1
        maf_threshold (float): MAF threshold to try to infer palindromic SNPs. Default = 0.3

    Returns:
        result: JSON object as returned by API

    """
    return _api_query("associations", method="POST", data={
        "variant": variant,
        "id": backwards.legacy_ids(id),
        "proxies": proxies,
        "r2": r2,
        "align_alleles": align_alleles,
        "palindromes": palindromes,
        "maf_threshold": maf_threshold
    })


def phewas(variant, pval=1e-3, batch=[]):
    """Perform phenome-wide association analysis (PheWAS) of variant(s) across all traits in the IEU GWAS database

    Args:
        variant (list): list of variants, e.g. ["rs1205", "7:105561135", "7:105561135-105563135"]
        pval (float): p-value threshold
        batch (list): OpenGWAS data batches, e.g. ["ieu-a"]. Leave empty to search across all batches

    Returns:
        result: JSON object as returned by API

    """
    rsid = ",".join(variants.variants_to_rsid(variant))
    return _api_query("phewas", method="POST", data={
        "variant": rsid,
        "pval": pval,
        "index_list": batch
    })


def tophits(
        id,
        pval=5e-8,
        preclumped=1,
        clump=1,
        bychr=0,
        r2=0.001,
        kb=10000,
        pop="EUR",
        force_server=False
):
    """Retrieve association data for specific SNP/study combinations 

    Args:
        id (list): list of OpenGWAS IDs, e.g. ["ieu-a-1239", "ieu-a-2"]
        pval (float): use this p-value threshold. Default = 5e-8
        preclumped (int): `1` or `0`, whether to use pre-clumped hits (1, default) or not (0)
        clump (int): `1` or `0`, whether to clump (1, default) or not (0)
        bychr (int): `0` or `1`, whether to extract all at once (0, default) or by chromosome (1). There is a limit on query results so bychr might be required for some well-powered datasets
        r2 (float): use this clumping r2 threshold. Default = 0.001 (very strict)
        kb (int): use this clumping kb window. Default = 10000 (very strict)
        pop (str): `EUR`, `SAS`, `EAS`, `AFR`, `AMR` or `legacy`, indicating the population. Default = EUR
        force_server (bool): `True` or `False`. By False (default) it will return preclumped hits with pval = 5e-8, r2 = 0.001 and kb = 10000 and using only SNPs with MAF > 0.01 in the European (EUR) samples in 1000 genomes. If TRUE then it will recompute using server side LD reference panel

    Returns:
        result: JSON object as returned by API

    """
    if clump == 1 and pval == 5e-8 and r2 == 0.001 and kb == 10000:
        preclumped = 0 if force_server else 1
    else:
        preclumped = 0
    return _api_query("tophits", method="POST", data={
        "id": backwards.legacy_ids(id),
        "pval": pval,
        "preclumped": preclumped,
        "clump": clump,
        "bychr": bychr,
        "r2": r2,
        "kb": kb,
        "pop": pop
    })
