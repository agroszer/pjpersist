##############################################################################
#
# Copyright (c) 2011 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""PyMongo Patches"""

def lazy_hash(self):
    """Get a hash value for this :class:`DBRef`.

    .. versionadded:: 1.1
    """
    if self.__hash is None:
        self.__hash = self.orig_hash()
    return self.__hash

def patch():
    # ObjectId should get patched too, but it is hard, since it uses slots
    # *and* rquires the original object reference to be around (otherwise it
    # creates BSON encoding errors.
    import bson.dbref
    bson.dbref.DBRef.__hash = None
    bson.dbref.DBRef.orig_hash = bson.dbref.DBRef.__hash__
    bson.dbref.DBRef.__hash__ = lazy_hash
