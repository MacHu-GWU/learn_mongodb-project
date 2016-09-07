#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pymongo

client = pymongo.MongoClient()
db = client.__getattr__("test")
col = db.__getattr__("test_col")

def drop_all():
    """drop all collection in our test database.
    """
    for collection in [col, ]:
        col.drop()
