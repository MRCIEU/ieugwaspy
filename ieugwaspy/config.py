"""Configurations of ieugwaspy

Args:
    env: all the active configurations
    urls: API base urls available
    url_obtain_jwt: URL for the webpage to obtain a JWT
"""
import json

__version__ = "1.0.5"

env = {
    "base_url": "https://api.opengwas.io/api/",
    "jwt": "",
    "test_mode_key": ""
}
urls = {
    "public": "https://api.opengwas.io/api/",
    "private": "http://ieu-db-interface.epi.bris.ac.uk:8082/api/",
    "dev": "http://localhost:8019/api/"
}
url_obtain_jwt = "https://api.opengwas.io/profile/"

allowance_reset_timestamp = 0


def _save_env():
    """Save env variables to .ieugwaspy.json

    """
    with open(".ieugwaspy.json", "w") as f:
        json.dump(env, f)
        print('\nEnv variables have been saved to .ieugwaspy.json\nPlease add this file to .gitignore and .dockerignore if necessary')


def _load_env():
    """Load env variables from .ieugwaspy.json

    """
    try:
        with open(".ieugwaspy.json", "r") as f:
            env_loaded = json.load(f)
            for k in env.keys():
                if k in env_loaded:
                    env[k] = env_loaded[k]
            print("Env variables have been loaded from .ieugwaspy.json as follows:\n", env)
    except Exception as e:
        print("The .ieugwaspy.json file does not yet exist: using default env variables.\n\nTo setup JWT authentication (which will create .ieugwas.json) please run ieugwaspy.get_jwt().")
