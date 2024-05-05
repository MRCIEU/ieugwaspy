"""API management
"""
import ieugwaspy.config as config
import webbrowser

from .query import status


def select_api(key="public"):
    """Select API base URL (no return value)

    Args:
        key: the short name for the required API base url

    Returns:
        data: JSON object as returned by API

    """
    if key in config.urls.keys():
        config.env["base_url"] = config.urls[key]
        print("API server is now: " + config.env["base_url"])
        return status()
    else:
        print("Please select one from the following: \n" + "\n".join([k + " - " + v for k, v in config.urls.items()]))


def get_jwt():
    """Obtain a token (JWT) and save it locally
    """
    webbrowser.open(config.url_obtain_jwt)
    config.env["jwt"] = input("Paste your token (JWT) like ey****.******.******:\n")
    config._save_env()
