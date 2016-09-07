#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Aggregation中的pipeline主要和Projection Operator打交道。

Projection在MongoDB中的概念类似于Sql的Aggregate。不过通常Sql中的Aggregate是对于
单片数据库而言的。对于可以无限sharding的MongoDB来说, Projection更像Mapreduce。

ref: https://docs.mongodb.com/manual/aggregation/
"""
