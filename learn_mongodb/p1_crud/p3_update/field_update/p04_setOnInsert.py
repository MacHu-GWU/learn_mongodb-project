#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$setOnInsert`` 操作符在field update中的功能是: 在upsert的时候, 如果发生的是
update, 则$setOnInsert无效; 如果发生的是insert, 则有效。

ref: https://docs.mongodb.com/manual/reference/operator/update/setOnInsert/
"""

from learn_mongodb.db_test import col


def setOnInsert_example():
    """
    """
    _id = 1
    col.update(
        {"_id": _id},
        {"$set": {"item": "apple"}, "$setOnInsert": {"defaultQty": 100}},
        upsert=True,
    )
    doc = col.find_one({"_id": _id})
    assert doc["item"] == "apple"
    assert doc["defaultQty"] == 100


if __name__ == "__main__":
    #
    setOnInsert_example()
