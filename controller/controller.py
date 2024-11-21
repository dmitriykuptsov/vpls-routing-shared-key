#!/usr/bin/python3

# Copyright (C) 2024 strangebit
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = "Dmitriy Kuptsov"
__copyright__ = "Copyright 2024, strangebit"
__license__ = "GPL"
__version__ = "0.0.1b"
__maintainer__ = "Dmitriy Kuptsov"
__email__ = "dmitriy.kuptsov@strangebit.io"
__status__ = "development"

# Sleep
from time import sleep
# Configuration
from config import config
# HIP Server
import crypto_server
from hiplib.utils.misc import Utils
# Logging....
import logging
logger = logging.getLogger("controller")
# Hexidecimal utlis
from binascii import hexlify

cs = None

def completed_callback(cipher, hmac, cipher_key, hmac_key, src, dst):
    src_str = Utils.ipv4_bytes_to_string(src)
    dst_str = Utils.ipv4_bytes_to_string(dst)
    logging.debug("Completed HIP BEX between %s %s" %(src_str, dst_str))

def closed_callback(ihit, rhit, src, dst):
    logger.debug("HIP connection was closed...")

# Host Identity Protocol crypto server
# Performs BEX and derives the keys to secure 
# The dataplane
cs = crypto_server.CryptoServer(completed_callback, closed_callback)

while True:
    logger.debug("Periodic task....")
    sleep(10)