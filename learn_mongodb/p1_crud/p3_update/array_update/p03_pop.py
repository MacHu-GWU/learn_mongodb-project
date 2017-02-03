#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$pop`` 操作符在array update中的功能是: 移除列表中的最后一个或第一个元素。(使用
1/-1标识符区分两者)

ref: https://docs.mongodb.com/manual/reference/operator/update/pop/
"""

from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


@run_if_is_main(__name__)
def remove_last_item():
    _id = 1
    col.insert({"_id": _id, "scores": [8, 9, 10]})
    col.update({"_id": _id}, {"$pop": {"scores": 1}})
    assert col.find_one({"_id": _id})["scores"] == [8, 9]

remove_last_item()


@run_if_is_main(__name__)
def remove_first_item():
    _id = 2
    col.insert({"_id": _id, "scores": [8, 9, 10]})
    col.update({"_id": _id}, {"$pop": {"scores": -1}})
    assert col.find_one({"_id": _id})["scores"] == [9, 10]

remove_first_item()


@run_if_is_main(__name__)
def pop_from_empty_array():
    """如果已经是空列表, 则没有影响。
    """
    _id = 3
    col.insert({"_id": _id, "scores": []})
    col.update({"_id": _id}, {"$pop": {"scores": 1}})
    assert col.find_one({"_id": _id})["scores"] == []

pop_from_empty_array()
