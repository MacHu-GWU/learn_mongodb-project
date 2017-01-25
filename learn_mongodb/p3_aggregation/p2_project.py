#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$project``: 是指将一种数据结构映射成另一种数据结构的转换过程。

ref: https://docs.mongodb.com/manual/reference/operator/aggregation/project/
"""

from sfm.decorator import run_if_is_main
from learn_mongodb.db_test import col


@run_if_is_main(__name__)
def prepare_data():
    data = [{
        "_id": 1,
        "title": "abc123",
        "isbn": "0001122223334",
        "author": {"last": "zzz", "first": "aaa"},
        "copies": 5,
    }]
    col.insert(data)

prepare_data()


@run_if_is_main(__name__)
def include_specific_fields_in_output_documents():
    """只输出title和author两个field。
    """
    pipeline = [
        {
            "$project": {
                "full_title": "$title",  # 将title的field name换成full_title
                "author": 1,
            },
        },
    ]
    doc = list(col.aggregate(pipeline))[0]
    assert set(doc.keys()) == {"_id", "full_title", "author"}

include_specific_fields_in_output_documents()


@run_if_is_main(__name__)
def exclude_id_field():
    """跟上例一样, 只不过抛弃掉_id项。
    """
    pipeline = [
        {
            "$project": {
                "_id": 0, "title": 1, "author": 1,
            },
        },
    ]
    doc = list(col.aggregate(pipeline))[0]
    assert set(doc.keys()) == {"title", "author"}

exclude_id_field()


@run_if_is_main(__name__)
def include_computed_fields():
    """对文档进行计算之后输出。本例中主要将isbn拆分为了几个子field。
    关于string aggregation operations, 请参考:
        http://docs.mongodb.org/manual/reference/operator/aggregation-string/
    """
    pipeline = [
        {
            "$project": {
                "title": 1,
                "isbn": {
                    "prefix": {"$substr": ["$isbn", 0, 3]},
                    "group": {"$substr": ["$isbn", 3, 2]},
                    "publisher": {"$substr": ["$isbn", 5, 4]},
                    "title": {"$substr": ["$isbn", 9, 3]},
                    "checkDigit": {"$substr": ["$isbn", 12, 1]}
                },
                "lastName": "$author.last",
                "copiesSold": "$copies",
            },
        },
    ]
    doc = list(col.aggregate(pipeline))[0]
    assert doc == {
        "_id": 1,
        "copiesSold": 5,
        "isbn": {
            "checkDigit": "4",
            "group": "11",
            "prefix": "000",
            "publisher": "2222",
            "title": "333"
        },
        "lastName": "zzz",
        "title": "abc123"
    }

include_computed_fields()
