#
# This file is part of Bluepass. Bluepass is Copyright (c) 2012-2014
# Geert Jansen.
#
# Bluepass is free software available under the GNU General Public License,
# version 3. See the file LICENSE distributed with this file for the exact
# licensing terms.

import os
import time
import random
import hashlib
import uuid
import string
import hmac as hmaclib
import math

from bluepass import logging, base64
from bluepass._openssl import *

__all__ = []

_pbkdf2_speed = {}

def measure_pbkdf2_speed(prf='hmac-sha1'):
    """Measure the speed of PBKDF2 on this system."""
    salt = password = '0123456789abcdef'
    length = 1; count = 1000
    log = logging.get_logger()
    log.debug('starting PBKDF2 speed measurement')
    start = time.time()
    while True:
        startrun = time.time()
        pbkdf2(password, salt, count, length, prf)
        endrun = time.time()
        if endrun - startrun > 0.2:
            break
        count *= 2
    end = time.time()
    speed = int(count / (endrun - startrun))
    log.debug('PBKDF2 speed is {:,} iterations/second', speed)
    log.debug('PBKDF2 speed measurement took {:.2f} secs', (end - start))
    return speed

def pbkdf2_speed(prf='hmac-sha1'):
    """Return the speed in rounds/second for generating a key
    with PBKDF2 of up to the hash length size of `prf`."""
    if prf not in _pbkdf2_speed:
        _pbkdf2_speed[prf] = measure_pbkdf2_speed(prf)
    return _pbkdf2_speed[prf]


def random_bytes(count):
    """Return *count* random bytes."""
    return os.urandom(count)

def random_int(below):
    """Return a random integer < *below*."""
    return random.randrange(0, below)

def random_uuid():
    """Return a type-4 random UUID."""
    return str(uuid.uuid4())

_cookie_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
_bits_per_cookie_char = math.log(len(_cookie_chars), 2)

def random_cookie(bits=128):
    """Return a cookie with at least *bits* of entropy."""
    nchars = int(bits/_bits_per_cookie_char + 1)
    return ''.join([random_element(_cookie_chars) for i in range(nchars)])

def random_element(elements):
    """Return a random element from *elements*."""
    return random.choice(elements)


def _get_hash(name):
    if not hasattr(hashlib, name):
        raise ValueError('no such hash function: %s' % name)
    return getattr(hashlib, name)

def hmac(key, message, hash='sha256'):
    """Return the HMAC of *message* under *key*."""
    md = _get_hash(hash)
    return hmaclib.new(key, message, md).digest()
