#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$pull`` 操作符在array update中的功能是: 删除所有满足一定条件的元素。

ref: https://docs.mongodb.com/manual/reference/operator/update/pull/
"""

from learn_mongodb.db_test import col


def remove_all_items_that_equals_a_specified_value():
    col.insert([
        {
            "_id": 1,
            "fruits": ["apples", "pears", "oranges", "grapes", "bananas"],
            "vegetables": ["carrots", "celery", "squash", "carrots"],
        },
        {
            "_id": 2,
            "fruits": ["plums", "kiwis", "oranges", "bananas", "apples"],
            "vegetables": ["broccoli", "zucchini", "carrots", "onions"],
        }
    ])
    col.update(
        {},
        {"$pull": {"fruits": {"$in": ["apples", "oranges"]}, "vegetables": "carrots"}},
        multi=True,
    )
    
    doc1 = col.find_one({"_id": 1})
    assert doc1["fruits"] == ["pears", "grapes", "bananas"]
    assert doc1["vegetables"] == ["celery", "squash"]
    
    doc2 = col.find_one({"_id": 2})
    assert doc2["fruits"] == ["plums", "kiwis", "bananas"]
    assert doc2["vegetables"] == ["broccoli", "zucchini", "onions"]


def remove_all_items_that_match_a_specified_condition():
    _id = 3
    col.insert({"_id": _id, "votes": [3, 5, 6, 7, 7, 8]})
    col.update({"_id": _id}, {"$pull": {"votes": {"$gte": 6}}})
    assert col.find_one({"_id": _id})["votes"] == [3, 5]
    

def remove_items_from_an_array_of_documents():
    col.insert([
        {
            "_id": 4,
            "results": [
                {"item": "A", "score": 5},
                {"item": "B", "score": 8, "comment": "Strongly agree"},
           ],
        },
        {
           "_id": 5,
           "results": [
              {"item": "C", "score": 8, "comment": "Strongly agree"},
              {"item": "B", "score": 4 }
           ],
        },
    ])
    col.update(
        {},
        {"$pull": {"results": {"score": 8, "item": "B"}}},
        multi=True,
    )
    
    doc4 = col.find_one({"_id": 4})
    assert len(doc4["results"]) == 1
    
    doc5 = col.find_one({"_id": 5})
    assert len(doc5["results"]) == 2


def with_element_match():
    """Because $pull operator applies its query to each element as though it 
    were a top-level object, the expression did not require the use of 
    $elemMatch to specify the condition.
    
    详情请参考官方文档。
    """
    
    
if __name__ == "__main__":
    remove_all_items_that_equals_a_specified_value()
    remove_all_items_that_match_a_specified_condition()
    remove_items_from_an_array_of_documents()