import ieugwaspy.query as query

def variants_to_rsid(variants):
    for pos, variant in enumerate(variants):
        if variant.find(":") > 0:
            variants[pos] = variants_chrpos(variant)
    variants = list(dict.fromkeys(variants))
    return(variants)

def variants_chrpos(chrpos, radius=0):
    variantdata = query.api_query('variants/chrpos/{}'.format(chrpos))
    result = variantdata[0][0]["_id"]
    return(result)

