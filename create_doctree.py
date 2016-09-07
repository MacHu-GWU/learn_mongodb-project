#!/usr/bin/env python
# -*- coding: utf-8 -*-

import docfly

doc = docfly.DocTree("source")
doc.fly()

package_name = "learn_mongodb"
     
doc = docfly.ApiReferenceDoc(
    package_name, 
    dst="source",
    ignore=[
        "%s.zzz_manual_install.py" % package_name,
    ]
)
doc.fly()