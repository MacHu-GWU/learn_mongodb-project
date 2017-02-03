#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$group``

ref: https://docs.mongodb.com/manual/reference/operator/aggregation/group/
"""

import time
from learn_mongodb.db_test import col
from sfm.decorator import run_if_is_main


distinct_complexity = 10

@run_if_is_main(__name__)
def prepare_data():
    """测试数据为:

    doc = {"a": 0, "b": 0, "c": 0}, 
    a, b, c = 1 ~ 100, 一共1000,000条数据
    """
    if col.find().count() == distinct_complexity ** 3:
        return

    col.remove({})

    data = list()
    for i in range(distinct_complexity):
        for j in range(distinct_complexity):
            for k in range(distinct_complexity):
                data.append({"a": i, "b": j, "c": k})
    col.insert(data)

prepare_data()

#--- for distinct value ---


@run_if_is_main(__name__)
def distinct_on_one_field():
    """计算文档中的 "a" 项的所有不同的值。
    """

    result = list(col.find({}).distinct("a"))  # [0, 1, ..., 9]
    assert result == list(range(distinct_complexity))

distinct_on_one_field()


@run_if_is_main(__name__)
def distinct_on_multiple_field():
    """计算文档中a, b两项的组合的所有不同的值。
    """
    pipeline = [
        {
            "$group": {"_id": {"a": "$a", "b": "$b"}},
        },
    ]
    result = list()
    for doc in col.aggregate(pipeline):
        # doc = {"_id": {"a": 0, "b": 0}} ...
        result.append([doc["_id"]["a"], doc["_id"]["b"]])

    assert len(result) == distinct_complexity ** 2

distinct_on_multiple_field()


@run_if_is_main(__name__)
def count_distinct():
    """计算a, b不同的组合的个数。本例中用了3种方法实现, 其中method1最佳, 消耗
    的内存最小, 速度也几乎最快。
    """
    def method1():
        """使用group + count。
        """
        pipeline = [
            {
                "$group": {
                    "_id": {"_id": {"a": "$a", "b": "$b"}},
                },
            },
            {
                "$group": {"_id": None, "count": {"$sum": 1}},
            },
        ]
        doc = list(col.aggregate(pipeline))[0]
        assert doc["count"] == distinct_complexity ** 2

    def method2():
        """使用group和手动count。
        """
        pipeline = [
            {
                "$group": {
                    "_id": {"_id": {"a": "$a", "b": "$b"}},
                    "count": {"$sum": True},
                },
            },
        ]
        counter = 0
        for doc in col.aggregate(pipeline):
            counter += 1
        assert counter == distinct_complexity ** 2

    def method3():
        """遍历所有数据, 手动排重。
        """
        s = set()
        for doc in col.find({}, {"a": True, "b": True}):
            s.add("%s-%s" % (doc["a"], doc["b"]))
        assert len(s) == distinct_complexity ** 2

    st = time.clock()
    method1()
    elapse1 = time.clock() - st

    st = time.clock()
    method2()
    elapse2 = time.clock() - st

    st = time.clock()
    method3()
    elapse3 = time.clock() - st

    assert elapse1 < elapse3
    assert elapse2 < elapse3

count_distinct()


@run_if_is_main(__name__)
def occurence_of_a_b_combination():
    """计算每种a, b项的值的组合所出现的次数。
    """
    pipeline = [
        {
            "$group": {
                "_id": {"a": "$a", "b": "$b"},
                "count": {"$sum": 1},
            },
        },
    ]
    for doc in col.aggregate(pipeline):
        assert doc["count"] == 10

occurence_of_a_b_combination()
