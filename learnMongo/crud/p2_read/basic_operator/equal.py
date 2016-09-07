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

def equal():
    """{field: value} 相当于field的值等于value。等效于 ``{field: {"$eq": value}}``。
    """
    print("--- %s() output ---" % equal.__name__)
    filters = {"name": "Mike"}
    for doc in col.find(filters):
        print(doc)
        
equal()

def equal_none():
    """{field: None} 相当于该项不存在, 等效于 ``{field: {"$exists": False}}``。
    """
    print("--- %s() output ---" % equal_none.__name__)
    filters = {"height": None}
    for doc in col.find(filters):
        print(doc)
        
equal_none()