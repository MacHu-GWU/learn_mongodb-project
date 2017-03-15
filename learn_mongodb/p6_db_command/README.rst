Mongodb export, import, dump, restore, repair commands
===============================================================================
- mongoexport/mongoimport是一对反操作，主要用于collection级的操作。
- mongodump/mongorestore是一对反操作, 主要用于database级的操作。


备份和恢复整个数据库
-------------------------------------------------------------------------------
将整个数据库 **备份到文件夹**:

.. code-block:: console

	mongodump --db test --out C:\backup
	mongorestore --db test C:\backup\test

将整个数据库备份到 **单个文件**:

.. code-block:: console

	mongodump --archive=test.2017-01-01.archive --db test
	mongorestore --archive=test.2017-01-01.archive --db test

只要添加 ``--gzip`` 命令即可使用压缩模式。

Ref:

- https://docs.mongodb.com/manual/reference/program/mongodump/#examples
- https://docs.mongodb.com/manual/reference/program/mongorestore/#examples


导出和导入数据
-------------------------------------------------------------------------------
.. code-block:: console

	mongoexport --db test --collection user --type=json --out user.json
	mongoimport --db test --collection user --file user.json

更多import的参数可以参考官方文档。

Ref:

- https://docs.mongodb.com/manual/reference/program/mongoexport/#use
- https://docs.mongodb.com/manual/reference/program/mongoimport/#use


当数据库非正常关机时的恢复
-------------------------------------------------------------------------------
1. Create a backup of the data files.
2. Start mongod with --repair. ``mongod --dbpath /data/db --repair``

Ref： https://docs.mongodb.com/manual/tutorial/recover-data-following-unexpected-shutdown/
