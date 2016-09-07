#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``$size`` 查询符根据array中元素的数量匹配文档。请注意, 不支持对size的区间查询。若
你非常需要类似于 size >= 5 这样的查询, 请为你的文档增加一个叫做 array_count 的
项, 然后对该项进行查询。但是对于update而言, 为array使用 ``$push`` 添加元素后, 还
需要用 ``$inc`` 进行size的更新。

Ref: https://docs.mongodb.com/manual/reference/operator/query/size/
"""