#!/usr/bin/env python
# -*- coding: utf-8 -*-

from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


if __name__ == "__main__":
    data = [
        {"_id": "EN-01", "name": "John"},
        {"_id": "EN-02", "name": "Mike", "height": 186},
        {"_id": "EN-03", "name": "Kate", "height": 162},
    ]
    col.insert(data)


@run_if_is_main(__name__)
def equal():
    """{field: value} 相当于field的值等于value。等效于 ``{field: {"$eq": value}}``。
    """
    filters = {"name": "Mike"}
    results = list(col.find(filters))
    assert len(results) == 1
    assert results[0]["_id"] == "EN-02"


equal()


@run_if_is_main(__name__)
def equal_none():
    """{field: None} 相当于该项不存在, 等效于 ``{field: {"$exists": False}}``。
    """
    filters = {"height": None}
    results = list(col.find(filters))
    assert len(results) == 1
    assert results[0]["_id"] == "EN-01"


equal_none()
