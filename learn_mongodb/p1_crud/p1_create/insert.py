#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MongoDB对于每一个客户端程序的所有插入和修改操作, 都会自动Commit成功之后, 才会
顺序执行下一条命令。
"""

import random
import pymongo
from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


@run_if_is_main(__name__)
def handle_integrity_error():
    for _ in range(20):
        try:
            col.insert({"_id": random.randint(1, 1 + 10)})
        except pymongo.errors.DuplicateKeyError:
            pass
        
handle_integrity_error()
    

@run_if_is_main(__name__)    
def batch_insert():
    col.remove({})
    data = [{"_id": i} for i in range(1, 1 + 10)]
    col.insert(data)
    assert col.find().count() == 10
    
batch_insert()