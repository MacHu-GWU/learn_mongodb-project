#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
本篇介绍了greater than ("$gt")的用法, 相应的 greater equal than ("$gte"), 
less than ("$lt"), less equal than ("$lte")的运作方式与之类似。
"""

from __future__ import print_function
from datetime import datetime
from learnMongo.emptydatabase import col

data = [
    {"name": "John", "height": 172, "dob": datetime(1983, 5, 23)}, 
    {"name": "Mike", "height": 177, "dob": datetime(1992, 11, 8)}, 
    {"name": "Kate", "height": 164, "dob": datetime(1978, 7, 19)},
    {"name": "Sara", "height": 161, "dob": datetime(1996, 2, 4)},
]
col.insert(data)

def gt():
    """{field: {"$gt": value}} 相当于field的值大于value。
    """
    filters = {"height": {"$gt": 170}}
    for doc in col.find(filters):
        print(doc)
    
# gt()

def gt_with_str():
    """对于字符串, 按照其Ascii编码的顺序排序。英文字母的ASCII编码顺序从小到大
    是从A-Z, a-z。
    """
    filters = {"name": {"$gt": "L"}}
    for doc in col.find(filters):
        print(doc)

# gt_with_str()

def gt_with_datetime():
    """对于时间, 越晚的时间就越大。
    """
    filters = {"dob": {"$gt": datetime(1990, 1, 1)}}
    for doc in col.find(filters):
        print(doc)
        
# gt_with_datetime()