"""The ieugwaspy module provides a convenient Python wrapper for the IEU OpenGWAS database API. As far as possible the functionality in this module replicates functionality in the ieugwasr R package
"""
from ieugwaspy.config import env, _load_env
from ieugwaspy.api import *
from ieugwaspy.query import *
from ieugwaspy.variants import *

_load_env()
