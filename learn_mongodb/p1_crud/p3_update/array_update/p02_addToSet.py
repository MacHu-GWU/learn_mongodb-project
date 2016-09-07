#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$addToSet`` 的功能是将array field当成一个集合来看待(由于只涉及add, 所以集合中
已有多个相同值的元素是允许的)。

ref: https://docs.mongodb.com/manual/reference/operator/update/addToSet/
"""

from learn_mongodb.db_test import col


def add_to_a_not_existed_field():
    """如果field不存在, 则自动新建一个空列表。
    """
    _id = 1
    col.insert({"_id": _id, "item": "polarizing_filter"})
    col.update({"_id": _id}, {"$addToSet": {"tags": "electronics"}})
    assert col.find_one({"_id": _id})["tags"] == ["electronics", ]


def add_to_array():
    """添加单个元素到set array。
    """
    _id = 2
    col.insert({
        "_id": _id,
        "item": "polarizing_filter",
        "tags": ["electronics", "camera"],
    })
    col.update({"_id": _id}, {"$addToSet": {"tags": "accessories"}})
    assert col.find_one({"_id": _id})["tags"] == [
        "electronics", "camera", "accessories"]


def value_already_exists():
    """若添加的元素已经存在, 则不作任何变化。
    """
    _id = 3
    col.insert({
        "_id": _id,
        "item": "polarizing_filter",
        "tags": ["electronics", "camera"],
    })
    col.update({"_id": _id}, {"$addToSet": {"tags": "camera"}})
    assert col.find_one({"_id": _id})["tags"] == ["electronics", "camera"]


def each_modifier():
    """$each操作符允许一次添加多个元素。
    """
    _id = 4
    col.insert({
        "_id": _id,
        "item": "cable",
        "tags": ["electronics", "supplies"],
    })
    col.update(
        {"_id": _id},
        {"$addToSet": {
            "tags": {"$each": ["camera", "electronics", "accessories"]}}},
    )
    assert col.find_one({"_id": _id})["tags"] == [
        "electronics", "supplies", "camera", "accessories"]


if __name__ == "__main__":
    add_to_a_not_existed_field()
    add_to_array()
    value_already_exists()
    each_modifier()
