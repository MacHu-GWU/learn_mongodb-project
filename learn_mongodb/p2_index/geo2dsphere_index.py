#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Mongodb支持3种查询模式:

1. 找出距离一个点的距离在x, y之间的所有点, 按照从近到远排列。
2. 找出在一个多边形内的所有的点。
3. 找出一个多边形和另一个多边形的交集部分。

本例中只给出了第一种查询模式的例子。

ref:

- https://docs.mongodb.com/manual/core/2dsphere/
"""

import random

from haversine import haversine
from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


def assert_increasing(array):
    for i, j in zip(array[1:], array[:-1]):
        assert (i - j) >= 0


if __name__ == "__main__":
    import pymongo

    n = 1000
    data = list()

    col.create_index([("loc", pymongo.GEOSPHERE)])
    LAT, LNG = 39.074373, -77.142901
    for i in range(n):
        lat = LAT + random.choice([1, -1]) * random.random() * 0.5
        lng = LNG + random.choice([1, -1]) * random.random() * 0.5
        # Please always use GEO Json format instead of simple [lng, lat] format
        # Use [Longitude, Latitude]! [lat, lng] is wrong
        doc = {"_id": i, "loc": {"type": "Point", "coordinates": [lng, lat]}}
        data.append(doc)

    col.insert(data)


@run_if_is_main(__name__)
def find_near():
    """Find doc near point from nearest to farest. Usually have limit() clause.

    Order by distance from nearest to farest by default.
    """
    # This is how you construct a filter
    filters = {
        "loc": {
            "$nearSphere": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [LNG, LAT],
                },
                "$maxDistance": 5 * 1000, # max distance in meter
            }
        }
    }

    array = list()
    for doc in col.find(filters).limit(5):
        lng, lat = doc["loc"]["coordinates"][0], doc["loc"]["coordinates"][1]
        dist = haversine((lat, lng), (LAT, LNG), miles=False)
        assert dist <= 5.0
        array.append(dist)

    assert_increasing(array)

find_near()