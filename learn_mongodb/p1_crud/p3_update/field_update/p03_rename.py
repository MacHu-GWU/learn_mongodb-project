#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$rename`` 操作符在field update中的功能是: 修改field name。

注: 当rename一个不存在的field的时候, 会什么都不做。

ref: https://docs.mongodb.com/manual/reference/operator/update/rename/
"""

from learn_mongodb.db_test import col


def rename_example():
    """
    """
    _id = 1
    col.insert({"_id": _id, "value": 0})
    col.update({"_id": _id}, {"$rename": {"value": "count"}})
    doc = col.find_one({"_id": _id})
    assert "value" not in doc
    assert "count" in doc

    _id = 2
    col.insert({"_id": _id, "people": {"name": "Jack"}})
    col.update({"_id": _id}, {"$rename": {"people.name": "people.username"}})
    doc = col.find_one({"_id": _id})
    assert "name" not in doc["people"]
    assert "username" in doc["people"]


if __name__ == "__main__":
    #
    rename_example()
