import logging
import os
from logging import config

# ENVIRONMENT VARIABLES

# LOGGER CONFIG
config.fileConfig("/app/logging.conf")
LOGGER = logging.getLogger("replace_me")
