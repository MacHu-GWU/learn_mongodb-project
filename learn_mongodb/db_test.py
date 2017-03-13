#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Watch out, in mongomock 3.7.0, if you drop collection, then documents are not 
OrderedDict anymore. After that, anything you insert will not follow the insert
order.

Recommend to use: https://github.com/MacHu-GWU/mongomock-sanhe.git
"""

USE_MONGOMOCK = False

if not USE_MONGOMOCK:
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
 
else:
    import mongomock
     
    client = mongomock.MongoClient()
    db = client.get_database("test") 
    col = db.get_collection("test_col")


col.drop()