#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Upsert是update和insert的混合: 尝试Update, 如果文档不存在, 则Insert。
"""

from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


@run_if_is_main(__name__)
def example():
    """Wrong implement.
    """
    _id = 1
    col.insert({"_id": _id, "name": "Python"})
    
    col.update({"_id": _id}, {"$set": {"version": 3}}, upsert=True)
    
    doc = col.find_one({"_id": _id})
    assert doc["name"] == "Python"
    assert doc["version"] == 3
    
    
    _id = 2
    
    col.update({"_id": _id}, {"$set": {"version": 3}}, upsert=True)
    
    doc = col.find_one({"_id": _id})
    assert "name" not in doc
    assert doc["version"] == 3
    
example()