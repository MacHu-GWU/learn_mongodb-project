#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$`` 操作符用在array update中的含义是: 将array中第一个(仅仅是第一个)符合条件的
value进行update。例如::

    db.collection.update(
       {<array>: value ... },
       {<update operator>: {"<array>.$" : value } }
    )

ref: https://docs.mongodb.com/manual/reference/operator/update/positional/#update
"""

from learn_mongodb.db_test import col


def update_values_in_an_array():
    """如果更新的对象是array field里的值。
    """
    col.insert([
        {"_id": 1, "grades": [80, 85, 90, 80]},
        {"_id": 2, "grades": [88, 90, 92]},
        {"_id": 3, "grades": [85, 100, 90]},
    ])
    col.update({"_id": 1, "grades": 80}, {"$set": {"grades.$": 82}})
    doc = col.find_one({"_id": 1})
    assert doc["grades"] == [82, 85, 90, 80]  # The second 80 is not updated


def update_documents_in_an_array():
    """如果更新对象是doc array中的某个field。
    """
    _id = 4
    col.insert({
        "_id": _id,
        "grades": [
            {"grade": 80, "mean": 75, "std": 8},
            {"grade": 85, "mean": 90, "std": 5},
            {"grade": 90, "mean": 85, "std": 3},
            {"grade": 85, "mean": 81, "std": 9},
        ]
    })
    col.update(
        {"_id": _id, "grades.grade": 85},
        {"$set": {"grades.$.std": 6}},
    )
    doc = col.find_one({"_id": _id})
    assert doc["grades"][1]["std"] == 6
    # The fourth doc (second match) is not updated
    assert doc["grades"][3]["std"] == 9


def update_embedded_documents_using_multiple_field_matches():
    """当query有关多个field时, 使用$elemMatch
    """
    _id = 5
    col.insert({
        "_id": _id,
        "grades": [
            {"grade": 80, "mean": 75, "std": 8},
            {"grade": 85, "mean": 90, "std": 5},
            {"grade": 90, "mean": 85, "std": 3},
            {"grade": 85, "mean": 81, "std": 9},
        ]
    })
    col.update(
        {
            "_id": _id,
            "grades": {"$elemMatch": {"grade": {"$lte": 90}, "mean": {"$gt": 80}}},
        },
        {"$set": {"grades.$.std": 6}},
    )
    doc = col.find_one({"_id": _id})
    assert doc["grades"][1]["std"] == 6
    # The fourth doc (second match) is not updated
    assert doc["grades"][3]["std"] == 9


if __name__ == "__main__":
    update_values_in_an_array()
    update_documents_in_an_array()
    update_embedded_documents_using_multiple_field_matches()
