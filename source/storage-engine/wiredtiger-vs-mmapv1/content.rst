.. image:: https://img.shields.io/badge/Tag-MongoDB-brightgreen.svg
   :target: https://www.mongodb.com/

.. image:: https://img.shields.io/badge/Tag-WiredTiger_vs_MMapV1-brightgreen.svg
   :target: https://docs.mongodb.com/manual/faq/storage/


.. _wiredtiger_vs_mmapv1:

新旧存储引擎比较, WiredTiger与MMAPv1
====================================
下表列出了一些主要的异同点。

.. list-table:: WiredTiger vs MMAP v1
   :widths: 20 20 20
   :header-rows: 1

   * - 
     - WiredTiger
     - MMAPv1
   * - Write Performance
     - Excellent (No need padding)
     - Good (Need padding)
   * - Concurrency Control
     - Document Level
     - Collection Level
   * - Read Performance
     - Excellent
     - Excellent
   * - Compression Support
     - Yes
     - No
   * - Cache
     - WiredTiger Cache & File System Cache
     - Only Journal
   * - Platform Availability
     - Linux, Windows, MacOS, Solaris(x86)
     - Linux, Windows, MacOS


WiredTiger
-------------------------------------------------------------------------------


Two Caches
~~~~~~~~~~
WT引擎使用了二阶缓存WiredTiger Cache, File System Cache来保证Disk上的数据的最终一致性。

- WiredTiger Cache是内存中的缓存
- File System是本地数据文件中的缓存
- Disk是最终硬盘上的数据文件

每隔60秒, 或当Journal文件超过2GB, 会有一个叫Checkpoints的事件, WT会把WT Cache中的数据存入FS Cache, 然后一次性将所有改变应用到磁盘上。换言之, **如果你既没有用Replica Set, 也没有用Journal。那么在你宕机的时候仍然能从最后一个Checkpoints恢复数据**。


Document Level Locking
~~~~~~~~~~~~~~~~~~~~~~
虽然WT并不会对Document进行上锁, 但WT使用了一种非常先进的Concurency Control(并发控制)技术, 使得实际效果和Document一样, 但是性能却没有损失。


Compression
~~~~~~~~~~~
WiredTiger的数据是经过压缩的, 在MMAPv1中是没有经过压缩的。 默认情况下使用 `Google Snappy <http://google.github.io/snappy/>`_ 进行压缩。 **Snappy的特点是快, 比大多数算法要快很多, 而只牺牲了一点点压缩率**。WiredTiger还支持 `zlib <http://zlib.net/>`_ 压缩, 这样会比Snappy压缩率高一点点, 但速度慢很多。当然, 你也可以设定为和MMAPv1一样, 不压缩。


MMAPv1
------
MMAP的全称是Map files into Memory, 使用了一种将磁盘上的文件映射到内存的技术。

写入数据时, 首先会将数据写入到内存, 然后每隔60秒会将内存中的数据写入磁盘。而写入磁盘前, 会以每100毫秒一条的速度将数据先写入Journal, 然后再写入磁盘。换言之, 当数据写入Journal之后, 即使数据库挂掉, 也可以从Journal中恢复数据。但是和WiredTiger不同的是, **如果你既没有用Replica Set, 也没有用Journal, 那么很有可能会出现在数据写入磁盘的过程中服务器挂掉, 而导致数据不完整, 而此时, 是无法恢复到正常状态的**!


Collection Level Locking & Database Level Locking
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
MMAP使用Multiple Readers and Single Writer Lock来保证数据一致性。当多个Reader在读数据时, 所有的Writer就都无法工作。**而一个Writer在写数据时, 不仅完全不允许其他Writer进行操作, 连其他Reader都不允许读数据**。

什么是Shared Resources?

- Data
- Metadata
	- Indexes: 在Update多个文档时, 可能会影响同一个Index。
	- Journal: Write ahead Log, 在真正执行写操作之前, 数据引擎会将数据写入Journal Log, 然后才真正写入数据。


Padding
~~~~~~~
MMAPv1使用的是线性存储。为了使得同一个文档的数据在磁盘上也保持在相同的位置上, 我们需要解决 "当对文档进行更新时, 如果文档是无缝紧密排列的, 那么多出的空间就需要被放在磁盘的别处" 这一问题。MMAPv1是这样解决的:

在写入时, MMAPv1会为文档预分配一定的磁盘空间, 32KB, 64KB, ..., 2MB, 如果文档超过2MB, 则会自动向上fix到2MB的倍数。当然, 文档大小不能超过16MB的限制。而预分配空间和文档实际占用的磁盘大小之间的差值, 会用Padding来补足。

注意, 由于新引擎WiredTiger使用的是BTree存储, 不是线性存储, 所以压根不需要Padding。


**结论, 如果你不是在用Solaris系统, 毫无疑问你应该使用WiredTiger引擎**。


参考资料
--------
- `Storage Engine FAQ <https://docs.mongodb.com/manual/faq/storage/>`_
- `WiredTiger Internal <https://www.youtube.com/watch?v=O9TGqK3FBX8>`_
- `MMAPv1 Internal <https://www.youtube.com/watch?v=PZCdLVB4lw4>`_
- `MongoDB MMAPv1 vs WiredTiger storage engines <http://dba.stackexchange.com/questions/121160/mongodb-mmapv1-vs-wiredtiger-storage-engines>`_
