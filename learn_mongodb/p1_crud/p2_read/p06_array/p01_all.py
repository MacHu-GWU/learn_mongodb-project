#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$all`` 查询符匹配某一项中所有的元素包含了全部所指定的元素。

Ref: https://docs.mongodb.com/manual/reference/operator/query/all/

性能方面, 慎用! 因为 ``$all`` 无论如何都需要扫描所有文档, 即使对array field做了
index。

Ref: https://docs.mongodb.com/manual/reference/operator/query/all/#performance
"""

from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


@run_if_is_main(__name__)
def equivalent_to_and():
    col.insert({"_id": 1, "tags": ["A", "B"]})
    col.insert({"_id": 2, "tags": ["B", "C"]})
    col.insert({"_id": 3, "tags": ["C", "A"]})
    col.insert({"_id": 4, "tags": ["A", "B", "C"]})

    results = col.find({"tags": {"$all": ["A", "B"]}})
    assert [doc["_id"] for doc in results] == [1, 4]

    results = col.find({"$and": [{"tags": "A"}, {"tags": "B"}]})
    assert [doc["_id"] for doc in results] == [1, 4]

    # 对于array field, 可以直接用 {field: value} 的语法等效于 {field: {$all: [value, ]}}
    results = col.find({"tags": "A"})
    assert [doc["_id"] for doc in results] == [1, 3, 4]

equivalent_to_and()


@run_if_is_main(__name__)
def all_element_match():
    col.insert([
        {
            "_id": 5,
            "code": "xyz",
            "tags": ["school", "book", "bag", "headphone", "appliance"],
            "qty": [
                {"size": "S", "num": 10, "color": "blue"},
                {"size": "M", "num": 45, "color": "blue"},
                {"size": "L", "num": 100, "color": "green"},
            ],
        },
        {
            "_id": 6,
            "code": "abc",
            "tags": ["appliance", "school", "book"],
            "qty": [
                {"size": "6", "num": 100, "color": "green"},
                {"size": "6", "num": 50, "color": "blue"},
                {"size": "8", "num": 100, "color": "brown"},
            ],
        },
        {
            "_id": 7,
            "code": "efg",
            "tags": ["school", "book"],
            "qty": [
                {"size": "S", "num": 10, "color": "blue"},
                {"size": "M", "num": 100, "color": "blue"},
                {"size": "L", "num": 100, "color": "green"},
            ],
        },
        {
            "_id": 8,
            "code": "ijk",
            "tags": ["electronics", "school"],
            "qty": [
                {"size": "M", "num": 100, "color": "green"},
            ],
        },
    ])
    filters = {
        "qty": {
            "$all": [
                {"$elemMatch": {"size": "M", "num": {"$gt": 50}}},
                {"$elemMatch": {"num": 100, "color": "green"}},
            ],
        },
    }
    results = col.find(filters)
    assert [doc["_id"] for doc in results] == [7, 8]

all_element_match()
