#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$push`` 操作符在array update中的功能是: append单个元素到列表。有多个modifiers
能限定push的行为

ref: https://docs.mongodb.com/manual/reference/operator/update/push/
"""

from learn_mongodb.db_test import col


def push_example():
    _id = 1
    col.insert({"_id": _id, "items": [1, 2, 3]})
    col.update({"_id": _id}, {"$push": {"items": 9}})
    doc = col.find_one({"_id": _id})
    assert doc["items"] == [1, 2, 3, 9]
    

def position_example():
    """插入多个元素到指定位置, 必须和$each配合使用。
    
    ref: https://docs.mongodb.com/manual/reference/operator/update/position/
    """     
    _id = 2
    col.insert({"_id": _id, "items": [1, 2, 3]})
    col.update({"_id": _id}, {"$push": {"items": {"$each": [4, 5], "$position": 2}}})
    doc = col.find_one({"_id": _id})
    assert doc["items"] == [1, 2, 4, 5, 3]
    

def sort_example():
    """对列表进行排序, 必须和$each配合使用。
    
    ref: https://docs.mongodb.com/manual/reference/operator/update/sort/
    """
    from collections import OrderedDict
    
    _id = 3
    col.insert({
        "_id": _id, 
        "quizzes": [
            {"week": 1, "score": 10},
            {"week": 2, "score": 8},
            {"week": 3, "score": 5},
            {"week": 4, "score": 6},
        ],
    })
    col.update(
        {"_id": _id}, 
        {
            "$push": {
                "quizzes": {"$each": [], "$sort": {"score": 1}}
            },
        },
    )
    doc = col.find_one({"_id": _id})
    assert [d["week"] for d in doc["quizzes"]] == [3, 4, 2, 1]
    
    # Sort也支持同时对多个项进行复合排序, 但是要注意使用OrderedDict。
    _id = 4
    col.insert({
        "_id": _id, 
        "table": [
            {"col_1": 2, "col_2": 7},
            {"col_1": 1, "col_2": 9},
            {"col_1": 1, "col_2": 4},
            {"col_1": 3, "col_2": 4},
        ],
    })
    col.update(
        {"_id": _id}, 
        {
            "$push": {
                "table": {
                    "$each": [],
                    # 在复合排序中, 由于Python中的dict是无顺序的, 所以下面的
                    # 语法不能保证是先排序col1再排序col2。而使用OrderedDict就
                    # 没有这个问题。
                    # "$sort": {"col_1": 1, "col_2": 1},
                    "$sort": OrderedDict([("col_1", 1), ("col_2", 1)]),
                },
            },
        },
    )
    doc = col.find_one({"_id": _id})
    assert [d["col_1"] for d in doc["table"]] == [1, 1, 2, 3]
    assert [d["col_2"] for d in doc["table"]] == [4, 9, 7, 4]
    

def slice_example():
    """对列表进行切片。
    
    注: 在update中, slice不支持from, to形式的切片操作, 形如: {"$slice": [1, 3]}
    但是在find中是支持的, 这叫slice projection。所以我们需要进行update时无法
    执行原子的 $slice from to 切片update。 
    
    ref: https://docs.mongodb.com/manual/reference/operator/update/slice/
    """
    _id = 5
    col.insert({"_id": _id, "items": [1, 2, 3]})
    col.update({"_id": _id}, {"$push": {"items": {"$each": [4, 5], "$slice": 2}}})
    doc = col.find_one({"_id": _id})
    assert doc["items"] == [1, 2]
    
    _id = 6
    col.insert({"_id": _id, "items": [1, 2, 3]})
    col.update({"_id": _id}, {"$push": {"items": {"$each": [4, 5], "$slice": -2}}})
    doc = col.find_one({"_id": _id})
    assert doc["items"] == [4, 5]
    
    _id = 7
    col.insert({"_id": _id, "items": [1, 2, 3]})
    col.update({"_id": _id}, {"$push": {"items": {"$each": [4, 5], "$slice": 0}}})
    doc = col.find_one({"_id": _id})
    assert doc["items"] == []
    
    

if __name__ == "__main__":
    push_example()
    position_example()
    sort_example()
    slice_example()