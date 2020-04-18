"""The ieugwaspy module provides a convenient Python wrapper for the IEU GWAS database API. As far as possible the functionality in this module replicates functionality in the ieugwasr R package
"""
import os
from ieugwaspy.constants import option, urls
from ieugwaspy.api import *
from ieugwaspy.query import *
from ieugwaspy.variants import *
