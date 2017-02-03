#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main

if __name__ == "__main__":
    data = [
        {"_id": "EN-01", "name": "John"},
        {"_id": "EN-02", "name": "Mike", "height": 186},
        {"_id": "EN-03", "name": "Kate", "height": 162},
    ]
    col.insert(data)


@run_if_is_main(__name__)
def not_equal():
    """{field: value} 相当于field的值等于value。等效于 ``{field: {"$eq": value}}``。
    """
    filters = {"name": {"$ne": "Mike"}}
    assert [doc["_id"] for doc in col.find(filters)] == ["EN-01", "EN-03"]


not_equal()


@run_if_is_main(__name__)
def not_equal_none():
    """{field: {"$ne": None}} 相当于该项存在, 但不管值是多少。此语法与
    ``{field: {"$exists": True}}`` 等效。
    """
    filters = {"height": {"$ne": None}}
    if "mongomock" in str(col.__class__):
        assert [doc["_id"]
                for doc in col.find(filters)] == ["EN-01", "EN-02", "EN-03"]
    else:
        assert [doc["_id"] for doc in col.find(filters)] == ["EN-02", "EN-03"]

not_equal_none()
