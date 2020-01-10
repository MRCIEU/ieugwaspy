import ieugwaspy.constants as cons
import ieugwaspy.variants as variants
import json, requests

def api_query(path, query="", access_token=cons.api_token):
    '''Query the API and return the data

    Parameters:
        path: the path component of the URL
        query: any query to go after the ?query component of the URL
        access_token: the OAuth access token

    Returns:
        data: json object as returned by API

    ''' # Still need to handle timeouts
    ntry = 0
    ntries = 3
    if query != "":
        url = '{}{}?query={}&access_token={}'.format(cons.option['mrbaseapi'],path,query,access_token)
    else:
        url = '{}{}?access_token={}'.format(cons.option['mrbaseapi'],path,access_token)
    print(url)
    response = requests.get(url)
    data = json.loads(response.text)
    return(data)

def api_status():
    '''Check API status

    Returns:
        data: API status 

    '''
    data = api_query('status')
    return(data)

def gwasinfo(id = "", access_token = cons.api_token):
    '''Return GWAS study meta-data

    Parameters:
        id: ID(s) of specific studies
        access_token: the OAuth access token

    Returns:
        data: json object as returned by API

    '''
    id = ",".join(id)
    if id != "":
        data = api_query('gwasinfo/{}'.format(id), access_token=access_token)
    else:
        data = api_query('gwasinfo/list', access_token=access_token)
    return(data)

def phewas(variantlist, pval = 1e-3, access_token = cons.api_token):
    '''Perform PheWAS of variant(s)

    Parameters:
        variants: list of variants
        pval: p-value threshold
        access_token: the OAuth access token

    Returns:
        data: json object as returned by API

    '''
    rsid = ",".join(variants.variants_to_rsid(variantlist))
    data = api_query('phewas/{}/{}'.format(rsid,pval), access_token=cons.api_token)
    return(data)

