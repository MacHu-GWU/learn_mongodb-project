#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$pushAll`` 操作符在array update中的功能是: append多个元素到列表的末端。

ref: https://docs.mongodb.com/manual/reference/operator/update/pushAll/
"""

from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


@run_if_is_main(__name__)
def push_all_example():
    _id = 1
    col.insert({"_id": _id, "items": [1, 2]})
    col.update({"_id": _id}, {"$pushAll": {"items": [1, 2, 3, 4]}})
    doc = col.find_one({"_id": _id})
    assert doc["items"] == [1, 2, 1, 2, 3, 4]
    
push_all_example()