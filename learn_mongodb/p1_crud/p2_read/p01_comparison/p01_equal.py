#!/usr/bin/env python
# -*- coding: utf-8 -*-

from learn_mongodb.db_test import col 
  

if __name__ == "__main__":
    data = [
        {"_id": "EN-01", "name": "John"}, 
        {"_id": "EN-02", "name": "Mike", "height": 186}, 
        {"_id": "EN-03", "name": "Kate", "height": 162},
    ]
    col.insert(data)


def equal():
    """{field: value} 相当于field的值等于value。等效于 ``{field: {"$eq": value}}``。
    """
    filters = {"name": "Mike"}
    results = list(col.find(filters))
    assert len(results) == 1
    assert results[0]["_id"] == "EN-02"


if __name__ == "__main__":
    #
    equal()


def equal_none():
    """{field: None} 相当于该项不存在, 等效于 ``{field: {"$exists": False}}``。
    """
    filters = {"height": None}
    results = list(col.find(filters))
    assert len(results) == 1
    assert results[0]["_id"] == "EN-01"
    
        
if __name__ == "__main__":
    #
    equal_none()