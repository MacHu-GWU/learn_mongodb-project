#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$inc`` 操作符在field update中的功能是: 原子自增。减法操作也用这个。

ref: https://docs.mongodb.com/manual/reference/operator/update/inc/
"""

from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


@run_if_is_main(__name__)
def inc_example():
    _id = 1
    col.insert({"_id": _id, "value": 0})
    col.update({"_id": _id}, {"$inc": {"value": 1}})
    doc = col.find_one({"_id": _id})
    assert doc["value"] == 1

    _id = 2
    col.insert({"_id": _id, "value": 0})
    col.update({"_id": _id}, {"$inc": {"value": -1}})
    doc = col.find_one({"_id": _id})
    assert doc["value"] == -1

inc_example()
