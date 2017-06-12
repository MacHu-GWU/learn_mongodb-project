#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


if __name__ == "__main__":
    data = [
        {"_id": "EN-01", "lastname": "Allen",
            "role": ["engineer", "product manager"]},
        {"_id": "EN-02", "lastname": "Neil", "role": ["executive"]},
        {"_id": "EN-03", "lastname": "Shin",
            "role": ["accounting", "finance"]},
    ]
    col.insert(data)


@run_if_is_main(__name__)
def not_in_for_non_array_field():
    """对于non array field, 只要该项的值在$nin中出现, 即算不满足匹配条件。
    """
    filters = {"lastname": {"$nin": ["Neil", "Shin"]}}
    assert [doc["_id"] for doc in col.find(filters)] == ["EN-01",]

not_in_for_non_array_field()


@run_if_is_main(__name__)
def not_in_for_array_field():
    """对于array field, 只要任何一个该array中的值在$nin中的元素中出现, 即算不满足
    匹配条件。
    """
    filters = {"role": {"$nin": ["executive", "finance"]}}
    assert [doc["_id"] for doc in col.find(filters)] == ["EN-01", ]

not_in_for_array_field()
