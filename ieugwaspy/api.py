import ieugwaspy.constants as cons
def toggle_api(url="prod"):
    '''Toggle API URL (no return value)

    Parameters:
        url: the short name for the required API url

    '''
    if url in cons.urls.keys():
        cons.option['mrbaseapi'] = cons.urls[url]
    else:
        print('A valid API was not selected. No change')
