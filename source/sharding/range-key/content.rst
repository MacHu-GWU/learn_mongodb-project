.. _range_key_sharding:

Range Key Sharding
==================
Range Key是使用Document中的某一个Field作为关键字, 按照区间将文档映射到不同的Partition上。这非常好理解, 比如我们的文档是: ``{name: "Jack", age: 20}``, 而我们使用 ``name`` 作为Range Key, 比如我们有13个机器, 以a - b开头的放在1号机器, c - d开头的放在2号机器。


.. _range_key_con:

Range Key的优点
---------------

更快的查询
~~~~~~~~~~
在使用Range Key做查询的时候, **无需访问Cluster中的所有Partition**, 有可能我们 **只需要对区间内所影响到的机器** 进行查询 - 汇总即可。而Hash Key必须访问所有的Partition。**所以在Sharding Key是我们的主要查询模式时, 性能上有优势**。


更快的排序
~~~~~~~~~~


.. _range_key_pro:

Range Key的缺点
---------------
与Hash Key不同的是, 我们需要小心的选择Range Key才能使得各个Partition上的数据保持尽量平衡(Hash Key无论怎么选择基本上都会比较平衡)。而很多情况下, 无论我们怎么选择哪一项作为Range Key, 都无法保证这一点。



Split and Migrate Operation
---------------------------
M102视频中的内容, 没有太听懂。


Load Balancer
-------------
MangoDB在Sharding的Load Balance的实现中有3个主要部件:

1. Sharding Cluster, 
2. Metadata Server, 储存了Sharding Key的Metadata数据, 比如Hash Key和Range Key对应的Partition的Id。这个Server其实是一个小型的MongoDB, 通常由一个3个备份的Replica Set组成。
3. MongoD, 是Load Balance程序进程, 无需储存任何文件, 可以由任意多台机器构成。

所以整个流程看起来是这样: 当Client发起一个Read/Write请求时, 首先会到达MongoD; 然后MongoD会跟Metadata Server沟通, 获得下一步的指示; 最后对所有相关的Partition进行操作。


参考资料
--------
- `M102 Sharding Intro <https://www.youtube.com/watch?v=j2mYoEW9ehk>`_