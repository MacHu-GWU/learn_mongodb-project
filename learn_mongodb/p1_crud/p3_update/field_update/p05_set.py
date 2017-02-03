#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$set`` 操作符在field update中的功能是: 修改某项的值。

ref: https://docs.mongodb.com/manual/reference/operator/update/set/
"""

import pytest
from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


@run_if_is_main(__name__)
def set_example():
    _id = 1
    col.insert({"_id": _id, "value": 0})
    col.update({"_id": _id}, {"$set": {"value": 1}})
    doc = col.find_one({"_id": _id})
    assert doc["value"] == 1

    # _id是不能被set的
    with pytest.raises(Exception):
        col.update({"_id": _id}, {"$set": {"_id": 2}})

set_example()
