#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
求摸运算符

Ref: https://docs.mongodb.com/manual/reference/operator/query/mod/
"""

from learn_mongodb.db_test import col


def mod_example():
    """
    """
    col.insert({"_id": 1, "value": 98})
    assert col.find_one({"value": {"$mod": [4, 2]}})["_id"] == 1

    
if __name__ == "__main__":
    #
    mod_example()