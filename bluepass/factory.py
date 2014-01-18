#
# This file is part of Bluepass. Bluepass is Copyright (c) 2012-2014
# Geert Jansen.
#
# Bluepass is free software available under the GNU General Public License,
# version 3. See the file LICENSE distributed with this file for the exact
# licensing terms.

from __future__ import absolute_import, print_function

__all__ = ['instance', 'singleton']


def instance(cls):
    """Return the singleton instance of a type."""
    if not hasattr(cls, 'instance'):
        raise RuntimeError('Not yet instantiated.')
    return cls.instance

def singleton(cls, *args, **kwargs):
    """Create a singleton class instance."""
    if hasattr(cls, 'instance'):
        raise RuntimeError('Already instantiated.')
    cls.instance = cls(*args, **kwargs)
    return cls.instance
