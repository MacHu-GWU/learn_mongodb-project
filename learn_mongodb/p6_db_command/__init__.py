#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Run this file first.
"""

from learn_mongodb.db_test import client, db


def prepare():
    import random
    from datetime import datetime
    from sfm.rnd import simple_faker

    client.drop_database(db)

    user_data = [{"name": simple_faker.fake.name()} for i in range(1000)]
    db.user.insert(user_data)

    log_data = [
        {
            "time": str(datetime.now()),
            "activity": random.choice(["log in", "sign out"]),
            "user": random.choice(user_data)["name"],
        } for i in range(5000)
        ]
    db.log.insert(log_data)


if __name__ == "__main__":
    prepare()
