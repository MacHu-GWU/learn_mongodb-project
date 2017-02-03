#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
$elemMatch的匹配模式是: 一个列表中的任意一个元素满足某个条件, 则视为匹配成功。

ref: https://docs.mongodb.com/manual/reference/operator/query/elemMatch/
"""

from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


@run_if_is_main(__name__)
def elemMatch_example():
    col.insert([
        {"_id": 1, "results": [ 82, 85, 88 ]},
        {"_id": 2, "results": [ 75, 88, 89 ]},
    ])
    filters = {"results": {"$elemMatch": {"$gte": 80, "$lt": 85 }}}
    assert list(col.find(filters)) == [{"_id": 1, "results": [ 82, 85, 88 ]}]
    
elemMatch_example()
    

@run_if_is_main(__name__)
def array_of_embedded_document():
    col.insert([
        {"_id": 3, "results": [ {"product": "abc", "score": 10}, {"product": "xyz", "score": 5} ]},
        {"_id": 4, "results": [ {"product": "abc", "score": 8}, {"product": "xyz", "score": 7} ]},
        {"_id": 5, "results": [ {"product": "abc", "score": 7}, {"product": "xyz", "score": 8} ]},
    ])
    filters = {"results": {"$elemMatch": {"product": "xyz", "score": {"$gte": 8 } } } }
    assert [doc["_id"] for doc in col.find(filters)] == [5, ]

array_of_embedded_document()