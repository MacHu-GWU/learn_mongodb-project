.. image:: https://img.shields.io/badge/Tag-MongoDB-brightgreen.svg
   :target: https://www.mongodb.com/

.. image:: https://img.shields.io/badge/Tag-Replica_Set-brightgreen.svg
   :target: https://docs.mongodb.com/manual/replication/

连接Replica-Set中的一个小坑
=========================
MongoDB的一个非常强大的特性就是用replica set(复制集)来保持 `High availability <https://en.wikipedia.org/wiki/High_availability>`_ (`高可用性 <http://baike.baidu.com/view/2850255.htm>`_)。 而作为一个分布式系统, 复制集之间的主从关系发生变化是非常常见的。但是, **如果你的客户端跟数据库的连接设置不当, 则将会带来灾难性的后果**。

.. image:: replica-set-read-write-operations.png
	:target: https://www.mongodb.com/

我们在开发的时候, 通常我们是通过一个单一的Url, 直接连接我们的数据库的。**而生产环境下, 如果单一连接的primary挂掉, 即使secondary马上顶上变成primary, 可由于连接还是指向primary, 这将导致数据库不可用的严重后果**!

根据 `Connect String <https://docs.mongodb.com/manual/reference/connection-string/>`_ 的官方文档, MongoDB的连接字符串中, **需依次包含所有的replica set的连接信息, 这样连接会自动判断哪个是primary, 哪个是secondary**。当主/从发生变化时, 连接会立刻得知, 并作出响应。

作为补充说明, 在这些场景中, 复制集的主-从关系可能会发生变化, 可见primary/secondary的自动变化是经常发生的事:

- 轮转升级: 依次升级复制集的版本, 先升级secondary的复制集, 然后将升级好的复制集变成primary, 再升级其他的复制集。
- primary宕机: primary挂掉, 立刻从secondary中选举出一个作为primary, 继续为客户端服务。当挂掉的primary恢复时, 不再转换回来, 就以secondary的身份工作着。
- 网络分区(`Partition tolerance <https://en.wikipedia.org/wiki/Network_partition>`_): 是一种当某些关键节点出错时, 导致服务器之间无法互相通讯的状态。例如: 我们有1个primary和4个secondary, 但每次写入primary的时候primary并不会分发数据到所有的secondary, 而是只发给2和3, 然后分别由2和3转发给4和5。那么如果2或3挂了, 就会导致4或5无法和primary连接上。


.. 常用连接参数

.. 如何实现读写分离？

.. 在options里添加readPreference=secondaryPreferred即可实现，读请求优先到Secondary节点，从而实现读写分离的功能，更多读选项参考Read preferences

.. 如何限制连接数?

.. 在options里添加maxPoolSize=xx即可将客户端连接池限制在xx以内。

.. 如何保证数据写入到大多数节点后才返回?

.. 在options里添加w= majority即可保证写请求成功写入大多数节点才向客户端确认，更多写选项参考Write Concern


参考资料
-------
- `MongoDB Driver：使用正确的姿势连接复制集 <http://www.mongoing.com/archives/2642>`_
- `Connection String <https://docs.mongodb.com/manual/reference/connection-string/>`_