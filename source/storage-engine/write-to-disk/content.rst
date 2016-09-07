.. image:: https://img.shields.io/badge/Tag-MongoDB-brightgreen.svg
   :target: https://www.mongodb.com/

.. image:: https://img.shields.io/badge/Tag-Storage_Engine_FAQ-brightgreen.svg
   :target: https://docs.mongodb.com/manual/faq/storage/


.. _write_to_disk:

内存中的数据是以怎样的方式被写入磁盘的
======================================
MongoDB启动时会将所有的index信息读取到内存中, 因为index信息是防止duplicate key的关键, 所以要用内存保证其高性能。 而在写操作发生时:

1. MongoDB会首先将数据首先写入到内存中(如果成功的话)
2. 然后按照是否开启日志的设置, 写入到日志中
3. **按照一定的机制 (每隔一段时间, 或者日志文件到达一定体积) 时将内存中的数据写入磁盘**。

这一流程是有数据存储引擎控制的, 而目前MongoDB有三大数据引擎, 从最新到最老分别是:

- `WiredTiger <https://docs.mongodb.com/manual/core/wiredtiger/>`_
- `MMAPv1 <https://docs.mongodb.com/manual/core/mmapv1/>`_
- `In-Memory <https://docs.mongodb.com/manual/core/inmemory/>`_

不同的引擎有着不同的设定。 具体机制请参考如下官方文档:

- WiredTiger: https://docs.mongodb.com/manual/faq/storage/#how-frequently-does-wiredtiger-write-to-disk
- MMapv1: https://docs.mongodb.com/manual/faq/storage/#how-frequently-does-mmapv1-write-to-disk
- In-Memory: 没有写入磁盘的机制。