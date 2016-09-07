#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
使用下面的代码import的database和collection, 保证是全空, 无文档, 无index的
初始状态::

    from learnMongo.emptydatabase import db, col
"""

from learnMongo.database import db, col, drop_all

drop_all()