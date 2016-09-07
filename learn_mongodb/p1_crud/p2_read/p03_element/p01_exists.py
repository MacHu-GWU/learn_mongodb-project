#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref: https://docs.mongodb.com/manual/reference/operator/query/exists/
"""

from learn_mongodb.db_test import col


def exists_example():
    """
    
    ::
    
        {"field": {"$exists": True}} 等效于 {"field": {"$ne": None}}
        {"field": {"$exists": False}} 等效于 {"field": None} 
    """
    col.insert({"_id": 1, "value": 0})
    assert col.find_one({"value": {"$exists": True}})["_id"] == 1
    assert col.find_one({"value": {"$ne": None}})["_id"] == 1
    
    assert col.find_one({"name": {"$exists": False}})["_id"] == 1
    assert col.find_one({"name": None})["_id"] == 1

    
if __name__ == "__main__":
    #
    exists_example()