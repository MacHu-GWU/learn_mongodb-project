#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
简而言之, compound index就是多项联立起来的索引。

注意: 不支持同时对两个array field做compound index。

ref:

- https://docs.mongodb.com/manual/core/index-compound/#index-type-compound
"""

import random

from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main
from sfm.timer import Timer
from sfm.rnd import rand_hexstr


@run_if_is_main(__name__)
def create_test_data():
    data = list()
    for class_id in range(50000):
        doc = {
            "_id": class_id,
            "int": random.randint(1, 1000),
            "str": rand_hexstr(16),
        }
        data.append(doc)
    col.insert(data)


create_test_data()


@run_if_is_main(__name__)
def test_performance():
    filters = {
        "int": {"$gte": 490, "$lte": 510},
        "str": {"$gte": "a", "$lte": "b"},
    }

    with Timer() as timer:
        cursor = col.find(filters)
        for doc in cursor:
            pass
    elapse1 = timer.elapsed

    col.create_index([("int", 1), ("str", 1)])

    with Timer() as timer:
        cursor = col.find(filters)
        for doc in cursor:
            pass
    elapse2 = timer.elapsed

    assert elapse1 > elapse2


test_performance()
