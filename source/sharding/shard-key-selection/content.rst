Shard Key Selection (如何选择Shard Key)
=======================================
无论是Hash Key还是Range Key, 最终的目的只有两个: 

1. 减小每台机器的负载, 提高性能。
2. 优化查询。

根据 `M102 12 Shard Key Selection <https://www.youtube.com/watch?v=WU5rIUKJ9Fo&list=PL4MMeiBrna_boDt-aKkcIyj0tuHJG8GGH&index=7>`_ 课程中的解说, 选择Shard Key主要要考虑下面四个方面

- the shard key is common in query. (Shard Key是否是一个常见的查询模式)
- good "cardinality" and "granularity". ("粒度"不错, 换言之在整个Collection中, 大部分的文档的Shard Key都不相同)
- consider compound shard keys. (如果所有的Field的 "粒度" 都不高, 则考虑使用Compound Shard Key)
- is the key monotonically increasing? ()


参考资料
--------
- `M102 12 Shard Key Selection <https://www.youtube.com/watch?v=WU5rIUKJ9Fo&list=PL4MMeiBrna_boDt-aKkcIyj0tuHJG8GGH&index=7>`_