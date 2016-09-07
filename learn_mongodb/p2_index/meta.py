#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pymongo
from learn_mongodb.database import client, col
from learn_mongodb.fake import fake

n = 1000
data = [{"_id": i, "name": fake.name()} for i in range(n)]
# 插入一些数据
col.insert(data)
col.create_index([("name", pymongo.ASCENDING)])