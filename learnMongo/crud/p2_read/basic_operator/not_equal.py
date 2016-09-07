#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from learnMongo.emptydatabase import col

data = [
    {"_id": "EN-01", "name": "John"}, 
    {"_id": "EN-02", "name": "Mike", "height": 186}, 
    {"_id": "EN-03", "name": "Kate", "height": 162},
]
col.insert(data)

def not_equal():
    """{field: value} 相当于field的值等于value。等效于 ``{field: {"$eq": value}}``。
    """
    print("--- %s() output ---" % not_equal.__name__)
    filters = {"name": {"$ne": "Mike"}}
    for doc in col.find(filters):
        print(doc)
        
not_equal()

def not_equal_none():
    """{field: {"$ne": None}} 相当于该项存在, 但不管值是多少。此语法与
    ``{field: {"$exists": True}}`` 等效。
    """
    print("--- %s() output ---" % not_equal_none.__name__)    
    filters = {"height": {"$ne": None}}
    for doc in col.find(filters):
        print(doc)
        
not_equal_none()