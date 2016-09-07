#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
与Distinct有关的一切操作。
"""

import time
from learnMongo import test_col


def prepare_data():
    """测试数据为:
    
    doc = {"a": 0, "b": 0, "c": 0}, 
    a, b, c = 1 ~ 100, 一共1000,000条数据
    """
    if test_col.find().count() == 1000:
        return
    
    test_col.remove({})
    
    complexity = 10
    data = list()
    for i in range(complexity):
        for j in range(complexity):
            for k in range(complexity):
                data.append({"a": i, "b": j, "c": k})
    test_col.insert(data)

prepare_data()


def distinct_on_one_field():
    """计算文档中的a项的所有不同的值。
    """
    for doc in test_col.find({}).distinct("a"):
        print(doc)
    
# distinct_on_one_field()


def distinct_on_multiple_field():
    """计算文档中a, b两项的组合的所有不同的值。
    """
    pipeline = [
        {
            "$group": {"_id": {"a": "$a", "b": "$b"}},        
        },
    ]
    for doc in test_col.aggregate(pipeline):
        print(doc)
    
# distinct_on_multiple_field()


def count_distinct():
    """计算a, b有多少种不同的组合。本例中用了3种方法实现, 其中method1最佳。
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
        doc = list(test_col.aggregate(pipeline))[0]
        print(doc["count"])
        
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
        for doc in test_col.aggregate(pipeline):
            counter += 1
        print(counter)
    
    def method3():
        """遍历所有数据, 手动排重。
        """
        s = set()
        for doc in test_col.find({}, {"a": True, "b": True}):
            s.add("%s-%s" % (doc["a"], doc["b"]))
        print(len(s))

    st = time.clock()
    method1()
    print(time.clock() - st)
     
    st = time.clock()
    method2()
    print(time.clock() - st)
    
    st = time.clock()
    method3()
    print(time.clock() - st)
    
# count_distinct()

def freq_on_a_b():
    pipeline = [
        {
            "$group": {
                "_id": {"a": "$a", "b": "$b"}, "count": {"$sum": 1},
            },
        },
    ]
    for doc in test_col.aggregate(pipeline):
        print(doc)
freq_on_a_b()