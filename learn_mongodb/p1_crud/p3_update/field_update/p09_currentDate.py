#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$currentDate`` 操作符在field update中的功能是: 将当前

ref: https://docs.mongodb.com/manual/reference/operator/update/currentDate/
"""

from datetime import datetime
import bson
from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


@run_if_is_main(__name__)
def currentDate_example():
    _id = 1
    col.insert({"_id": _id, "status": "a", "lastModified": datetime(2016, 1, 1)})
    
    col.update(
        {"_id": _id},
        {
            "$currentDate": {
                "lastModified": True,
                "cancellation.date": {"$type": "timestamp"}
            },
            "$set": {
                "status": "D",
                "cancellation.reason": "user request",
            },
        },
    )
    doc = col.find_one({"_id": _id})
    assert doc["lastModified"] != datetime(2016, 1, 1)
    assert isinstance(doc["cancellation"]["date"], bson.timestamp.Timestamp)
    
currentDate_example()
