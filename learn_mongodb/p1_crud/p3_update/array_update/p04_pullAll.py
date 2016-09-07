#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$pullAll`` 操作符在array update中的功能是: 删除array中值与指定的列表中的值相等
的元素。请注意, ``$pullAll`` 只能够直接匹配具体的数值, 而不能进行更多的比较。如果
想要删除所有满足一定条件的元素, 请用 ``$pull``。

ref: https://docs.mongodb.com/manual/reference/operator/update/pullAll/
"""

from learn_mongodb.db_test import col


def pull_all_example():
    _id = 1
    col.insert({"_id": _id, "scores": [ 0, 2, 5, 5, 1, 0 ]})
    col.update({"_id": _id}, {"$pullAll": {"scores": [0, 5]}})
    assert col.find_one({"_id": _id})["scores"] == [2, 1]


def pull_all_non_generic_item():
    """pull all可以匹配复杂, 嵌套的数据结构。
    """
    _id = 2
    data = {
        "_id": _id,
        "user": [
            {"name": "Jack"}, 
            {"name": "Tom"}, 
            {"name": "Mike"},
        ],
    }
    col.insert(data)
    col.update({"_id": _id}, {"$pullAll": {"user": [{"name": "Jack"}, {"name": "Mike"}]}})
    doc = col.find_one({"_id": _id})
    assert doc["user"] == [{"name": "Tom"},] 


if __name__ == "__main__":
    pull_all_example()
    pull_all_non_generic_item()