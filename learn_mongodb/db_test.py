#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

client = pymongo.MongoClient("localhost", 27017)

# Use Database
db = client.__getattr__("test")

# Connect to Collection
col = db.__getattr__("test_col")

"""
By default, you can create a single instance of MongoDB using attribute style.
Like: ``client.test``. But Python IDLE can not figure out the type of attribute.
The ``__getattr__(db_name)`` method explicitly returns a Database instance, so 
we can take grants from 'auto-complete feature' for all available method.
"""

col.drop()