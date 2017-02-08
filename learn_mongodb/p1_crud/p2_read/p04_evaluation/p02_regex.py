#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
正则运算符

Ref: https://docs.mongodb.com/manual/reference/operator/query/regex/
"""

import re
from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


@run_if_is_main(__name__)
def regex_example():
    """
    """
    data = [
        {"_id": "Alabama"},
        {"_id": "California"},
        {"_id": "Delaware"},
        {"_id": "Florida"},
        {"_id": "Illinois"},
        {"_id": "Kansas"},
        {"_id": "New York"},
        {"_id": "Oregon"},
        {"_id": "Pennsylvania"},
        {"_id": "Texas"},
        {"_id": "Virginia"},
        {"_id": "Washington"},
    ]
    col.insert(data)
    
    # start with
    filters = {"_id": {"$regex": re.compile("^%s" % "a", re.IGNORECASE)}}
    result = [doc["_id"] for doc in col.find(filters)] 
    assert result == ["Alabama"]
    
    # end with
    filters = {"_id": {"$regex": re.compile("%s$" % "ia", re.IGNORECASE)}}
    result = [doc["_id"] for doc in col.find(filters)] 
    assert result == ["California", "Pennsylvania", "Virginia"]
    
    # contain
    filters = {"_id": {"$regex": re.compile("%s" % "or", re.IGNORECASE)}}
    result = [doc["_id"] for doc in col.find(filters)] 
    assert result == ["California", "Florida", "New York", "Oregon"]

regex_example()