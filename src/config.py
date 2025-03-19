import logging
import os
from logging import config

# ENVIRONMENT VARIABLES
JRNL_DIR = os.getenv("JRNL_DIR", "./examples/jrnl-dir/")

# LOGGER CONFIG
config.fileConfig("/app/logging.conf")
LOGGER = logging.getLogger("replace_me")
