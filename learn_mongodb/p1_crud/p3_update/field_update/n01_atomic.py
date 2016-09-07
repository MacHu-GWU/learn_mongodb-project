#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Atomic update:

Update和其他操作不一样, 在原子性上要非常小心。原则上: **千万不要使用Query取得
要Update的值, 通过一些计算后, 然后再使用 $set 设定新的值, 这样会有潜在的影响
原子性的结果**, 下面举例说明::

    # 假设我们有一个点赞技术器的应用, 如果有多个客户端程序对同一个值进行修改
    # 如果我们使用下面的代码
    # 1. 插入一条新数据
    collection.insert({"_id": "counter_01", "thumb_up": 0})
    
    # 2. 取得thumb_up值
    doc = collection.find_one({"_id": "counter_01"})
    
    # 3. 对value值进行加1
    collection.update({"_id": "counter_01"}, {"$set": {"thumb_up": doc["thumb_up"] + 1}})
    
假设在2 - 3的过程中有多个客户端同时在运行, 我们的应用的本意应该是有N个客户端,
thumb_up的值就加N。但是如果这些客户端在一个很短的时间内同时进行这一操作, 那么
就会导致结果不是我们的预期值。而正确的做法应该是使用服务端的原子性操作 $inc。
具体方法请参考下面的例子。
"""

from learn_mongodb.db_test import col


def thumb_up_by_id_v1(_id):
    """Wrong implement.
    """
    doc = col.find_one({"_id": _id})
    if doc:
        col.update({"_id": _id}, {"$set": {"thumb_up": doc["thumb_up"] + 1}})
        
        
def thumb_up_by_id_v2(_id):
    """Correct implement.
    """
    col.update({"_id": _id}, {"$inc": {"thumb_up": 1}})
    
    
if __name__ == "__main__":
    col.insert({"_id": "counter_01", "thumb_up": 0})
    
    # 虽然能用, 但是有潜在的原子性危险
    thumb_up_by_id_v1("counter_01")
    assert col.find_one({"_id": "counter_01"})["thumb_up"] == 1
    
    # 正确的方法
    thumb_up_by_id_v2("counter_01")
    assert col.find_one({"_id": "counter_01"})["thumb_up"] == 2