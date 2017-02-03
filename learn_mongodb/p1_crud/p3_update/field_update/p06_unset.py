#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$unset`` 操作符在field update中的功能是: 删除某项。

ref: https://docs.mongodb.com/manual/reference/operator/update/set/
"""

from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


@run_if_is_main(__name__)
def unset_example():
    _id = 1
    col.insert({"_id": _id, "value": 0})
    col.update({"_id": _id}, {"$unset": {"value": True}})  # True可以替换为任何东西
    doc = col.find_one({"_id": _id})
    assert "value" not in doc

unset_example()
