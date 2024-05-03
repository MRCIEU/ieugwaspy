"""SNP/variant helper functions
"""


def variants_chrpos(chrpos):
    """This function returns the dbSNP rsid for a single variant in chr:pos format. Note: only the first rsid will be returned

    Args:
        chrpos (str): variant in `chr:pos` format

    Returns:
        result: single variant rsid string

    """
    import ieugwaspy.query as query

    variantdata = query._api_query("variants/chrpos/{}".format(chrpos))
    result = variantdata[0][0]["_id"]
    return result


def variants_to_rsid(variants):
    """This function returns dbSNP rsid for variants provided in chr:pos format, calling the variants_chrpos() function for each variant. Note: only one rsid will be returned for each chr:pos

    Args:
        variants (list): variants in chr:pos format (leaves rsids unchanged), e.g. ["rs1234", "10:44865737"]

    Returns:
        variants: list of variant rsids

    """
    for pos, variant in enumerate(variants):
        if variant.find(":") > 0:
            variants[pos] = variants_chrpos(variant)
    return variants
