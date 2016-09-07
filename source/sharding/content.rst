Sharding (分片)
===============
NoSQL相比RelationDB最大的区别就是其超强的横向扩展性。 而Sharding即是MongoDB用于横向扩展的关键技术。所谓Sharding就是, 在你的数据增大到一定的程度, 导致查询变得很慢的时候, 将数据分片到不同的主机上, 使得性能不会随着数据体积的增大而急剧下降。

由于MongoDB没有Join, Collection之间没有强制关联, 所以Sharding是在MongoDB是针对Collection级的操作。

Sharding的具体实现是通过Sharding Key来实现的。也就是


Sharding Key FAQ
================

是否可以有多个field做Shard Key?
-------------------------------------------------------------------------------
不行。


是否可以在Sharding之后, 改变Shard Key?
-------------------------------------------------------------------------------
不行! Sharding Key一旦确定, 是无法改变的, 如果你一定要改变, 只有将所有数据dump到磁盘, 然后drop掉collection, 最后重新向新的collection中添加数据。**



Glossary
--------

.. list-table:: Sharding Glossary (分片相关术语列表)
   :widths: 50 50
   :header-rows: 1

   * - English
     - 中文
   * - Sharding
     - 分片
   * - Sharded Cluster
     - 被分片的集群
   * - Partition
     - 分区, 多个分片中的一个
   * - Sharding Key
     - 分片主键
   * - Hash Key
     - 散列主键
   * - Range Key
     - 区间主键
   