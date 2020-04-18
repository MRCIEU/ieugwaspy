"""This defines constants ieugwaspy

Parameters:
    option: API url selected
    urls: API urls available
    api_token_url: URL for API OAuth
    api_token: API token (default is NULL)
"""
option = {"mrbaseapi": "http://gwasapi.mrcieu.ac.uk/"}
urls = {
    "test": "http://ieu-db-interface.epi.bris.ac.uk:8084/",
    "prod": "http://gwas-api.mrcieu.ac.uk/",
    "dev": "http://localhost:8019/",
}
api_token_url = "https://accounts.google.com/o/oauth2/auth?client_id=906514199468-m9thhcept50gu26ng494376iipt125d6.apps.googleusercontent.com&redirect_uri=urn:ietf:wg:oauth:2.0:oob&scope=https://www.googleapis.com/auth/userinfo.email&response_type=code"
api_token = "NULL"
