#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref:

- https://docs.mongodb.com/manual/core/index-multikey/
"""

import random
from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main
from sfm.timer import Timer


@run_if_is_main(__name__)
def create_test_data():
    data = list()
    for class_id in range(50000):
        doc = {
            "_id": class_id,
            "scores": [random.randint(50, 95) for _ in
                       range(random.randint(10, 30))]
        }
        data.append(doc)
    col.insert(data)


create_test_data()


@run_if_is_main(__name__)
def test_performance():
    filters = {"scores": 95}

    with Timer() as timer:
        cursor = col.find(filters)
        for doc in cursor:
            pass
    elapse1 = timer.elapsed

    col.create_index([("scores", 1)])

    with Timer() as timer:
        cursor = col.find(filters)
        for doc in cursor:
            pass
    elapse2 = timer.elapsed

    assert elapse1 > elapse2


test_performance()
