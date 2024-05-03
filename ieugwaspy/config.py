"""Configurations of ieugwaspy

Args:
    env: all the active configurations
    urls: API base urls available
    url_obtain_jwt: URL for the webpage to obtain a JWT
"""
import json


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
        print("The .ieugwaspy.json file does not exist. Now using default env variables.")
