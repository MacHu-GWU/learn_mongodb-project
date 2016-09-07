#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MongoDB对于每一个客户端程序的所有插入和修改操作, 都会自动Commit成功之后, 才会
顺序执行下一条命令。
"""

import random
import pymongo
from learn_mongodb.db_test import col


def handle_integrity_error():
    for _ in range(20):
        try:
            col.insert({"_id": random.randint(1, 1 + 10)})
        except pymongo.errors.DuplicateKeyError:
            pass
        

if __name__ == "__main__":
    #
    handle_integrity_error()
    
    
def batch_insert():
    col.remove({})
    data = [{"_id": i} for i in range(1, 1 + 10)]
    col.insert(data)
    assert col.find().count() == 10
    

if __name__ == "__main__":
    #
    batch_insert()