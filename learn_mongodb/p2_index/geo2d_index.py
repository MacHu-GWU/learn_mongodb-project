#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ref:

- https://docs.mongodb.com/manual/core/2d/
"""
import random

from bson.son import SON
from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


def find_dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def assert_increasing(array):
    for i, j in zip(array[1:], array[:-1]):
        assert (i - j) >= 0


if __name__ == "__main__":
    import pymongo

    n = 1000
    data = list()

    col.create_index([("loc", pymongo.GEO2D)])
    for i in range(n):
        doc = {
            "_id": i,
            "loc": [
                random.randint(1, 100),
                random.randint(1, 100),
            ],
        }
        data.append(doc)

    col.insert(data)

@run_if_is_main(__name__)
def find_near():
    """Find doc near point from nearest to farthest. Usually have limit() clause.

    Order by distance from nearest to farthest by default.
    """
    filters = {"loc": {"$near": [50, 50]}}
    array = list()
    for doc in col.find(filters).limit(5):
        dist = find_dist(doc["loc"][0], doc["loc"][1], 50, 50)
        array.append(dist)
    assert_increasing(array)


find_near()

@run_if_is_main(__name__)
def find_near_max_distance():
    """

    Order by distance from nearest to farthest by default.
    """
    filters = {"loc": SON([("$near", [50, 50]), ("$maxDistance", 10)])}
    array = list()
    for doc in col.find(filters):
        dist = find_dist(doc["loc"][0], doc["loc"][1], 50, 50)
        assert dist <= 10
        array.append(dist)
    assert_increasing(array)


find_near_max_distance()

@run_if_is_main(__name__)
def find_within_box():
    """There's no order.
    """
    filters = {"loc": {"$within": {"$box": [[40, 40], [60, 60]]}}}
    array = list()
    for doc in col.find(filters):
        x, y = doc["loc"][0], doc["loc"][1]
        assert 40 <= x <= 60
        assert 40 <= y <= 60
    assert_increasing(array)


find_within_box()

@run_if_is_main(__name__)
def find_within_center():
    """There's no order.
    """
    filters = {"loc": {"$within": {"$center": [[50, 50], 10]}}}
    array = list()
    for doc in col.find(filters):
        dist = find_dist(doc["loc"][0], doc["loc"][1], 50, 50)
        assert dist <= 10
    assert_increasing(array)


find_within_center()
