#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
对于体积小于16MB的文件, 我们可以以Binary的形式储存在数据库中。但一旦文件大于
16MB, 那么我们就需要用到GridFS系统。GridFS的实质是将大文件分拆成小文件, 并
表上序号, 然后将小文件储存在一个Collection中, 大文件的metadata储存在另一个
Collection中。

Ref:

- https://docs.mongodb.com/manual/core/gridfs/
- http://api.mongodb.com/python/current/examples/gridfs.html
"""

from learn_mongodb.db_test import db, col
import gridfs
from bson import ObjectId
import hashlib

def md5_of_content(binary):
    m = hashlib.md5()
    m.update(binary)
    return m.hexdigest()

fs = gridfs.GridFS(db)
content = "Hello World".encode("utf-8")
# filename = "text.txt"
# extension = ".txt"
# _id = fs.put(content, filename=filename, extension=extension)

# gf = fs.get(_id)
# print(gf)
# print(gf.filename)
# print(gf.extension)
# print(gf.read())

md5 = md5_of_content(content)
gf = fs.find_one({"extension": ".txt"})
print(gf.extension)

