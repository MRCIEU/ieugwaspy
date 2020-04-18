"""SNP/variant helper functions
"""


def variants_to_rsid(variants):
    """This function returns dbSNP rsid for variants provided in chr:pos format, calling the variants_chrpos function for each variant 

    Parameters:
        variants: list of variants in chr:pos format (Python list) (leaves rsids unchanged)

    Returns:
        data: list of variant rsids (Python list)

    """
    for pos, variant in enumerate(variants):
        if variant.find(":") > 0:
            variants[pos] = variants_chrpos(variant)
    variants = list(dict.fromkeys(variants))
    return variants


def variants_chrpos(chrpos, radius=0):
    """This function returns the dbSNP rsid for a single variant in chr:pos format

    Parameters:
        chrpos: variant in chr:pos format (string)

    Returns:
        data: variant rsid (string)

    """
    import ieugwaspy.query as query

    variantdata = query.api_query("variants/chrpos/{}".format(chrpos))
    result = variantdata[0][0]["_id"]
    return result
