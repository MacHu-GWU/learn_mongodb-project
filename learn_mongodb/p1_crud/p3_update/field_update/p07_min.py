#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$min`` 操作符在field update中的功能是: 当指定值比某项目前的值小时, 执行update。

ref: https://docs.mongodb.com/manual/reference/operator/update/min/
"""

from learn_mongodb.db_test import col


def min_example():
    _id = 1
    col.insert({"_id": _id, "value": 0})
    
    col.update({"_id": _id}, {"$min": {"value": 0}}) # do nothing
    doc = col.find_one({"_id": _id})
    assert doc["value"] == 0
    
    col.update({"_id": _id}, {"$min": {"value": 1}}) # do nothing
    doc = col.find_one({"_id": _id})
    assert doc["value"] == 0
    
    col.update({"_id": _id}, {"$min": {"value": -1}}) # update to -1
    doc = col.find_one({"_id": _id})
    assert doc["value"] == -1


if __name__ == "__main__":
    #
    min_example()
