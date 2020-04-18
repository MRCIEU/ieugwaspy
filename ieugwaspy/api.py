"""API management
"""
import ieugwaspy.constants as cons
import webbrowser, os


def toggle_api(url="prod"):
    """Toggle API URL (no return value)

    Parameters:
        url: the short name for the required API url

    """
    if url in cons.urls.keys():
        cons.option["mrbaseapi"] = cons.urls[url]


def get_api_token():
    webbrowser.open(cons.api_token_url)
    return input("Paste API token: ")
