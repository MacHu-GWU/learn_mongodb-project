#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This feature was introduced in 3.4

``$count``: 

ref: https://docs.mongodb.com/manual/reference/operator/aggregation/count/
"""

from sfm.decorator import run_if_is_main
from learn_mongodb.db_test import col


@run_if_is_main(__name__)
def prepare_data():
    data = [
        {"_id": 1, "subject": "History", "score": 88},
        {"_id": 2, "subject": "History", "score": 92},
        {"_id": 3, "subject": "History", "score": 97},
        {"_id": 4, "subject": "History", "score": 71},
        {"_id": 5, "subject": "History", "score": 79},
        {"_id": 6, "subject": "History", "score": 83},
    ]
    col.insert(data)

prepare_data()


@run_if_is_main(__name__)
def example():
    pipeline = [
        {
            "$match": {
                "score": {
                    "$gt": 80,
                },
            },
        },
        {
            "$count": "passing student",
        },
    ]

    doc = list(col.aggregate(pipeline))[0]
    assert doc["passing student"] == 4

example()
