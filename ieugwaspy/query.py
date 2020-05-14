"""API query functions
"""
import json
import os
import requests

from retry import retry
from urllib.parse import urljoin

import ieugwaspy.constants as cons
import ieugwaspy.variants as variants
import ieugwaspy.backwards as backwards

MAX_TRIES = 10
TRIES_DELAY = 2  # 2 seconds
TRIES_BACKOFF = 2

@retry(tries=MAX_TRIES, delay=TRIES_DELAY, backoff=TRIES_BACKOFF)
def api_query(path, query="", method="GET", access_token=cons.api_token):
    """This is a general-purpose function called by other functions to query the API and return the resulting data in JSON format.  

    Parameters:
        path: the path component of the URL
        query: any query to go after the ?query component of the URL
        access_token: the OAuth access token

    Returns:
        data: json object as returned by API

    """
    url = urljoin(cons.option["mrbaseapi"], path)
    
    if method == "GET":
        payload = {"access_token": access_token}
        if query != "":
            payload['query'] = query

        response = requests.get(url, params=payload)
    elif method == "POST":
        response = requests.post(url, data=query)
    else:
        return "Invalid API method"
    return response.json()


def api_status():
    """Check API status

    Returns:
        data: API status 

    """
    data = api_query("status")
    return data


def gwasinfo(id="", access_token=cons.api_token):
    """This function will return GWAS study meta-data describing the specific studies selected by id

    Parameters:
        id: ID(s) of specific studies (Python list)
        access_token: the OAuth access token

    Returns:
        data: json object as returned by API

    """
    id = ",".join(id)
    if id != "":
        data = api_query("gwasinfo/{}".format(id), access_token=access_token)
    else:
        data = api_query("gwasinfo", access_token=access_token)
    return data


def associations(
    variantlist,
    id,
    proxies=1,
    r2=0.8,
    align_alleles=1,
    palindromes=1,
    maf_threshold=0.3,
    access_token=cons.api_token,
):
    """Retrieve associations for specific SNP/study combinations

    Parameters:
        variantlist: list of variants (Python list)
        id: list of study IDs (Python list)
        proxies: proxies 0 or (default) 1 - indicating whether to look for proxies
        r2: minimum proxy LD rsq value. Default=0.8
        align_alleles: try to align tag alleles to target alleles (if proxies = 1). 1 = yes (default), 0 = no
        palindromes: allow palindromic SNPs (if proxies = 1). 1 = yes (default), 0 = no
        maf_threshold: MAF threshold to try to infer palindromic SNPs. Default = 0.3.
        access_token: the OAuth access token

    Returns:
        data: json object as returned by API

    """
    id = backwards.legacy_ids(id)
    data = {
        "variant": variantlist,
        "id": id,
        "proxies": proxies,
        "r2": r2,
        "align_alleles": align_alleles,
        "palindromes": palindromes,
        "maf_threshold": maf_threshold,
        "access_token": access_token,
    }
    result = api_query("associations", query=data, method="POST")
    return result


def phewas(variantlist, pval=1e-3, access_token=cons.api_token):
    """Perform phenome-wide association analysis (PheWAS) of variant(s) across all traits in the IEU GWAS database

    Parameters:
        variants: list of variants (Python list)
        pval: p-value threshold
        access_token: the OAuth access token

    Returns:
        data: json object as returned by API

    """
    rsid = ",".join(variants.variants_to_rsid(variantlist))
    data = api_query("phewas/{}/{}".format(rsid, pval), access_token=access_token)
    return data


def tophits(
    id,
    pval=5e-8,
    clump=1,
    r2=0.001,
    kb=10000,
    force_server=False,
    access_token=cons.api_token,
):
    """Retrieve association data for specific SNP/study combinations 

    Parameters:
        id: list of study IDs (Python list)
        pval: use this p-value threshold. Default = 5e-8
        clump: whether to clump (1) or not (0). Default = 1
        r2: use this clumping r2 threshold. Default is very strict, 0.001
        kb: use this clumping kb window. Default is very strict, 10000
        force_server: True/False. By default (False) will return preclumped hits. p-value threshold 5e-8, with r2 threshold 0.001 and kb threshold 10000, using only SNPs with MAF > 0.01 in the European samples in 1000 genomes. If force_server = TRUE then will recompute using server side LD reference panel.
        access_token: the OAuth access token

    Returns:
        data: json object as returned by API

    """
    id = backwards.legacy_ids(id)
    if clump == 1 and r2 == 0.001 and kb == 10000 and pval == 5e-8:
        preclumped = 1
    else:
        preclumped = 0
    if preclumped == 1 and force_server:
        preclumped = 0
    data = {
        "id": id,
        "pval": pval,
        "preclumped": preclumped,
        "clump": clump,
        "r2": r2,
        "kb": kb,
        "access_token": access_token,
    }
    result = api_query("tophits", query=data, method="POST")
    return result
