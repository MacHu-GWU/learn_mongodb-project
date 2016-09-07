#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from learnMongo.emptydatabase import col

data = [
    {"_id": "EN-01", "lastname": "Allen", "role": ["engineer", "product manager"]}, 
    {"_id": "EN-02", "lastname": "Neil", "role": ["executive"]}, 
    {"_id": "EN-03", "lastname": "Shin", "role": ["accounting", "finance"]},
]
col.insert(data)

def in_for_non_array_field():
    """对于non array field, 只要该项的值在$in中出现, 即算满足匹配条件。
    """
    print("--- %s() output ---" % in_for_non_array_field.__name__)
    filters = {"lastname": {"$in": ["Neil", "Shin"]}}
    for doc in col.find(filters):
        print(doc)
        
in_for_non_array_field()

def in_for_array_field():
    """对于array field, 只要任何一个该array中的值在$in中的元素中出现, 即算满足
    匹配条件。
    """
    print("--- %s() output ---" % in_for_array_field.__name__)
    filters = {"role": {"$in": ["executive", "finance"]}}
    for doc in col.find(filters):
        print(doc)
        
in_for_array_field()