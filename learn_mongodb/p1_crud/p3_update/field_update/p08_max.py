#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$max`` 操作符在field update中的功能是: 当指定值比某项目前的值大时, 执行update。

ref: https://docs.mongodb.com/manual/reference/operator/update/max/
"""

from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


@run_if_is_main(__name__)
def max_example():
    _id = 1
    col.insert({"_id": _id, "value": 0})
    
    col.update({"_id": _id}, {"$max": {"value": 0}}) # do nothing
    doc = col.find_one({"_id": _id})
    assert doc["value"] == 0
    
    col.update({"_id": _id}, {"$max": {"value": -1}}) # do nothing
    doc = col.find_one({"_id": _id})
    assert doc["value"] == 0
    
    col.update({"_id": _id}, {"$max": {"value": 1}}) # update to 1
    doc = col.find_one({"_id": _id})
    assert doc["value"] == 1

max_example()
